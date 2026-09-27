# 🧠 MemorySupport

## AI Customer Support Agent with Long-Term Memory

MemorySupport is an AI customer support agent that remembers previous customer conversations using **Hindsight**.

### 💡 Problem

Traditional support agents may treat every new conversation as a completely new interaction. This can make customers repeat the same information again and again.

### 🚀 Solution

MemorySupport stores important customer interactions and recalls relevant information when the customer returns.

### ✨ Features

* Customer-specific memory
* Stores previous conversations
* Recalls relevant past information
* Personalized support responses
* Simple Streamlit interface
* Hindsight-powered long-term memory

### 🛠️ Technologies

* Python
* Streamlit
* Hindsight
* Hindsight Client

### 🔄 How It Works

1. Customer enters their name and message.
2. MemorySupport checks previous memories.
3. Hindsight retrieves relevant information.
4. The current conversation is saved.
5. The agent uses the remembered context for future conversations.

### ▶️ Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the Hindsight server and then run:

```bash
streamlit run app.py
```

### 🎯 Example

**First conversation:**

> My laptop keyboard is not working properly.

The system stores this information.

**Later conversation:**

> It is still not working.

Hindsight recalls the previous issue, allowing the support agent to continue the conversation with context.

### 📌 Project Goal

The goal of MemorySupport is to demonstrate how long-term memory can make AI customer support more consistent and personalized.

## Hindsight

MemorySupport uses Hindsight to retain and recall customer conversation history.
