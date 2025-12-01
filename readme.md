# House Price Data Concierge Agent 🏡🤖

This repository collects all the material used to build a **Data Concierge Agent** for the classic **House Prices – Advanced Regression Techniques** dataset, as part of the **Google × Kaggle 5‑Day AI Agents Intensive**.  

The project notebook (`house-price-data-concierge-eda-on-autopilot-1.ipynb`) shows a production‑style agent that automates exploratory data analysis (EDA), data‑quality checks, and a quick baseline model for the housing price data, while the other notebooks and PDFs are the official course materials used as a reference for agents, tools, sessions, memory, observability, evaluation, and deployment. [attached_file:124]  

---

## 1. Project overview

Working with the housing price dataset typically starts with a lot of boilerplate: loading the CSV, inspecting 79+ features, diagnosing missing values, plotting distributions and correlations, and wiring up a baseline regressor for `SalePrice`.  

The **House Price Data Concierge Agent** turns that repetitive EDA workflow into a conversational experience inside a Kaggle Notebook:

- Loads the House Prices training data from Kaggle’s input directory.  
- Inspects schema, dtypes, cardinality, and missingness for all columns.  
- Generates EDA plots such as numeric distributions and correlation heatmaps.  
- Suggests a cleaning plan: what to drop, how to impute, and what to encode.  
- Trains a quick `scikit-learn` baseline model (Random Forest) and reports metrics like RMSE. [attached_file:124]  

All of this is orchestrated by an LLM‑powered agent built with Google’s **Agent Development Kit (ADK)**, following patterns from the 5‑day course notebooks.  

---

## 2. Repository structure

**Capstone project notebook**

- `house-price-data-concierge-eda-on-autopilot-1.ipynb`  
  - Main capstone implementation.  
  - Defines custom EDA tools, the `DataConciergeAgent`, an optional memory‑aware variant, and a small evaluation harness that runs scripted prompts. [attached_file:124]  

**Day 1 – Agent foundations & architectures**

- `day-1a-from-prompt-to-action.ipynb`  
  - Intro to building a single agent with tools and running it via an in‑memory runner.  
- `day-1b-agent-architectures.ipynb`  
  - Multi‑agent patterns (coordinator, sequential, parallel, loop) used as inspiration for the concierge architecture.  

**Day 2 – Tools & best practices**

- `day-2a-agent-tools.ipynb`  
  - How to turn Python functions into tools and use built‑in tools like search.  
- `day-2b-agent-tools-best-practices-1.ipynb`  
  - Tool design patterns (clear docstrings, type hints, structured returns) that are followed by the EDA tools in the capstone notebook.  

**Day 3 – Sessions, memory & context engineering**

- `day-3a-agent-sessions.ipynb`  
  - Managing sessions and runner services.  
- `day-3b-agent-memory.ipynb`  
  - Long‑term memory concepts, memory services, and callbacks.  
- `Context-Engineering_-Sessions-Memory.pdf`  
  - Additional background on how to design prompts and context windows for agents.  

**Day 4 – Observability & evaluation**

- `day-4a-agent-observability.ipynb`  
  - Logging, traces, and understanding what an agent is doing internally.  
- `day-4b-agent-evaluation.ipynb`  
  - Designing evaluation scenarios and metrics, which informs the miniature evaluation harness in the capstone notebook.  

**Day 5 – Agent‑to‑agent and deployment**

- `day-5a-agent2agent-communication.ipynb`  
  - Agent‑to‑agent communication patterns and protocols.  
- `day-5b-agent-deployment.ipynb`  
  - Deploying ADK agents (e.g., to Vertex AI Agent Engine) and production considerations.  

**Concept papers**

- `Introduction-to-Agents.pdf`  
  - High‑level overview of what agents are and how ADK structures them.  
- `Agent-Tools-Interoperability-with-Model-Context-Protocol-MCP.pdf`  
  - How tools can be exposed via MCP to make agents interoperable with external systems.  

In short: the day‑N notebooks + PDFs are the “textbook”, and `house-price-data-concierge-eda-on-autopilot-1.ipynb` is the final “project report” that applies those ideas to a real Kaggle dataset.  

