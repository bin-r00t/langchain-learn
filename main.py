from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-udemy!")
    api_key = os.environ.get("OPENAI_API_KEY")
    print(f"API Key loaded: {api_key is not None}")

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
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(
    #     temperature=0,
    #     model="gemma3:4b",
    #     base_url="https://api.deepseek.com",
    #     # api_key=api_key
    # )

    # usually, the above line of code would work, but we deployed our ollama server on a different host
    # llm = ChatOllama(temperature=0, model="gemma3:4b")

    # so, we need to specify the base_url
    llm = ChatOllama(
        temperature=0,
        model="gemma3:4b",
        base_url="http://192.168.31.131:11434"
    )

    # LCEL: langchain expression language (pipe)
    # returns a RUNNABLE chain, which can be invoked
    chain = summary_prompt_template | llm

    # invoke
    response = chain.invoke(input={"information": information})

    print(response.content)


if __name__ == "__main__":
    main()



# Ollama's response: (gemma3:4b) are as follows:
# To be honest, the answer is almost bullshit.
#
# Okay, here’s a short summary and two interesting facts about Elon Musk, based on the information provided:
# **1. Short Summary:**
# Elon Musk is a hugely influential and wealthy American entrepreneur. He’s best known for founding PayPal, SpaceX, Tesla, and acquiring Twitter (now X). He’s also had a brief stint as a government advisor under Donald Trump. As of 2025, he holds the title of world’s richest person with a net worth of $393 billion.
# **2. Two Interesting Facts:**
# *   **DOGE Involvement:** Despite his current focus on X, Musk was briefly involved in promoting and leading the "Department of Government Efficiency" (DOGE) during Donald Trump’s administration – a project centered around the cryptocurrency Dogecoin.
# *   **Early Space Obsession:** Musk’s fascination with space travel began in childhood, and he famously built and sold his first rockets as a teenager.