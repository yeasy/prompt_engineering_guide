"""
03_chain_of_thought.py - 思维链提示词示例

演示如何使用思维链推理来解决复杂的多步骤问题。
"""

from shims.anthropic_sdk import create_message


def example_math_reasoning():
    """
    数学问题求解的思维链推理
    """
    prompt = """请通过步骤来解决这个数学问题。首先思考，然后得出答案。

问题: 一个农场有一些鸡和兔子。总共有25个头和70条腿。
请问农场里有多少只鸡和多少只兔子？

让我们逐步思考："""
    
    response = create_message(prompt)
    print("数学问题思维链推理:")
    print(f"结果:\n{response}\n")


def example_logic_reasoning():
    """
    逻辑推理的思维链
    """
    prompt = """请通过逻辑推理来回答这个问题。

问题: 
- 所有的鸟都有羽毛
- 所有有羽毛的东西都会飞
- 鸡是一只鸟
- 问题：鸡会飞吗？

首先，让我们理解我们知道的事实...
然后，我们可以推理出...
最后，我们的结论是...
"""
    
    response = create_message(prompt)
    print("逻辑推理思维链:")
    print(f"结果:\n{response}\n")


def example_planning_reasoning():
    """
    项目规划的思维链推理
    """
    prompt = """帮助规划一个产品发布策略。请先分解问题，然后制定计划。

问题: 我们需要在2周内发布一个新的手机应用。

让我们分步思考：
1. 首先，我应该识别所有关键的任务...
2. 然后，我应该考虑任务的优先级...
3. 接下来，我应该分配时间...
4. 最后，我应该识别潜在的风险...

请提供一个详细的发布计划。"""
    
    response = create_message(prompt)
    print("项目规划思维链:")
    print(f"结果:\n{response}\n")


def example_decision_making():
    """
    决策制定的思维链推理
    """
    prompt = """帮助分析这个决策问题。使用思维链方法。

背景: 一家科技公司需要决定是否进入一个新市场（如AI芯片市场）。

让我们逐步分析：
1. 首先，列出所有相关的因素...
2. 其次，评估每个因素的重要性...
3. 然后，考虑可能的结果...
4. 最后，权衡利弊...

请提供一个平衡的分析。"""
    
    response = create_message(prompt)
    print("决策制定思维链:")
    print(f"结果:\n{response}\n")


def example_text_analysis():
    """
    文本分析的思维链推理
    """
    prompt = """分析这段文字，使用思维链方法来理解其含义。

文本: "人工智能的发展就像一场长跑，不是冲刺。快速的进步固然令人兴奋，
但持久的、思虑周密的进步才是真正改变世界的力量。"

让我们逐步分析：
1. 首先，识别主要的比喻...
2. 其次，理解比喻的含义...
3. 然后，识别隐含的论点...
4. 最后，总结整体的观点..."""
    
    response = create_message(prompt)
    print("文本分析思维链:")
    print(f"结果:\n{response}\n")


def main():
    """
    运行所有思维链示例
    """
    print("=" * 60)
    print("思维链推理示例")
    print("=" * 60)
    print()
    
    example_math_reasoning()
    example_logic_reasoning()
    example_planning_reasoning()
    example_decision_making()
    example_text_analysis()


if __name__ == "__main__":
    main()
