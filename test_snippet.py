from openai import OpenAI
client = OpenAI()
messages = [{"role": "user", "content": "分析这款产品：智能手表"}]
class ProductAnalysis:
    pass
response = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=messages,
    response_format=ProductAnalysis
)
