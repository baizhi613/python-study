import gradio as gr
import cv2


def turn_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray


iface = gr.Interface(fn=turn_gray, inputs=gr.Image(), outputs="image")

iface.launch()
