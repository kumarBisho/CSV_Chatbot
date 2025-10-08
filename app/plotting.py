import pandas as pd
import matplotlib.pyplot as plt
import tempfile

def generate_plot(file, column, plot_type):
    if file is None:
        return "Please upload a CSV file."

    try:
        df = pd.read_csv(file)
        if column not in df.columns:
            return f"Error: Column '{column}' not found in the CSV file."

        plt.figure(figsize=(6, 4))

        if plot_type == "Histogram":
            if pd.api.types.is_numeric_dtype(df[column]):
                df[column].hist(bins=20, edgecolor="black")
                plt.xlabel(column); plt.ylabel("Frequency"); plt.title(f"Histogram of {column}")
            else:
                df[column].value_counts().plot(kind='bar', edgecolor="black")
        elif plot_type == "Scatter Plot":
            if len(df.columns) < 2:
                return "Error: Need at least two columns for a scatter plot."
            plt.scatter(df[column], df[df.columns[1]])
            plt.xlabel(column); plt.ylabel(df.columns[1]); plt.title(f"Scatter Plot of {column} vs {df.columns[1]}")
        elif plot_type == "Bar Chart":
            df[column].value_counts().plot(kind='bar', edgecolor="black")
        elif plot_type == "Line Plot":
            df[column].plot(kind='line')

        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        plt.savefig(temp_file.name, format='png')
        plt.close()
        return temp_file.name

    except Exception as e:
        return f"Error generating plot: {e}"
