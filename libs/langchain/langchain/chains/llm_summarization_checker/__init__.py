"""Summarization checker chain for verifying accuracy of text generation.

Chain that tries to verify the accuracy of text generation by splitting it into a
list of facts, then checking if those facts are true or not, and rewriting
the text to make it more truth-ful.  It will repeat this loop until it hits `max_tries`
or gets to a "true" output.
"""

# 总结检查链以验证文本生成的准确性。
# 链尝试通过将其拆分为事实列表来验证文本生成的准确性，然后检查这些事实是否为真，并重写文本以使其更真实。
# 它将重复此循环，直到达到`max_tries`或达到“真”输出。