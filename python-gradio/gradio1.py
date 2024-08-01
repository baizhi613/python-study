import gradio as gr


def greet(name):
    return "Hello" + name + "!"


iface = gr.Interface(fn=greet, inputs=gr.Textbox(lines=5,placeholder="name here",label="name:"), outputs=gr.Textbox(label="Greeting"))

iface.launch()
