import gradio as gr
from app.processing import process_query
from app.plotting import generate_plot

def create_app():
    with gr.Blocks() as demo:
        gr.Markdown("## CSV Query and Visualization Tool (Ollama)")

        with gr.Row():
            csv_file = gr.File(label="Upload CSV")

        with gr.Row():
            query_input = gr.Textbox(label="Enter your query")
            query_output = gr.Textbox(label="LLM Response")

        query_button = gr.Button("Process Query")
        query_button.click(process_query,
                           inputs=[query_input, csv_file],
                           outputs=[query_output, gr.Dataframe()])

        with gr.Row():
            column_name = gr.Textbox(label="Column for Plot", placeholder="write a column name")
            plot_type = gr.Dropdown(label="Plot Type",
                                    choices=["Histogram", "Scatter Plot", "Bar Chart", "Line Plot"])
            plot_output = gr.Image(label="Plot Output")

        plot_button = gr.Button("Generate Plot")
        plot_button.click(generate_plot,
                          inputs=[csv_file, column_name, plot_type],
                          outputs=plot_output)
    return demo


if __name__ == "__main__":
    app = create_app()
    # app.launch(server_name="0.0.0.0", server_port=7860)
    app.launch(server_name="localhost", server_port=8080)
