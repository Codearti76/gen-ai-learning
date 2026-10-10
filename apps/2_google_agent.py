from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent


llm=ChatGroq(model="openai/gpt-oss-20b")
search=GoogleSerperAPIWrapper()


agent=create_agent(
    model=llm,
    tools=[search.run],
    system_prompt="You are a agent  and can search for any question on google."
)

while True:
    query=input("User: ")
    if query.lower() in ["quit", "bye", "exit"]:
        print("Good Bye ")
        break
    response=agent.invoke({"messages":[{"role":"user", "content":query}]})
    print("AI: ", response["messages"][-1].content)
