"""
05_rag_retrieval.py - 检索增强生成（RAG）示例

演示如何将外部知识库与语言模型结合，提高回答的准确性和可信度。
"""

from shims.anthropic_sdk import create_message


def example_document_qa():
    """
    基于文档的问答系统
    """
    print("基于文档的问答系统:")
    print("-" * 40)
    
    # 模拟知识库文档
    knowledge_base = """
    公司政策文档：
    
    远程工作政策：
    - 员工可以每周远程工作不超过3天
    - 必须在工作时间保持在线
    - 重要会议必须亲自参加
    
    假期政策：
    - 年假：20天
    - 病假：10天（需要医疗证明）
    - 法定假期：按国家规定
    """
    
    # 用户问题
    question = "我每周最多可以远程工作多少天？"
    
    prompt = f"""你是一个公司政策问答助手。基于以下知识库回答用户的问题。
    
    知识库：
    {knowledge_base}
    
    用户问题：{question}
    
    请仅基于知识库中的信息回答，如果知识库中没有相关信息，请说明。"""
    
    answer = create_message(prompt)
    print(f"问题：{question}")
    print(f"答案：{answer}\n")


def example_product_recommendation():
    """
    基于产品知识库的推荐系统
    """
    print("产品推荐系统:")
    print("-" * 40)
    
    # 产品知识库
    product_db = """
    我们的产品目录：
    
    产品A - AI助手Pro
    - 价格：¥99/月
    - 功能：文本生成、翻译、编程辅助
    - 适合：专业人士和开发者
    
    产品B - AI学习伙伴
    - 价格：¥49/月
    - 功能：解题、学习辅导、知识讲解
    - 适合：学生和学习者
    
    产品C - AI办公助手
    - 价格：¥69/月
    - 功能：文档生成、数据分析、邮件写作
    - 适合：办公工作者
    """
    
    customer_profile = "我是一个高中学生，需要帮助完成作业和理解难题"
    
    prompt = f"""你是产品推荐顾问。基于以下产品信息和客户需求，推荐最合适的产品。
    
    产品库：
    {product_db}
    
    客户信息：{customer_profile}
    
    请说明为什么推荐这个产品。"""
    
    recommendation = create_message(prompt)
    print(f"客户需求：{customer_profile}")
    print(f"推荐：{recommendation}\n")


def example_technical_support():
    """
    技术支持问答系统
    """
    print("技术支持问答系统:")
    print("-" * 40)
    
    # 技术知识库
    tech_kb = """
    常见问题解答：
    
    问题：应用启动很慢
    解决方案：
    1. 清除应用缓存（设置 > 应用 > 清除缓存）
    2. 关闭后台运行的其他应用
    3. 如果仍然缓慢，尝试重新安装应用
    
    问题：无法登录
    解决方案：
    1. 检查网络连接
    2. 确保输入正确的用户名和密码
    3. 尝试重置密码
    4. 清除浏览器缓存和Cookies
    
    问题：数据同步失败
    解决方案：
    1. 检查网络连接状态
    2. 在设置中禁用再启用同步
    3. 检查账户空间是否足够
    4. 联系技术支持
    """
    
    user_issue = "我的应用每次打开都需要等待很长时间"
    
    prompt = f"""你是技术支持代表。基于以下知识库帮助用户解决问题。
    
    技术知识库：
    {tech_kb}
    
    用户问题：{user_issue}
    
    请提供清晰的步骤和解决方案。"""
    
    solution = create_message(prompt)
    print(f"用户问题：{user_issue}")
    print(f"解决方案：{solution}\n")


def example_research_assistant():
    """
    研究辅助系统
    """
    print("研究辅助系统:")
    print("-" * 40)
    
    # 研究资料
    research_materials = """
    气候变化研究摘要：
    
    全球变暖的影响：
    - 海平面上升：过去100年上升约17厘米
    - 冰川融化：格陵兰冰床每年融化约3600亿吨冰
    - 生物多样性：物种灭绝速率是自然速率的100-1000倍
    
    主要原因：
    - 温室气体排放（CO2, CH4, N2O）
    - 森林砍伐
    - 工业活动
    - 农业生产
    
    可能的解决方案：
    - 可再生能源转型
    - 森林保护和恢复
    - 碳捕获技术
    - 政策和国际合作
    """
    
    research_query = "气候变化对生物多样性的主要影响有哪些？"
    
    prompt = f"""你是一个研究助手。基于以下研究资料回答学术问题。
    
    研究资料：
    {research_materials}
    
    研究问题：{research_query}
    
    请用学术语言组织答案，并引用资料中的具体数据。"""
    
    research_answer = create_message(prompt)
    print(f"研究问题：{research_query}")
    print(f"答案：{research_answer}\n")


def main():
    """
    运行所有RAG示例
    """
    print("=" * 60)
    print("检索增强生成（RAG）示例")
    print("=" * 60)
    print()
    
    example_document_qa()
    example_product_recommendation()
    example_technical_support()
    example_research_assistant()


if __name__ == "__main__":
    main()
