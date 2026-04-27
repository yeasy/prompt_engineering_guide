## 附录G：MCP 与提示词工程的融合

### G.1 MCP时代的提示词工程范式转变

从2024年起，Anthropic推出的MCP（Model Context Protocol）正在改变我们设计和使用提示词的方式。这不仅是一个新的API规范，更代表了从“静态文本提示”到“动态协议化上下文注入”的范式演进。

#### 传统提示词工程 vs MCP时代的上下文工程

```text
传统方式（2023年及之前）:
  手动拼接 → 静态提示词文本 → 发送给模型
  问题：
  - 信息通过字符串硬编码
  - 难以动态更新和管理
  - 每次都要重新拼接，低效且容易出错
  - 无法实时注入新数据

MCP方式（2024年及之后）:
  协议化注入 → 动态上下文源 → 标准化接口 → 发送给模型
  优势：
  - 通过协议标准化上下文的提供方式
  - 支持实时、动态的信息注入
  - 模型可以请求访问所需信息，宿主应用按权限和用户策略决定是否提供
  - 清晰的权限和隔离机制
```

### G.2 MCP的三大核心原语与提示词工程

MCP定义了三个核心概念，直接影响现代提示词设计：

#### 1. Resources（资源）- 数据的声明式描述

**原语定义**：Resources允许客户端发现和读取服务器提供的数据。

**对提示词工程的影响**：

传统方式：
```text
系统: "你可以访问以下数据库...
数据库结构是...
表包含的字段有...
[重复冗长的描述]"

问题：占用大量token，且难以维护
```

MCP方式：
```json
{
  "resources": [
    {
      "uri": "file:///customer_db",
      "name": "Customer Database",
      "description": "企业客户关系管理数据库"
    },
    {
      "uri": "file:///product_catalog",
      "name": "Product Catalog",
      "description": "实时产品目录和库存信息"
    }
  ]
}
```

提示词只需简洁地说：
```text
你可以访问以下资源：
- Customer Database (file:///customer_db)
- Product Catalog (file:///product_catalog)

使用file:// URI查询这些资源获取所需数据。
```

**优势**：
- Token消耗减少50%+
- 资源描述在服务器端管理，易于更新
- 模型可以自主决定何时查询哪个资源

#### 2. Tools（工具）- 可执行操作的标准化

**原语定义**：Tools允许模型请求执行特定操作。

**对提示词工程的影响**：

传统方式（ReAct）：
```text
你可以使用以下工具：
1. send_email(recipient, subject, body)
2. query_database(sql)
3. update_record(table, id, data)

[冗长的使用说明和示例]
```

MCP方式：
```json
{
  "tools": [
    {
      "name": "send_email",
      "description": "发送电子邮件",
      "inputSchema": {
        "type": "object",
        "properties": {
          "recipient": {"type": "string", "description": "收件人邮箱"},
          "subject": {"type": "string"},
          "body": {"type": "string"}
        },
        "required": ["recipient", "subject", "body"]
      }
    }
  ]
}
```

提示词可以更简洁：
```text
当需要发送电子邮件时，使用send_email工具。
格式和参数由MCP协议定义。
```

**优势**：
- 工具定义与提示词分离
- 模型自动理解工具的签名和约束
- 减少提示词中关于“如何使用工具”的冗余文本

#### 3. Prompts（提示模板）- 可复用的提示词模板库

**原语定义**：Prompts是可复用的提示词模板，由服务器管理。

**对提示词工程的影响**：

传统方式：
```text
每个应用都维护自己的提示词：
- 代码审查应用有一套提示词
- 文档生成应用有另一套
- 内容分类应用又有一套
→ 大量重复、难以版本管理、难以共享最佳实践
```

MCP方式：
```text
MCP服务器提供标准化的提示词模板：

{
  "prompts": [
    {
      "name": "code_review",
      "description": "代码审查提示模板",
      "arguments": [
        {"name": "language", "description": "编程语言"},
        {"name": "focus", "description": "审查重点"}
      ]
    },
    {
      "name": "document_summarization",
      "description": "文档总结提示模板",
      "arguments": [{"name": "style", "description": "摘要风格"}]
    }
  ]
}
```

应用调用：
```text
// 而不是手动构建提示词
const prompt = await mcp.getPrompt("code_review", {
  language: "python",
  focus: "security"
});
```

**优势**：
- 提示词成为可共享的资产
- 版本控制和最佳实践积累
- 跨组织、跨项目的一致性

