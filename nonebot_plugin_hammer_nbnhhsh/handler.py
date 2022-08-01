import httpx
from httpx import Response
from nonebot.adapters.onebot.v11 import MessageEvent, Message
from nonebot.internal.matcher import Matcher
from nonebot.internal.params import ArgPlainText, Arg
from nonebot.params import CommandArg
from nonebot.plugin.on import on_command

from nonebot_plugin_hammer_core.util.message_factory import reply_text
from .const import consts

query = on_command("nbnhhsh")
submit = on_command("nbnhhsh.submit")


def get_trans_result_str(trans: list[dict, ...]) -> str:
    result = []
    for word in trans:
        s = str()
        s += f"- {word[consts.QUERY_KEY_NAME]}"
        if consts.QUERY_KEY_TRANS in word:
            s += f":\n {' '.join(word[consts.QUERY_KEY_TRANS])}"
        elif word[consts.QUERY_KEY_INPUTTING] is not None and len(word[consts.QUERY_KEY_INPUTTING]) > 0:
            s += f" 有可能是:\n {' '.join(word[consts.QUERY_KEY_INPUTTING])}"
        else:
            s += f':\n 尚未录入，可以自行使用"{consts.command_prefix}nbnhhsh.submit {word["name"]} <含义>"命令提交对应文字，“含义”末尾可通过括号包裹（简略注明来源）'
        result.append(s)
    return '\n'.join(result)


@query.handle()
async def handle_query(event: MessageEvent, args: Message = CommandArg()):
    response = Response
    try:
        response = httpx.post(consts.API_URL + 'guess', data={'text': args.extract_plain_text()}, timeout=3)
        response.raise_for_status()
    except httpx.RequestError as exc:
        await query.finish(reply_text(f'访问API出错！错误信息：{exc}', event))
    r_body = response.json()
    if len(r_body) == 0:
        await query.finish(reply_text('没有找到有关该段文字中的任何缩写信息', event))
    await query.finish(reply_text(get_trans_result_str(r_body), event))


@submit.handle()
async def handle_submit(matcher: Matcher, event: MessageEvent, args: Message = CommandArg()):
    raw_args = args.extract_plain_text().strip().split(' ')
    if len(raw_args) != 2:
        await query.finish(reply_text('参数数量错误', event))
    matcher.set_arg(consts.QUERY_KEY_NAME, Message(raw_args[0].strip()))
    matcher.set_arg(consts.QUERY_KEY_TRANS, Message(raw_args[1].strip()))


@submit.got("confirm", prompt="您确认要提交该词条吗（输入Y确认）")
async def handle_submit_confirm(
        event: MessageEvent,
        name: str = ArgPlainText(consts.QUERY_KEY_NAME),
        trans: str = ArgPlainText(consts.QUERY_KEY_TRANS),
        confirm: Message = Arg()
):
    if confirm.extract_plain_text().upper() == 'Y':
        try:
            response = httpx.post(consts.API_URL + 'translation/' + name, data={'text': trans}, timeout=3)
            response.raise_for_status()
        except httpx.RequestError as exc:
            await query.finish(reply_text(f'访问API出错！错误信息：{exc}', event))
        await submit.finish(reply_text(f'成功提交 {name}: {trans} 至好好说话项目API，审核通过后此词条将会生效', event))
    await submit.finish(reply_text('已取消提交', event))
