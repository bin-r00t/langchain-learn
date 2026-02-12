from dotenv import load_dotenv
import os

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI 
from langchain_tavily import TavilySearch

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
tavily_api_key = os.environ.get("TAVILY_API_KEY")

print("Hello from langchain-udemy!")
print(f"API Key loaded: {api_key is not None}")
print(f"Tavily API Key loaded: {tavily_api_key is not None}")

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", base_url='https://openrouter.ai/api/v1/chat/completions') #<=== NOT working...
react_prompt = hub.pull('hwchase17/react')
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)
agent_executor= AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor  


def main():
    result = chain.invoke(
        input={"input": "search for 3 job posting for an engineer using langchain in Hangzhou, zhejiang on zhipin.com and list their details"}
    )
    print(result)

if __name__ == "__main__":
    main()