### G.3 MCP改变的提示词设计原则

#### 原则1：从“包含所有信息”到“按需获取”

**传统方式**：
```text
系统提示词 =
  角色定义 +
  完整的背景信息 +
  所有可能的规则 +
  工具说明 +
  示例

→ 巨大且笨重的提示词
```

**MCP方式**：
```text
系统提示词 =
  核心角色定义 +
  对可用资源和工具的引用（简洁的声明）

当应用暴露资源时 → 模型可请求读取，宿主按权限决定是否提供
当应用暴露工具时 → 模型可请求调用，宿主/用户按策略授权执行
当需要特定指导时 → 应用可检索特定的 Prompt 模板

→ 精简且高效的核心提示词
```

#### 原则2：从“静态管理”到“动态协商”

**传统方式**：
```text
提示词是静态的：
- 写好后就不变了
- 或者需要手动重新构建
- 版本管理困难
- 扩展困难
```

**MCP方式**：
```text
提示词组件由协议动态提供：
- 资源列表可以实时更新
- 工具定义服务器端维护
- 模型可以在运行时发现新的能力
- 支持条件化的信息注入
```

#### 原则3：从“模型中心”到“上下文中心”

**提示词工程的演进**：
```text
阶段1：模型中心 (2020-2022)
  "我需要写一个很好的提示词来指导模型"
  重点：优化文本本身

阶段2：链式思维 (2022-2023)
  "通过结构化推理改进模型输出"
  重点：提示词结构

阶段3：上下文中心 (2024+)
  "如何设计最优的上下文环境让模型自主发现答案"
  重点：上下文来源和动态组装
```

### G.4 MCP时代的最佳实践

#### 实践1：最小化系统提示词

**示例**：

```text

# 旧方式（包含所有细节，超过5000 tokens）

你是一个专业的数据分析师...
你可以访问以下数据库...
数据库模式包括...
支持的查询类型有...
请遵循这些格式规范...
[等等冗长内容]

# MCP方式（核心提示词，仅500 tokens）

你是一个数据分析助手。

可用资源：
- 客户数据库 (db://customers)
- 销售数据库 (db://sales)
- 产品目录 (resource://products)

可用工具：
- query_database - 执行SQL查询
- generate_report - 生成分析报告

需要任何数据或执行特定操作时，使用上述资源和工具。
```

#### 实践2：利用Prompts模板库

**组织中的提示词管理**：

```text
企业级MCP服务器上的提示词库：

prompts/
  ├─ business_analysis/
  │  ├─ competitor_analysis.json
  │  ├─ market_sizing.json
  │  └─ trend_analysis.json
  ├─ technical/
  │  ├─ code_review.json
  │  ├─ architecture_review.json
  │  └─ testing_strategy.json
  └─ content/
     ├─ blog_post_outline.json
     ├─ social_media.json
     └─ product_documentation.json
```

应用使用：
```python

# 而不是在每个应用中重复提示词

class AnalysisAgent:
    async def analyze_competitor(self, company_name):
        # 从MCP服务器获取最新的提示模板
        prompt_template = await mcp.getPrompt(
            "competitor_analysis",
            {"company": company_name}
        )
        result = await claude.process(prompt_template)
        return result
```

#### 实践3：条件化的上下文注入

**根据用户查询动态选择资源**：

```python
class SmartContextBuilder:
    async def build_context(self, user_query):
        context_parts = []

        # 核心系统提示词（总是包含）
        context_parts.append(self.base_system_prompt)

        # 通过MCP动态发现相关资源
        if "客户" in user_query or "订单" in user_query:
            customer_resource = await mcp.getResource("db://customers")
            context_parts.append(f"相关资源：{customer_resource}")

        if "产品" in user_query:
            product_resource = await mcp.getResource("resource://products")
            context_parts.append(f"相关资源：{product_resource}")

        # 根据查询复杂度选择合适的工具集合
        if self.is_complex_query(user_query):
            tools = await mcp.discoverTools(category="advanced")
        else:
            tools = await mcp.discoverTools(category="basic")

        context_parts.append(f"可用工具：{tools}")

        return "\n\n".join(context_parts)
```

#### 实践4：MCP驱动的Agent设计

**新的Agent架构**：

