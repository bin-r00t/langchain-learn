
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

def main():
    print("Hello from langchain-udemy!")
    print(os.environ.get("OPEN_API_KEY"))

    # provide the material to summarize
    information = """Elon Musk (born June 28, 1971, Pretoria, South Africa) is a South African–born American entrepreneur who cofounded the electronic payment firm PayPal and formed SpaceX, maker of launch vehicles and spacecraft. He was also one of the first significant investors in, as well as chief executive officer of, the electric car manufacturer Tesla. In addition, Musk acquired Twitter (later X) in 2022. Musk led the Department of Government Efficiency (DOGE) in U.S. President Donald Trump’s second administration for four months before stepping down in May 2025. Musk is the world’s richest person, with a net worth of $393 billion, as of 2025."""
    
    # we do not use format string here: (think about format string's downsites)
    summary_template = """
    given then information {information} about a person I want you to give me a short summary about him.
    1. A short summary.
    2. two interesting facts about him.
    """

    # create prompt
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="deepseek-chat", base_url="https://api.deepseek.com")

    # LCEL: langchain expression language (pipe)
    # returns a RUNNABLE chain, which can be invoked
    chain = summary_prompt_template | llm 

    # invoke
    response = chain.invoke(input={"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
