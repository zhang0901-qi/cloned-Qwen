from langchain_community.chat_models import ChatTongyi
#from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
#from langchain_core.runnables.history import RunnableWithMessageHistory
#from langchain.memory import ChatMessageHistory
from langchain.chains import ConversationChain# 导入对话链工具，用于管理对话流程
from langchain.memory import ConversationBufferMemory# 导入对话记忆存储工具
import os
def get_chat_response(prompt, memory, qwen_api_key):
    model = ChatTongyi(model = "qwen-turbo", api_key = qwen_api_key)
    chain = ConversationChain(llm=model, memory=memory)# 创建对话链：组合模型+记忆系统
    response = chain.invoke({"input":prompt})#发送用户输入并获取AI回复，调用对话链处理用户输入并返回响应。
    return response["response"]

memory = ConversationBufferMemory(return_messages=True)
#创建一个对话缓冲区，用于保存对话的历史信息，以便在后续对话中使用。
#print(get_chat_response("光与夜之恋中齐司礼比较出名的话是什么，列出三句即可", memory, os.getenv("DASHSCOPE_API_KEY")))
#print(get_chat_response("再列出一句吧", memory, os.getenv("DASHSCOPE_API_KEY")))