```text
用户输入
  ↓
[感知阶段]
  ├─ 通过MCP的Prompts获取"任务理解"模板
  ├─ 通过MCP的Resources发现相关数据源
  └─ 通过MCP的Tools列表确定可用操作
  ↓
[规划阶段]
  ├─ 根据发现的资源制定计划
  └─ 确定需要调用的工具序列
  ↓
[执行阶段]
  ├─ 调用MCP工具执行每个步骤
  ├─ 实时查询MCP资源获取所需数据
  └─ 根据反馈调整计划
  ↓
[响应阶段]
  └─ 通过MCP的Prompt模板格式化输出
```

### G.5 MCP与成本优化

#### Token消耗的改善

```text
传统提示词工程：
  系统提示词: 2000 tokens
  工具定义: 1500 tokens
  示例: 1000 tokens
  当前会话: 500 tokens
  ─────────────────
  总计: 5000 tokens/请求

MCP方式：
  系统提示词: 300 tokens
  资源/工具引用: 100 tokens (仅名称和URI)
  当前会话: 500 tokens
  ─────────────────
  总计: 900 tokens/请求

节省: 82%
```

#### Prompt Caching与MCP的协同

```text
MCP + Prompt Caching的最佳实践：

1. 缓存基础系统提示词（300 tokens）
   - 这部分几乎不变
   - 缓存命中率99%+

2. 动态注入资源和工具引用
   - 通过MCP在缓存边界之外
   - 每次查询可能不同
   - 无需重新缓存

3. 结果：
   - 缓存节省基础成本
   - MCP动态适应每个查询
   - 组合优化效果显著
```

### G.6 企业级MCP部署示例

```python

# 企业的MCP服务器配置示例

class EnterpriseMCPServer:
    def __init__(self):
        self.resources = []
        self.tools = []
        self.prompts = []

    def setup_resources(self):
        """注册企业数据源"""
        self.resources.extend([
            {
                "uri": "db://salesforce",
                "name": "Sales Database",
                "auth": "oauth2",
                "read_only": False
            },
            {
                "uri": "db://jira",
                "name": "Project Management",
                "auth": "api_key",
                "read_only": True
            },
            {
                "uri": "file://company_docs",
                "name": "Company Knowledge Base",
                "auth": "none",
                "read_only": True
            }
        ])

    def setup_tools(self):
        """注册企业工具"""
        self.tools.extend([
            {
                "name": "create_ticket",
                "description": "在Jira中创建工作单",
                "requires_auth": True,
                "rate_limit": "100/hour"
            },
            {
                "name": "update_sales_record",
                "description": "更新Salesforce销售记录",
                "requires_auth": True,
                "rate_limit": "1000/hour"
            }
        ])

    def setup_prompts(self):
        """注册标准化提示模板库"""
        self.prompts.extend([
            {
                "name": "sales_analysis",
                "version": "2.1",
                "maintained_by": "sales_team",
                "last_updated": "2024-03-01"
            },
            {
                "name": "technical_design_review",
                "version": "1.5",
                "maintained_by": "engineering_team",
                "last_updated": "2024-02-28"
            }
        ])
```

### G.7 MCP时代的安全性考量

#### 权限管理通过MCP实现

```text
传统方式：
  在提示词中说明权限 → 容易被注入攻击绕过

MCP方式：
  权限由服务器端强制执行
  ├─ 某个角色只能查询读权限的资源
  ├─ 某个工具需要额外的授权
  ├─ 敏感操作需要审计日志
  └─ 提示词中不需要重复说明权限

→ 安全性由架构保证，而非提示词技巧
```

### G.8 小结：MCP带来的范式转变

```text
维度           传统方式              MCP方式
────────────────────────────────────────────────
上下文来源     手动拼接文本          协议化声明
信息更新       需要重写提示词        服务器端更新
工具调用       详细的使用说明        标准化JSON
权限管理       在提示词中描述        服务器端强制
可扩展性       每新增能力都修改提示词  自动发现
Token消耗      5000-8000/请求        800-1200/请求
版本管理       困难                  标准化
────────────────────────────────────────────────

核心转变：
从 "精心设计单一提示词"
到 "设计最优的上下文环境"
```

### G.9 学习资源

- [官方 MCP 规范](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- Anthropic的MCP最佳实践指南
- 社区驱动的MCP服务器集合

### 思考题

1. 在你的当前项目中，如果采用MCP方式，提示词能减少多少token？
2. 你如何设计一个企业级MCP服务器来统一管理提示词模板？
3. MCP与Prompt Caching结合时，如何设计缓存边界以最大化成本节省？
