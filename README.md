<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# Nonebot Plugin Hammer Nbnhhsh

✨ 基于onebot、nonebot2与「好好说话」项目的 字母/数字缩写含义查询及提交插件 ✨
</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/ArgonarioD/nonebot-plugin-hammer-nbnhhsh/main/LICENSE">
    <img src="https://img.shields.io/github/license/ArgonarioD/nonebot-plugin-hammer-core" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-hammer-nbnhhsh">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-hammer-nbnhhsh.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.9-blue.svg" alt="python">
  <img src="https://img.shields.io/badge/Onebot-v11-lightgrey" alt="onebot11">
  <img src="https://img.shields.io/badge/nonebot-2.0.0b4-orange" alt="nonebot2">
  <a href="https://github.com/ArgonarioD/nonebot-plugin-hammer-core">
    <img src="https://img.shields.io/badge/hammer--core-0.1.1-green" alt="hammer-core">
  </a>
</p>

## 使用本插件

### 1. 使用nb-cli安装（推荐）

在命令行中执行`nb plugin install nonebot-plugin-hammer-nbnhhsh`安装即可

### 2. 使用包管理工具安装（用pip举例）

1. 在命令行中执行`pip install nonebot-plugin-hammer-nbnhhsh`安装python包
2. 在`bot.py`中添加`nonebot.load_plugin('nonebot-plugin-hammer-nbnhhsh')`

## 命令
> 注：
>  - 本节中的命令省略了命令前缀，本插件的命令前缀采用了`.env`文件配置中的`COMMAND_START`的值，默认情况下是`/`，也就是说，在你没有自行配置过`.env`文件的情况下，本插件提供的命令如`/nbnhhsh <一段话>`
>  - 在下文中，“缩写”的定义为“仅由字母或阿拉伯数字中任意一种或两种所构成的长度大于1的连续字符串

| 命令                       | 说明                                             |
|--------------------------|------------------------------------------------|
| nbnhhsh <一段话>            | 查询该段话中所有缩写所代表的含义                               |
| nbnhhsh.submit <缩写> <含义> | 为「好好说话」项目贡献词条，“含义”末尾可通过括号包裹（简略注明来源），经人工审核将整理录入 |

## 主要功能效果
例命令（`COMMAND_START`配置为默认值）：
```
/nbnhhsh u1s1，nsdd，但是你有没有想过ababa是怎么想的，nm有，nzzhnzz
```
机器人回复：
```
- u1s1:
 有一说一
- nsdd:
 你说的对 你是对的 你是弟弟 诺森德岛 你萨顶顶 你神叨叨 你手短短 南山大道 泥塑敦敦 你射得多 你塞蛋蛋 泥兽段段 你屎多多 你是大雕 男神代代 扭扭捏捏 你耍大刀 你水多多 你稍等等 内射到顶 铃声多多
- nm:
 纳米 你妈 你妹 农民 normal Nicki Minaj 柠檬 奶妈 妮妙 诺民（NCT成员李帝努和罗渽民的cp） no miss 嫩模 Nuclear missile 牛马 尼玛（网络） 你没事吧 匿名 内幕（网络） 年迈 nano machine
- ababa 有可能是:
 Ababa
- nzzhnzz:
 尚未录入，可以自行使用"/nbnhhsh.submit nzzhnzz <含义>"命令提交对应文字
```
## 测试环境
- Python 3.9
- go-cqhttp v1.0.0-rc3
- nonebot 2.0.0-beta.4

## 鸣谢

- [onebot](https://github.com/botuniverse/onebot)
- [nonebot2](https://github.com/nonebot/nonebot2)
- [能不能好好说话？](https://github.com/itorr/nbnhhsh)

---
~~*如果觉得有用的话求点个Star啵QwQ*~~