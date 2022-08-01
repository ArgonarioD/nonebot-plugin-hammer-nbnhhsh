from nonebot import get_driver

from nonebot_plugin_hammer_core.util.constant import ConstNamespace

consts = ConstNamespace.nbnhhsh

consts.API_URL = 'https://lab.magiconch.com/api/nbnhhsh/'
consts.command_prefix = list(get_driver().config.command_start)[0]
consts.QUERY_KEY_NAME = 'name'
consts.QUERY_KEY_TRANS = 'trans'
consts.QUERY_KEY_INPUTTING = 'inputting'
