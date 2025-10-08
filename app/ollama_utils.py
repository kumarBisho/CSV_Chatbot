import ollama

OLLAMA_MODEL = "llama3"

def query_llm(query: str, df_summary: str) -> str:
    """Process user query using Ollama AI model."""
    prompt = f"""You are an AI trained to analyze CSV data.
    Here is a summary of the dataset:
    {df_summary}

    User Query: {query}
    Provide a clear and concise answer.
    """

    try:
        response = ollama.chat(model=OLLAMA_MODEL,
                               messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"
