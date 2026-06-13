<div align='center'>
  <h1>DeepSeek 自动化周报生成器</h1>
  <h3>📝 输入关键词，一键生成结构化周报</h3>
  <p><em>基于 DeepSeek API 的智能周报生成工具，告别手动写周报的烦恼</em></p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/DeepSeek-API-0066FF?style=flat" alt="DeepSeek"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License"/>
</div>

---

## 🎯 项目介绍

&emsp;&emsp;每周写周报是不是很头疼？明明做了很多工作，却不知道怎么组织语言？这个工具帮你解决烦恼！

&emsp;&emsp;DeepSeek 自动化周报生成器是一个基于 DeepSeek API 的智能工具，你只需要输入本周的工作关键词或简要描述，AI 就能帮你生成一份结构化的专业周报。支持两种风格：正式专业版用于工作汇报，轻松活泼版用于团队内部分享。

## ✨ 功能特点

- 📝 **智能生成** - 根据关键词自动生成结构化周报
- 🎨 **双风格可选** - 正式专业 / 轻松活泼两种风格
- 💾 **自动保存** - 生成后自动保存为 Markdown 文件
- 🔄 **流式输出** - 实时显示生成过程，打字机效果
- 📊 **结构完整** - 包含工作总结、重点成果、问题解决、下周计划

## 📚 快速开始

### 1. 安装依赖

```bash
pip install openai python-dotenv
```

### 2. 配置 API 密钥

在项目根目录创建 `.env` 文件：

```env
DEEPSEEK_API_KEY=your_api_key_here
```

### 3. 运行程序

```bash
python report_generator.py
```

## 📖 使用示例

```
==================================================
   DeepSeek 自动化周报生成器
==================================================

请输入本周的工作内容（关键词或简要描述即可）：
示例：完成了用户登录模块开发，修复了3个bug，参加了需求评审会议

>>> 完成了用户登录模块开发，修复了3个bug，参加了需求评审会议

选择周报风格：
1. 正式专业 (默认)
2. 轻松活泼
请选择 (1/2，默认1): 1

正在生成周报，请稍候...

## 本周工作总结
- 完成用户登录模块的开发工作，支持手机号和邮箱登录
- 修复了3个影响用户体验的Bug
- 参与了产品需求评审会议，明确了下周开发方向

周报已保存到: output/weekly-report-2024-01-15.md
```

## 📁 项目结构

```
deepseek-weekly-report/
├── .env                 # API 密钥配置
├── report_generator.py  # 主程序
├── README.md            # 项目说明
└── output/              # 生成的周报存放目录
```

## 🔧 技术栈

- **Python 3.8+** - 主要编程语言
- **DeepSeek API** - 大语言模型服务
- **OpenAI SDK** - API 调用工具

## 💡 如何学习

&emsp;&emsp;本项目适合作为 LangChain/AI 应用开发的入门练习。通过这个项目，你将学习到：

- 如何调用大语言模型 API
- 如何设计有效的 Prompt
- 流式输出的实现方式
- 文件操作和环境变量管理

&emsp;&emsp;建议你亲手运行代码，尝试修改 Prompt 模板，观察不同输入对输出的影响。

## 🤝 如何贡献

欢迎任何形式的贡献！

- 🐛 **报告 Bug** - 发现问题请提交 Issue
- 💡 **提出建议** - 有更好的想法欢迎讨论
- 📝 **完善功能** - 提交你的 Pull Request

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。