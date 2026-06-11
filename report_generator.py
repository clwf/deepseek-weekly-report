"""
DeepSeek 自动化周报生成器
功能：输入本周工作关键词，自动生成结构化周报
"""

import os
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 初始化 DeepSeek 客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"  # DeepSeek 的 API 地址
)


def generate_report(topics: str, style: str = "professional") -> str:
    """
    根据关键词生成结构化周报

    Args:
        topics: 本周工作关键词或简要描述
        style: 风格 - professional(正式) / casual(轻松)

    Returns:
        生成的周报文本
    """

    # System Prompt：定义 AI 的角色和输出格式
    system_prompt = """你是一位专业的周报撰写助手。请根据用户提供的工作内容，
生成一份结构化的周报，包含以下部分：

1. **本周工作总结**（3-5个要点，每个要点一句话概括）
2. **重点成果**（本周最值得说的1-2个成果）
3. **遇到的问题与解决方案**（如果用户提到了问题）
4. **下周计划**（根据本周内容合理推断2-3条）

要求：
- 语言简洁专业，不要废话
- 用数据说话（如果没有具体数据就合理估算）
- 总字数控制在300-500字"""

    # 根据风格调整
    if style == "casual":
        system_prompt += "\n风格要求：轻松活泼，可以用一些口语化表达。"

    # User Prompt：用户的实际输入
    user_prompt = f"这是我本周的工作内容：{topics}。请帮我生成周报。"

    print("正在生成周报，请稍候...\n")

    # 调用 DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-chat",  # DeepSeek-V3 模型
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,   # 控制创造性，0.7 是比较平衡的值
        max_tokens=1000,   # 最大输出长度
        stream=True        # 流式输出，打字机效果
    )

    # 流式读取并打印结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            print(text, end="", flush=True)
            full_response += text

    print("\n")  # 换行
    return full_response


def save_report(report: str, filename: str = None) -> str:
    """
    将周报保存为 Markdown 文件

    Args:
        report: 周报内容
        filename: 文件名（可选，默认按日期命名）

    Returns:
        保存的文件路径
    """
    # 确保 output 目录存在
    os.makedirs("output", exist_ok=True)

    if filename is None:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"output/weekly-report-{today}.md"

    # 写入文件
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 周报 - {datetime.now().strftime('%Y年%m月%d日')}\n\n")
        f.write(report)
        f.write(f"\n\n---\n*由 DeepSeek 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")

    print(f"周报已保存到: {filename}")
    return filename


def main():
    """主函数：交互式周报生成"""
    print("=" * 50)
    print("   DeepSeek 自动化周报生成器")
    print("=" * 50)
    print()

    # 获取用户输入
    print("请输入本周的工作内容（关键词或简要描述即可）：")
    print("示例：完成了用户登录模块开发，修复了3个bug，参加了需求评审会议，下周要开始做支付功能")
    print()
    topics = input(">>> ").strip()

    if not topics:
        print("输入不能为空，请重新运行。")
        return

    # 选择风格
    print("\n选择周报风格：")
    print("1. 正式专业 (默认)")
    print("2. 轻松活泼")
    choice = input("请选择 (1/2，默认1): ").strip()

    style = "casual" if choice == "2" else "professional"

    # 生成周报
    print()
    report = generate_report(topics, style)

    # 询问是否保存
    print()
    save_choice = input("是否保存为文件？(y/n，默认y): ").strip().lower()
    if save_choice != "n":
        save_report(report)

    print("\n完成！")


if __name__ == "__main__":
    main()
