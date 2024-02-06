from typing import Tuple

from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import PromptTemplate


class FinishedOutputParser(BaseOutputParser[Tuple[str, bool]]):
    """Output parser that checks if the output is finished."""
    # 输出解析器，检查输出是否完成。

    finished_value: str = "FINISHED"
    """Value that indicates the output is finished."""

    def parse(self, text: str) -> Tuple[str, bool]:
        cleaned = text.strip()
        finished = self.finished_value in cleaned
        return cleaned.replace(self.finished_value, ""), finished


PROMPT_TEMPLATE = """\
Respond to the user message using any relevant context. \
If context is provided, you should ground your answer in that context. \
Once you're done responding return FINISHED.

>>> CONTEXT: {context}
>>> USER INPUT: {user_input}
>>> RESPONSE: {response}\
"""

# # 翻译上述内容
# PROMPT_TEMPLATE_CN = """\
# 使用任何相关的上下文来回复用户消息。如果提供了上下文，您应该将您的答案放在该上下文中。一旦您完成回复，返回FINISHED。
# >>> 上下文: {context}
# >>> 用户输入: {user_input}
# >>> 回复: {response}\
# """

PROMPT = PromptTemplate(
    template=PROMPT_TEMPLATE,
    input_variables=["user_input", "context", "response"],
)


QUESTION_GENERATOR_PROMPT_TEMPLATE = """\
Given a user input and an existing partial response as context, \
ask a question to which the answer is the given term/entity/phrase:

>>> USER INPUT: {user_input}
>>> EXISTING PARTIAL RESPONSE: {current_response}

The question to which the answer is the term/entity/phrase "{uncertain_span}" is:"""

# # 翻译上述内容
# QUESTION_GENERATOR_PROMPT_TEMPLATE_CN = """\
# 给定用户输入和现有的部分响应作为上下文，提出一个问题，其答案是给定的术语/实体/短语:
# >>> 用户输入: {user_input}
# >>> 现有部分响应: {current_response}
# 问题的答案是术语/实体/短语 "{uncertain_span}" 是:"""

QUESTION_GENERATOR_PROMPT = PromptTemplate(
    template=QUESTION_GENERATOR_PROMPT_TEMPLATE,
    input_variables=["user_input", "current_response", "uncertain_span"],
)
