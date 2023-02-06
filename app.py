from transformers import pipeline
import gradio as gr


def hello(i):
    # classifier = pipeline("sentiment-analysis")
    # a = classifier(i)
    # return a
    return "Hello World!"

iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
