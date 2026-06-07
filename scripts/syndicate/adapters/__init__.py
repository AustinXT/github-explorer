"""注册所有可用 adapter。新增平台时在此 import 触发 @register。

路线（按 README 的优先级）：
  - wechat        ✅ adapter（复用 scripts/wechat_publish.py 的图片/渲染/草稿逻辑，mode=api）
  - cnblogs       ✅ MetaWeblog API（唯一无需浏览器的国内渠道，mode=api）
  - juejin/csdn   ✅ 浏览器半自动（mode=browser，Claude-in-Chrome 按 playbook 驱动）
  - zhihu/segmentfault  待接，同样走 mode=browser
"""
from . import cnblogs  # noqa: F401
from . import wechat  # noqa: F401
from . import juejin  # noqa: F401
from . import csdn  # noqa: F401
