import gradio as gr
from recommend import recommend

interface = gr.Interface(
    fn=recommend,
    inputs=gr.Textbox(label="🎥 Enter Movie Name"),
    outputs=gr.HTML(label="🎯 Top 5 Recommendations"),
    title="Movie Recommendation System",
    description="Type a movie name and get top 5 similar movies with posters and clickable YouTube trailers."
)

if __name__ == "__main__":
    interface.launch(share=True)
