# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

_PROMPT_TEMPLATE = """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.

Question: ${{Question with math problem.}}
```text
${{single line mathematical expression that solves the problem}}
```
...numexpr.evaluate(text)...
```output
${{Output of running the code}}
```
Answer: ${{Answer}}

Begin.

Question: What is 37593 * 67?
```text
37593 * 67
```
...numexpr.evaluate("37593 * 67")...
```output
2518731
```
Answer: 2518731

Question: 37593^(1/5)
```text
37593**(1/5)
```
...numexpr.evaluate("37593**(1/5)")...
```output
8.222831614237718
```
Answer: 8.222831614237718

Question: {question}
"""

# 翻译上述_PROMPT_TEMPLATE为中文注释
_PROMPT_TEMPLATE_CN = """将数学问题翻译为可使用Python的numexpr库执行的表达式。使用运行此代码的输出来回答问题。

问题：${{带有数学问题的问题。}}
```text
${{单行数学表达式，用于解决问题}}
```
...numexpr.evaluate(text)...
```output
${{运行代码的输出}}
```
答案：${{答案}}

开始。

问题：37593 * 67是多少？
```text
37593 * 67
```
...numexpr.evaluate("37593 * 67")...
```output
2518731
```
答案：2518731

问题：37593^(1/5)
```text
37593**(1/5)
```
...numexpr.evaluate("37593**(1/5)")...
```output
8.222831614237718
```
答案：8.222831614237718

问题：{question}
"""

PROMPT = PromptTemplate(
    input_variables=["question"],  # 输入变量，即模板中的${{question}}
    template=_PROMPT_TEMPLATE,  # prompt模板
)
