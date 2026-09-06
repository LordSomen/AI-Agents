# AI Document Assistant

An intelligent document processing system built with LangChain and LangGraph. This multi-agent AI assistant can answer questions, summarize documents, and perform calculations on financial and healthcare documents using structured output routing and persistent memory.

## Project Overview

This document assistant uses a multi-agent architecture with LangGraph to handle different types of user requests:
- **Q&A Agent**: Answers specific questions about document content and cites sources.
- **Summarization Agent**: Creates structured summaries and extracts key points from documents.
- **Calculation Agent**: Safely evaluates mathematical operations on document data using a custom Python `eval` calculator tool.

It also leverages `InMemorySaver` to persist conversation history across user interactions and includes a memory summarization node to retain context efficiently.

## Getting Started

### Dependencies
- Python 3.9+
- OpenAI API Key
- See `starter/requirements.txt` for the full list of Python packages.

### Installation

1. Navigate to the project starter directory:
   ```bash
   cd starter
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Open .env and add your OpenAI API key
   ```

## Running the Assistant
You can launch the interactive CLI assistant by running:
```bash
python main.py
```

## Example Conversations

Here are examples of the three different intents in action:

### 1. Q&A Intent
**User:** What is the status of the claim filed by John Doe?
**Assistant:** According to Document CLM-001, the claim filed by John Doe is currently "Under Review".

### 2. Summarization Intent
**User:** Can you summarize the Acme Corporation document?
**Assistant:** Here is a summary of the Acme Corporation document (INV-001):
- **Client:** Acme Corporation
- **Date:** 2024-01-15
- **Type:** Invoice
- **Key Point:** The document is an invoice for Acme Corporation amounting to $22,000.

### 3. Calculation Intent
**User:** What is the total sum of the invoice for Acme Corporation and the invoice for TechStart Inc?
**Assistant:** 
- The Acme Corporation invoice (INV-001) is for $22,000.
- The TechStart Inc invoice (INV-002) is for $69,300.
- Using the calculator tool: 22000 + 69300 = 91300.
The total sum of both invoices is $91,300.

## Built With
* [LangChain](https://langchain.com/) - LLM Orchestration
* [LangGraph](https://langchain-ai.github.io/langgraph/) - Multi-agent graph routing
* [Pydantic](https://docs.pydantic.dev/) - Structured data validation
* [OpenAI](https://openai.com/) - LLM Models