---

## 3. Capstone notebook: what the agent does

Inside `house-price-data-concierge-eda-on-autopilot-1.ipynb` the agent: [attached_file:124]

- **Loads data**  
  - Uses `load_csv` to bring in the House Prices training CSV and cache it in a simple in‑memory store.

- **Runs data‑quality checks**  
  - `inspect_schema_tool` summarises rows, columns, dtypes, and missing fractions.  
  - Flags high‑missing columns such as `PoolQC`, `Fence`, `Alley`, and `MiscFeature`, and suggests special handling.

- **Performs EDA**  
  - `run_basic_eda` produces numeric distributions and a correlation heatmap.  
  - (Optional) additional tools can generate target‑aware plots showing how `SalePrice` changes across key features.

- **Suggests cleaning steps**  
  - `suggest_cleaning` outputs a human‑readable list of actions: dropping very high‑missing columns, imputing others, encoding categoricals, and keeping an eye on potential leakage columns.

- **Trains a baseline model**  
  - A `scikit-learn` pipeline with `ColumnTransformer`, `OneHotEncoder`, and `RandomForestRegressor` is used to train a quick baseline and report RMSE, giving a starting point for more advanced models.

- **Runs via an ADK Runner**  
  - A `Runner` connects the `DataConciergeAgent` with `InMemorySessionService` and `InMemoryMemoryService`, enabling interactive “chat‑style” EDA inside the notebook.

---

## 4. Agent concepts from the 5‑Day course

The project demonstrates several key AI‑agent concepts from the intensive:

- **Tools & tool best practices**  
  - Custom Python tools with clear docstrings, type hints, and structured dict returns, inspired by the Day‑2 notebooks.  

- **Multi‑agent / orchestration patterns**  
  - A main coordinator agent (`DataConciergeAgent`) plus the option to plug in a specialist EDA agent as an `AgentTool`, borrowing from the architecture and agent‑2‑agent examples.  

- **Sessions & memory**  
  - Use of session services and optional callbacks to persist conversation history and user preferences, based on the sessions/memory notebooks.  

- **Evaluation & observability**  
  - A small evaluation harness that runs scripted prompts and logs basic metrics, echoing the principles from the evaluation and observability notebooks.  

- **Deployment‑ready mindset**  
  - The code structure (tools module, agent definition, runner setup) is compatible with the deployment patterns shown in Day‑5; it could be packaged and deployed with minimal refactoring.  

---

## 5. How to run the project

1. **Open the capstone notebook**  
   - `house-price-data-concierge-eda-on-autopilot-1.ipynb` in Kaggle.  

2. **Configure secrets**  
   - In Kaggle, create a User Secret named `GOOGLEAPIKEY` with your Gemini API key.  

3. **Run setup cells**  
   - Install/verify `google-adk`, import libraries, initialise the Gemini model, session service, and memory service.  

4. **Load the housing price dataset**  
   - Run the cell that calls `load_csv` on the training CSV from the Kaggle input directory.  

5. **Interact with the agent**  
   - Use prompts like:
     - “Give me an overview of this dataset and tell me what looks messy.”  
     - “Show which features look most related to SalePrice.”  
     - “Suggest a cleaning plan and then train a quick baseline model.”  

---

## 6. Future directions

Possible next steps building on this repo:

- Add richer feature engineering tools (e.g., total area, log‑transformed `SalePrice`, combined bathroom features).  
- Implement outlier and skew‑detection tools specifically for the housing data.  
- Generalise the EDA tools so the agent can plug into any tabular dataset with minimal changes.  
- Package the agent code into an ADK project and follow the Day‑5 deployment notebook to host it on a managed runtime.  

---

## 7. Acknowledgements

- **Google × Kaggle 5‑Day AI Agents Intensive** for providing the ADK, notebooks, and patterns used throughout this project. [ 
- **Kaggle** for the House Prices competition and the notebook environment. 
- ADK and Gemini teams for the tooling that makes building agentic EDA experiences straightforward.

---
_______________________________________________________________________________________

