def raise_on_import() -> None:
    """Raise an error on import since is deprecated."""
    # 产生一个错误，提示用户该模块已经被移动到langchain-experimental
    raise ImportError(
        "This module has been moved to langchain-experimental. "
        "For more details: https://github.com/langchain-ai/langchain/discussions/11352."
        "To access this code, install it with `pip install langchain-experimental`."
        "`from langchain_experimental.llm_bash.base "
        "import LLMBashChain`"
    )


raise_on_import()
