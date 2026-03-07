"""
04_prompt_chaining.py - 提示词链接示例

演示如何将多个提示词串联起来，每个步骤的输出作为下一个步骤的输入。
"""

from shims.anthropic_sdk import create_message


def example_writing_pipeline():
    """
    内容创作管道：计划 -> 草稿 -> 编辑
    """
    print("内容创作管道示例:")
    print("-" * 40)
    
    # 第一步：生成写作计划
    prompt_1 = """你是一个内容策划师。为一篇关于"AI在医疗中的应用"的文章生成一个详细的大纲。
    包括：导言、主要部分（最少3个）、结论。"""
    
    outline = create_message(prompt_1)
    print(f"步骤1 - 生成大纲:\n{outline}\n")
    
    # 第二步：基于大纲生成初稿
    prompt_2 = f"""基于以下大纲，写一篇关于AI在医疗中应用的初稿文章（300-400字）。
    
    大纲：
    {outline}
    
    请用通俗易懂的语言编写。"""
    
    draft = create_message(prompt_2)
    print(f"步骤2 - 生成初稿:\n{draft}\n")
    
    # 第三步：编辑和改进
    prompt_3 = f"""作为编辑，请改进以下文章。提高清晰度、流畅性和专业性。
    并指出任何需要改进的地方。
    
    原文：
    {draft}"""
    
    final = create_message(prompt_3)
    print(f"步骤3 - 编辑改进:\n{final}\n")


def example_data_processing_pipeline():
    """
    数据处理管道：提取 -> 清理 -> 分析
    """
    print("数据处理管道示例:")
    print("-" * 40)
    
    raw_data = """用户反馈数据：
    - "这个app很好用！！！" - 时间：2024-01-15
    - "速度太慢，经常崩溃" - 2024-01-16
    - "功能很丰富，值得推荐" - 2024-01-17"""
    
    # 第一步：提取关键信息
    prompt_1 = f"""从以下用户反馈中提取结构化数据。
    格式：日期、用户评价、情感倾向
    
    原始数据：
    {raw_data}"""
    
    extracted = create_message(prompt_1)
    print(f"步骤1 - 提取数据:\n{extracted}\n")
    
    # 第二步：数据清理
    prompt_2 = f"""清理以下数据并规范化格式。移除多余的符号和表情。
    
    原始提取数据：
    {extracted}"""
    
    cleaned = create_message(prompt_2)
    print(f"步骤2 - 清理数据:\n{cleaned}\n")
    
    # 第三步：分析结果
    prompt_3 = f"""基于清理后的数据进行分析。总结用户的主要看法。
    
    清理后的数据：
    {cleaned}"""
    
    analysis = create_message(prompt_3)
    print(f"步骤3 - 分析结果:\n{analysis}\n")


def example_code_generation_pipeline():
    """
    代码生成管道：需求 -> 设计 -> 实现 -> 测试
    """
    print("代码生成管道示例:")
    print("-" * 40)
    
    requirement = "创建一个用户认证系统"
    
    # 第一步：生成设计
    prompt_1 = f"""作为系统设计师，为以下需求提供技术设计方案：
    需求：{requirement}
    
    包括：架构、使用的技术栈、主要模块"""
    
    design = create_message(prompt_1)
    print(f"步骤1 - 生成设计:\n{design}\n")
    
    # 第二步：生成实现代码
    prompt_2 = f"""基于以下设计，用Python生成核心代码。
    
    设计方案：
    {design}"""
    
    code = create_message(prompt_2)
    print(f"步骤2 - 生成代码:\n{code}\n")
    
    # 第三步：生成测试用例
    prompt_3 = f"""为以下代码编写单元测试用例。
    
    代码：
    {code}"""
    
    tests = create_message(prompt_3)
    print(f"步骤3 - 生成测试:\n{tests}\n")


def example_translation_and_localization():
    """
    翻译和本地化管道：翻译 -> 检查 -> 本地化
    """
    print("翻译本地化管道示例:")
    print("-" * 40)
    
    english_text = "Hello, welcome to our service. We provide the best AI solutions."
    
    # 第一步：翻译
    prompt_1 = f"""将以下英文文本翻译成中文：
    {english_text}"""
    
    translated = create_message(prompt_1)
    print(f"步骤1 - 翻译:\n{translated}\n")
    
    # 第二步：检查翻译质量
    prompt_2 = f"""检查以下翻译的准确性和自然性。如有改进建议，请指出。
    原文：{english_text}
    翻译：{translated}"""
    
    review = create_message(prompt_2)
    print(f"步骤2 - 翻译审查:\n{review}\n")
    
    # 第三步：本地化
    prompt_3 = f"""基于以下翻译，进行本地化以适应中文用户习惯。
    调整文案、表达方式等。
    
    翻译文本：{translated}"""
    
    localized = create_message(prompt_3)
    print(f"步骤3 - 本地化:\n{localized}\n")


def main():
    """
    运行所有提示词链接示例
    """
    print("=" * 60)
    print("提示词链接示例")
    print("=" * 60)
    print()
    
    example_writing_pipeline()
    print()
    example_data_processing_pipeline()
    print()
    example_code_generation_pipeline()
    print()
    example_translation_and_localization()


if __name__ == "__main__":
    main()
