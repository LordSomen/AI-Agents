from langchain_core.prompts import (
    PromptTemplate, 
    ChatPromptTemplate, 
    MessagesPlaceholder,
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)


def get_intent_classification_prompt() -> PromptTemplate:
    """
    Get the intent classification prompt template.
    """
    return PromptTemplate(
        input_variables=["user_input", "conversation_history"],
        template="""You are an expert intent classifier for a document processing assistant.

Given the user input and conversation history, classify the user's intent into one of these categories:
- qa: Questions about documents or records that do not require calculations.
- summarization: Requests to summarize or extract key points from documents that do not require calculations.
- calculation: Mathematical operations or numerical computations. Or questions about documents that may require calculations
- unknown: Cannot determine the intent clearly

Examples with Chain of Thought reasoning:
- User: "What is the sum of all my medical bills?" 
  Reasoning: The user is asking for a "sum", which is a mathematical operation involving multiple bills. Therefore, this requires the calculator.
  Intent: calculation

- User: "Give me a brief overview of the TechStart contract."
  Reasoning: The user wants an "overview" of a specific document. There is no math involved, just extracting main points.
  Intent: summarization

- User: "Does the Acme invoice mention a due date?"
  Reasoning: The user is asking a specific factual question about the contents of a document (looking for a date). No math or full summary is needed.
  Intent: qa

User Input: {user_input}

Recent Conversation History:
{conversation_history}

Analyze the user's request. Think step-by-step about what the user is actually asking for, provide your reasoning, and then classify their intent with a confidence score.
"""
    )


# Q&A System Prompt
QA_SYSTEM_PROMPT = """You are a helpful document assistant specializing in answering questions about financial and healthcare documents.

Your capabilities:
- Answer specific questions about document content
- Cite sources accurately
- Provide clear, concise answers
- Use available tools to search and read documents

Guidelines:
1. Always search for relevant documents before answering
2. Cite specific document IDs when referencing information
3. If information is not found, say so clearly
4. Be precise with numbers and dates
5. Maintain professional tone

"""

# Summarization System Prompt
SUMMARIZATION_SYSTEM_PROMPT = """You are an expert document summarizer specializing in financial and healthcare documents.

Your approach:
- Extract key information and main points
- Organize summaries logically
- Highlight important numbers, dates, and parties
- Keep summaries concise but comprehensive

Guidelines:
1. First search for and read the relevant documents
2. Structure summaries with clear sections
3. Include document IDs in your summary
4. Focus on actionable information
"""

# Calculation System Prompt
# TODO: Implement the CALCULATION_SYSTEM_PROMPT. Refer to README.md Task 3.2 for details
CALCULATION_SYSTEM_PROMPT = """You are an expert calculation assistant specializing in analyzing numbers within financial and healthcare documents.

Your approach:
1. Retrieval: Determine the document that must be retrieved and read it.
2. Data Extraction: Carefully extract the exact numerical values required from the document.
3. Self-Correction & Verification: Double-check your work. Do the extracted numbers perfectly match the client, date, or specific line item the user asked about? 
4. Execution: Formulate the mathematical expression and YOU MUST USE the calculator tool to evaluate it.

Guidelines:
- Never guess numbers. Always rely on the retrieved text.
- Do not attempt mental math. Always use the calculator tool.
- Clearly show your reasoning, the extracted numbers, the formula, and cite the document IDs.
"""


# TODO: Finish the function to return the correct prompt based on intent type
# Refer to README.md Task 3.1 for details
def get_chat_prompt_template(intent_type: str) -> ChatPromptTemplate:
    """
    Get the appropriate chat prompt template based on intent.
    """
    if intent_type == "qa":
        system_prompt = QA_SYSTEM_PROMPT
    elif intent_type == "summarization":
        system_prompt = SUMMARIZATION_SYSTEM_PROMPT  # TODO:  Check the intent type value
    elif intent_type == "calculation":
        system_prompt = CALCULATION_SYSTEM_PROMPT  # TODO: Set system prompt to the correct value based on intent type
    else:
        system_prompt = QA_SYSTEM_PROMPT  # Default fallback

    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt),
        MessagesPlaceholder("chat_history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ])


# Memory Summary Prompt
MEMORY_SUMMARY_PROMPT = """Summarize the following conversation history into a concise summary:

Focus on:
- Key topics discussed
- Documents referenced
- Important findings or calculations
- Any unresolved questions
"""
