// 在公众号后台 (mp.weixin.qq.com) 任意业务页（URL 含 ?token=...）的 Console 里跑。
// 翻完所有「群发记录」分页，过滤出 GitHub 项目分析报告合辑（album_id=4452365495291461633）的文章，
// 触发浏览器下载 wechat_published.json 到 ~/Downloads。
//
// 完整三步同步流程：
//   1) pbcopy < scripts/fetch_wechat_published.js  → mp 后台 Console 粘贴回车
//   2) mv ~/Downloads/wechat_published.json tmp/
//      python3 scripts/match_wechat_to_slugs.py     # 拉文章正文 → GitHub URL → 反查 slug
//   3) python3 scripts/apply_wechat_mapping.py --apply  # 写回 src/publish.md
//
// 接口结构（2026-05 实测）：
//   GET /cgi-bin/appmsgpublish?sub=list&begin=N&count=20&token=...&lang=zh_CN
//   → { base_resp, is_admin, publish_page: "<JSON string>" }
//       publish_page parse 后 → { total_count, publish_count, masssend_count, publish_list[] }
//         publish_list[i].publish_info 又是 JSON string → parse 得到 appmsg_info[]、publish_info 等

(async () => {
  const token = new URLSearchParams(location.search).get('token');
  if (!token) { console.error('当前页 URL 没有 token 参数，请在 mp 后台业务页上跑'); return; }
  const PAGE = 20, DELAY_MS = 600, ALBUM_ID = 4452365495291461633;
  const all = [], gh = [];
  let total = null;
  let begin = 0;
  while (true) {
    const url = `/cgi-bin/appmsgpublish?sub=list&begin=${begin}&count=${PAGE}&token=${token}&lang=zh_CN&f=json`;
    const r = await fetch(url, { credentials: 'include' });
    if (!r.ok) { console.error('HTTP', r.status, 'at begin=' + begin); break; }
    const wrap = await r.json();
    if (!wrap.publish_page) { console.error('no publish_page key at begin=' + begin, Object.keys(wrap)); break; }
    let page;
    try { page = JSON.parse(wrap.publish_page); }
    catch (e) { console.error('parse publish_page failed at begin=' + begin, e); break; }
    if (total === null) total = page.total_count || 0;
    const list = page.publish_list || [];
    if (!list.length) break;
    for (const it of list) {
      try {
        const pi = JSON.parse(it.publish_info);
        const outerUpdate =
          (pi.publish_info && pi.publish_info.update_time) ||
          (pi.publish_info && pi.publish_info.create_time) ||
          (pi.sent_result && pi.sent_result.update_time) ||
          (pi.sent_info && pi.sent_info.time);
        for (const am of (pi.appmsg_info || [])) {
          const rec = {
            title: am.title,
            content_url: am.content_url,
            appmsgid: am.appmsgid,
            digest: am.digest,
            album_id: am.appmsg_album_info && am.appmsg_album_info.album_id,
            album_title: am.appmsg_album_info && am.appmsg_album_info.title,
            send_time: (am.line_info && am.line_info.send_time) || outerUpdate,
            update_time: outerUpdate,
            publish_type: it.publish_type,
            read_num: am.read_num,
            like_num: am.like_num,
            comment_num: am.comment_num,
          };
          all.push(rec);
          if (rec.album_id === ALBUM_ID) gh.push(rec);
        }
      } catch (e) { console.error('parse publish_info failed at begin=' + begin, e); }
    }
    console.log(`  begin=${begin} got ${list.length} entries (累计 all=${all.length}, github=${gh.length}, total=${total})`);
    if (list.length < PAGE) break;
    begin += PAGE;
    if (total && begin >= total) break;
    await new Promise(r => setTimeout(r, DELAY_MS));
  }
  const payload = {
    fetched_at: new Date().toISOString(),
    total_count: total,
    collected: all.length,
    github_only: gh.length,
    all,
    github: gh,
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'wechat_published.json';
  document.body.appendChild(a); a.click(); a.remove();
  console.log(`\n✓ 完成：服务端 total=${total}，本次收集 ${all.length} 条，GitHub 合辑 ${gh.length} 条`);
  console.log(`✓ 已触发下载：~/Downloads/wechat_published.json`);
  return { total, collected: all.length, github_only: gh.length };
})();
