<div align='right'><span>Language:&ensp;</span><span><a href='README-zh.md'>zh</a></span>&ensp;<span><abbr title='Need to be translated!'>en</abbr></span>&ensp;<span><a><abbr title='Need to be translated!'>jp</abbr></a></span></div>

<div align="center">
    <a href="http://erajs.net">Homepage</a> |
    <a href="https://github.com/miswanting/Era.js/wiki">Doc</a> |
    <a href="https://github.com/miswanting/Era.js/projects">Roadmap</a> |
    <a href="https://github.com/miswanting/Era.js/issues">Support</a> |
    <a href="https://github.com/miswanting/Era.js/issues">FAQ</a>
</div>



<h1 align="center">Era.js</h1>
<div align="center">Latest Version: v0.2.0-191112</div>
<div align="center"><sub>The following contents is a description of the development target.<br />The current progress is subject to the progress shown in <a href="https://github.com/miswanting/Era.js/projects">Roadmap</a></sub></div>

## Overview

>   Description Updated on: 200326

<div align='center'><img src="ss.png" alt="screenshot" width="33%" /></div>

Era.js is a next-generation cross-platform "era-like" rich text game engine built by JavaScript + Python3, with Python3 as the game script. ~~It is developed based on the Electron application platform and Semantic UI style library.~~<sub>Deleted on 200326, <a href='docs/en/FAQ.md'>Why?<a></sub>

## Notice

Work In Heavy Progress. Ultra-Experimental.

## Development Philosophy

- make full use of HTML5 technology to create a gorgeous, neat, rich, full of design sense of the game front end;
- carefully set up the API so that game developers can worry less about things that have nothing to do with content or gameplay;
- all code cross-platform;
- the development environment, packaging and deployment must be simple and reliable;
-friendly to secondary development;
- in principle, do not cut off any functionality provided by the technology used.
- use the latest technology.

## 引擎特性

- 易于游玩
  - 游戏界面与游戏操作均继承于原 Era 类游戏，并在其基础上进行了相当程度上的优化，弥补了原 Era 类游戏引擎的系统缺陷，并对界面操作逻辑进行了改进；
  - 完全适配 HTML5 富文本显示。
- 易于开发
  - API 设计直观、简洁而全面；
  - 引擎面向游戏开发友好、面向修改友好；
  - 排版、图片、视频、音频等功能将在未来得到游戏引擎原生支持。

## 技术栈（Tech Stack）

### 核心代码

- 前端语言：[JavaScript]()
  - 前端响应式框架：[React](https://reactjs.org/)
  - 样式库（其一）：[Span Charm
  - 发布工具：[Electron Builder](https://www.electron.build/)
- 后端语言：[Python3](https://www.python.org/)
  - 发布工具：[cx_Freeze](https://anthony-tuininga.github.io/cx_Freeze/)
### 桌面端容器

-   应用容器：[Electron](https://electronjs.org/)

### 移动端容器

-   N/A

## 平台支持情况

|   平台支持情况   |  Web   | Windows | MacOS  | Linux | Android |  iOS   |
| :--------------: | :----: | :-----: | :----: | :---: | :-----: | :----: |
|   引擎开发平台   |  N/A   |  可用   | 未验证 | 可用  |   N/A   |  N/A   |
|   游戏开发平台   |  N/A   |  可用   | 未验证 | 可用  |   N/A   |  N/A   |
| 游戏二次开发平台 |  可用  |  可用   |  可用  | 可用  |  可用   |  可用  |
|   游戏运行平台   | 开发中 |  可用   | 未计划 | 可用  | 未计划  | 未计划 |

## 目录结构

-   Core：核心代码
-   Desktop Container：桌面端适配容器
-   Mobile Container：移动端适配容器
-   SDK：软件开发工具包
-   docs：Pages

## 鸣谢

感谢 [qsjl11](https://github.com/qsjl11) 的 [pyera](https://github.com/qsjl11/pyera) 为本项目提供了灵感和 API 名称的参考；