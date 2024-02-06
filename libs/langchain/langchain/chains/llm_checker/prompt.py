# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

_CREATE_DRAFT_ANSWER_TEMPLATE = """{question}\n\n"""
CREATE_DRAFT_ANSWER_PROMPT = PromptTemplate(
    input_variables=["question"], template=_CREATE_DRAFT_ANSWER_TEMPLATE
)

_LIST_ASSERTIONS_TEMPLATE = """Here is a statement:
{statement}
Make a bullet point list of the assumptions you made when producing the above statement.\n\n"""
LIST_ASSERTIONS_PROMPT = PromptTemplate(
    input_variables=["statement"], template=_LIST_ASSERTIONS_TEMPLATE
)

_CHECK_ASSERTIONS_TEMPLATE = """Here is a bullet point list of assertions:
{assertions}
For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""
CHECK_ASSERTIONS_PROMPT = PromptTemplate(
    input_variables=["assertions"], template=_CHECK_ASSERTIONS_TEMPLATE
)

_REVISED_ANSWER_TEMPLATE = """{checked_assertions}

Question: In light of the above assertions and checks, how would you answer the question '{question}'?

Answer:"""

# _REVISED_ANSWER_TEMPLATE中文注释
_REVISED_ANSWER_TEMPLATE_CN = """{checked_assertions}
问题：在上述断言和检查的基础上，您将如何回答“{question}”这个问题？
答案："""

REVISED_ANSWER_PROMPT = PromptTemplate(
    input_variables=["checked_assertions", "question"],
    template=_REVISED_ANSWER_TEMPLATE,
)
