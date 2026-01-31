# LangChain Learning Project

A hands-on learning project for exploring LangChain, a powerful framework for developing applications powered by language models. This project demonstrates practical implementations using various LLM providers including OpenAI, DeepSeek, and Ollama.

## 🎯 Overview

This repository contains learning materials and practical examples for working with LangChain. The project focuses on understanding core LangChain concepts such as prompt templates, chain composition using LCEL (LangChain Expression Language), and integration with multiple LLM providers.

## ✨ Features

- **Multiple LLM Provider Support**: Integrated support for OpenAI, DeepSeek, and Ollama
- **LCEL Implementation**: Demonstrates LangChain Expression Language for chain composition
- **Prompt Engineering**: Examples of prompt templates and structured outputs
- **Local & Cloud LLMs**: Flexibility to run with both cloud-based and local language models
- **Environment Management**: Secure API key handling with python-dotenv
- **Development Tools**: Pre-configured with Black and isort for code formatting

## 📋 Prerequisites

- Python 3.12.12 or higher
- `uv` package manager (recommended) or `pip`
- API keys for cloud providers (optional):
  - OpenAI API key
  - DeepSeek API key
- Ollama installed locally (optional, for local LLM usage)

## 🚀 Installation

### 1. Install UV Package Manager

```bash
pip3 install uv
```

### 2. Clone the Repository

```bash
git clone https://github.com/bin-r00t/langchain-learn.git
cd langchain-learn
```

### 3. Initialize Project

```bash
# Initialize and install dependencies
uv init
uv add langchain langchain-openai langchain-ollama python-dotenv black isort
```

### 4. Activate Virtual Environment

```bash
chmod u+x .venv/bin/activate
source .venv/bin/activate
```

Your terminal prompt should now show `(langchain-udemy)` prefix.

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
# Add other API keys as needed
```

### Ollama Setup (Optional)

If using local LLMs with Ollama:

1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull a model: `ollama pull gemma3:4b`
3. For remote Ollama server, update the `base_url` in `main.py`

## 💻 Usage

### Basic Execution

Run the main script:

```bash
python main.py
```

### Example Code

The project includes a practical example that:
1. Loads environment variables
2. Creates a prompt template for summarization
3. Chains the prompt with an LLM using LCEL
4. Invokes the chain to generate structured output

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Create prompt template
summary_prompt_template = PromptTemplate(
    input_variables=["information"], 
    template=summary_template
)

# Initialize LLM
llm = ChatOpenAI(temperature=0, model="deepseek-chat")

# Create chain using LCEL (pipe operator)
chain = summary_prompt_template | llm

# Execute chain
response = chain.invoke(input={"information": information})
```

## 📁 Project Structure

```
langchain-learn/
├── main.py              # Main application with LangChain examples
├── pyproject.toml       # Project dependencies and metadata
├── uv.lock             # Locked dependencies
├── .env                # Environment variables (not in git)
├── .python-version     # Python version specification
├── notes/              # Learning notes and documentation
│   ├── 1.hello-world.md
│   ├── 2.local-version.md
│   ├── 3.temperature-settings.md
│   └── 4.update-python-to-3.12.md
└── README.md           # This file
```

## 📚 Learning Notes

The `notes/` directory contains detailed documentation on various topics:

- **Temperature Settings**: Understanding LLM temperature parameters (0.0 for consistency, 1.0 for creativity)
- **Local LLM Setup**: Using Ollama for local model deployment
- **Environment Setup**: Package management and virtual environment configuration
- **Message Formats**: LangChain message structure and role types

## 🔧 Development

### Code Formatting

The project uses Black and isort for code formatting:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .
```

## 🤝 Contributing

Contributions are welcome! This is a learning project, so feel free to:
- Add new examples
- Improve documentation
- Share learning notes
- Fix bugs or issues

## 📄 License

This is a personal learning project. Feel free to use and modify for your own learning purposes.

## 🙏 Acknowledgments

- Built while learning from Udemy courses on LangChain
- Uses the LangChain framework and ecosystem
- Examples adapted for multiple LLM providers

## 📞 Contact

For questions or discussions about this learning project, please open an issue in the repository.

---

**Happy Learning! 🚀**
