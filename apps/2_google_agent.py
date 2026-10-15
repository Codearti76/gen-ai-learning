from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver


llm=ChatGroq(model="openai/gpt-oss-20b")
search=GoogleSerperAPIWrapper()
memory=MemorySaver()


agent=create_agent(
    model=llm,
    tools=[search.run],
    system_prompt="You are a agent  and can search for any question on google.",
    checkpointer=memory
)

while True:
    query=input("User: ")
    if query.lower() in ["quit", "bye", "exit"]:
        print("Good Bye ")
        break
    response=agent.invoke({"messages":[{"role":"user", "content":query}]},
                          {"configurable":{"thread_id": "12"}}
                          )
    print("AI: ", response["messages"][-1].content)
