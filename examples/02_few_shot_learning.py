"""
02_few_shot_learning.py - 少样本学习示例

演示如何通过提供少数示例来引导模型学习特定的模式或风格。
"""

from shims.anthropic_sdk import create_message


def example_sentiment_analysis():
    """
    情感分析的少样本学习
    """
    prompt = """你的任务是分析文本的情感，输出"正面"、"负面"或"中性"。

示例：
文本: "这个产品非常好用，我很满意！"
情感: 正面

文本: "非常失望，产品质量很差。"
情感: 负面

文本: "这是一个新产品。"
情感: 中性

现在分析以下文本的情感：
文本: "这个服务很快，价格也合理，值得推荐。"
情感:"""
    
    response = create_message(prompt)
    print("情感分析少样本学习:")
    print(f"结果: {response}\n")


def example_translation():
    """
    翻译任务的少样本学习
    """
    prompt = """翻译以下文本从中文到英文。示例如下：

中文: "你好吗？"
英文: "How are you?"

中文: "今天天气很好。"
英文: "The weather is nice today."

中文: "我想学习编程。"
英文: "I want to learn programming."

现在翻译这个：
中文: "提示词工程是一个新兴的领域。"
英文:"""
    
    response = create_message(prompt)
    print("翻译少样本学习:")
    print(f"结果: {response}\n")


def example_code_generation():
    """
    代码生成的少样本学习
    """
    prompt = '''你是一个Python代码生成助手。根据描述生成相应的Python代码。

描述: 创建一个函数，计算列表中所有数字的平均值
代码:
```python
def calculate_average(numbers):
    """计算列表中数字的平均值"""
    return sum(numbers) / len(numbers)
```

描述: 创建一个函数，检查一个数字是否是质数
代码:
```python
def is_prime(n):
    """检查n是否是质数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

描述: 创建一个函数，将列表中的字符串转换为大写
代码:'''
    
    response = create_message(prompt)
    print("代码生成少样本学习:")
    print(f"结果:\n{response}\n")


def example_entity_extraction():
    """
    实体抽取的少样本学习
    """
    prompt = """从文本中提取人名、地点和组织名称。

文本: "张三在北京的微软公司工作。"
提取结果:
- 人名: 张三
- 地点: 北京
- 组织: 微软公司

文本: "李四是上海复旦大学的教授。"
提取结果:
- 人名: 李四
- 地点: 上海
- 组织: 复旦大学

文本: "王五在深圳的腾讯技术有限公司担任工程师。"
提取结果:"""
    
    response = create_message(prompt)
    print("实体抽取少样本学习:")
    print(f"结果:\n{response}\n")


def main():
    """
    运行所有少样本学习示例
    """
    print("=" * 60)
    print("少样本学习示例")
    print("=" * 60)
    print()
    
    example_sentiment_analysis()
    example_translation()
    example_code_generation()
    example_entity_extraction()


if __name__ == "__main__":
    main()
