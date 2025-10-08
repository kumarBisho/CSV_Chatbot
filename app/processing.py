import pandas as pd
from app.ollama_utils import query_llm

def process_query(query, file):
    if file is None:
        return "Error: Please upload a CSV file.", None

    try:
        df = pd.read_csv(file)
        if df.empty:
            return "Error: The uploaded CSV file is empty.", None

        summary = df.describe(include='all').to_string()
        categorical_summary = "\n\nCategorical Data Summary:\n"
        for col in df.select_dtypes(include=['object']).columns:
            categorical_summary += f"{col}:\n{df[col].value_counts().to_string()}\n\n"

        full_summary = summary + categorical_summary
        
        # summary = df.describe(include='number').head(5).to_string()
        # categorical_summary = "\n".join([
        #     f"{col}: {df[col].value_counts().head(5).to_dict()}" 
        #     for col in df.select_dtypes(include=['object']).columns
        # ])
        # full_summary = summary + "\n" + categorical_summary
        
        response = query_llm(query, full_summary)
        return response, df
    except Exception as e:
        return f"Error processing file: {e}", None
