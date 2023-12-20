from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler
import os
import streamlit as st

OPENAI_API_KEY = os.environ.get("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")

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0, streaming=True)
tools = load_tools(["llm-math","ddg-search"], llm=llm)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(prompt, callbacks=[st_callback])
        st.write(response)
