# DeepSeek 自动化周报生成器

> 输入本周工作关键词，自动生成结构化周报，支持导出 Markdown 文件。

## 功能

- 根据关键词自动生成结构化周报
- 支持正式/轻松两种风格
- 流式输出，实时查看生成过程
- 自动保存为带日期的 Markdown 文件
- 支持批量生成和多语言翻译（进阶）

## 快速开始

### 1. 安装依赖
pip install openai python-dotenv

### 2. 配置 API Key
DEEPSEEK_API_KEY=sk-你的密钥

### 3.运行
python report_generator.py
