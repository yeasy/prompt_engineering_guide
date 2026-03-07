"""
01_basic_prompting.py - 基础提示词示例

演示如何编写清晰、直接的提示词来与大语言模型交互。
"""

from shims.anthropic_sdk import create_message


def example_simple_question():
    """
    最简单的提示词：直接提问
    """
    prompt = "请解释什么是提示词工程？"
    
    response = create_message(prompt)
    print(f"问题: {prompt}")
    print(f"回答: {response}\n")


def example_with_instructions():
    """
    带有清晰指示的提示词
    """
    prompt = """你是一个数据分析专家。
    
    请按照以下步骤分析这个数据集：
    1. 描述数据的基本统计特征
    2. 识别任何明显的趋势或模式
    3. 提出两个可能的改进建议
    
    数据集: [2, 4, 6, 8, 10, 12, 15, 18, 22, 25]"""
    
    response = create_message(prompt)
    print(f"指示性提示词的回答:\n{response}\n")


def example_with_context():
    """
    提供背景信息的提示词
    """
    prompt = """背景: 我们开发一个电商推荐系统
    
    用户行为数据:
    - 用户A: 经常浏览电子产品
    - 用户B: 购买家居用品
    - 用户C: 关注书籍和教育内容
    
    任务: 为每个用户生成一个个性化的推荐语句"""
    
    response = create_message(prompt)
    print(f"带有上下文的提示词的回答:\n{response}\n")


def example_role_playing():
    """
    角色扮演提示词
    """
    prompt = """你是一个技术博客写手，专门为初学者解释复杂的编程概念。
    
    请用简单、有趣的方式解释"API"的概念，
    并给出一个日常生活中的类比。"""
    
    response = create_message(prompt)
    print(f"角色扮演提示词的回答:\n{response}\n")


def main():
    """
    运行所有基础提示词示例
    """
    print("=" * 60)
    print("基础提示词示例")
    print("=" * 60)
    print()
    
    example_simple_question()
    example_with_instructions()
    example_with_context()
    example_role_playing()


if __name__ == "__main__":
    main()
