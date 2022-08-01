import nonebot.plugin
from nonebot import get_driver

from .config import Config
from .const import consts
from .handler import query, submit

__plugin_meta__ = nonebot.plugin.PluginMetadata(
    name='Nonebot2 Plugin Hammer Nbnhhsh',
    description='Nonebot2查询nbnhhsh',
    usage=f'''欢迎使用Nonebot2 nbnhhsh
    注：在下文中，“缩写”的定义为“仅由字母或阿拉伯数字中任意一种或两种所构成的长度大于1的连续字符串”
    {consts.command_prefix}nbnhhsh <一段话> 查询该段话中所有缩写所代表的含义
    {consts.command_prefix}nbnhhsh.submit <缩写> <含义> 为「好好说话」项目贡献词条，“含义”末尾可通过括号包裹（简略注明来源），经人工审核将整理录入''',
    extra={
        "version": "1.0.0",
        "repository": "https://github.com/ArgonarioD/nonebot-plugin-hammer-nbnhhsh"
    }
)

global_config = get_driver().config
config = Config.parse_obj(global_config)