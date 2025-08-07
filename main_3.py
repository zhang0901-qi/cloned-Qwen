import streamlit as st
from streamlit import sidebar
from langchain.memory import ConversationBufferMemory
from utils_3 import get_chat_response

st.title("克隆Tongyi")

with sidebar:
    qwen_api_key = st.text_input("请输入Tongyi API KEY：", type="password")
    st.markdown("[获取Tongyi API KEY](https://www.aliyun.com/product/pai)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"ai" , "content":"我是你的ai小助手，有啥可以帮你的嘛？" }]
#检查session_state中是否存在memory，如果不存在则初始化。
#同时初始化消息列表，开始时包含一条AI助手的问候语。

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])
#遍历session_state.messages中的每条消息，并将其显示在界面上。
prompt = st.chat_input()
if prompt:
    if not qwen_api_key:
        st.info("请输入你的Tongyi API KEY")
        st.stop
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)#将用户的输入添加到消息列表中，并显示在界面上。

    with st.spinner("ai正在思考，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"], qwen_api_key)
    msg = {"role":"ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
    #调用get_chat_response函数获取AI的回复，并将其添加到消息列表中。
#最后，在界面上显示AI的回复。