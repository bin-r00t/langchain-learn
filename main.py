
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    print("Hello from langchain-udemy!")
    print(os.environ.get("OPEN_API_KEY"))


if __name__ == "__main__":
    main()
