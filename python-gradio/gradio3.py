import gradio as gr

input_list = [
    gr.Audio(sources=["microphone", "upload"], type="numpy", label="Audio File"),
    gr.Checkbox(label="Checkbox"),
    gr.ColorPicker(label="Color Picker"),
    gr.DataFrame(label="DataFrame"),
    gr.Dropdown(["option 1", "option 2", "option 3"], label="Dropdown"),
    gr.File(label="File", type="binary"),
    gr.Image(sources=["webcam", "upload"], label="Image"),
    gr.Number(label="Number"),
    gr.Radio(["option 1", "option 2", "option 3"], label="Radio"),
    gr.Slider(minimum=0, maximum=10, label="Slider", step=5),
    gr.Textbox(label="Textbox", lines=3, max_lines=7, placeholder="placeholder"),
    gr.TextArea(label="TextArea", lines=3, max_lines=7, placeholder="placeholder"),
    gr.Video(sources=["webcam", "upload"], label="Video"),
]

output_list = [
    gr.Textbox(label="Audio outputs", lines=7),
    gr.Textbox(label="Checkbox outputs"),
    gr.Textbox(label="ColorPicker outputs"),
    gr.Textbox(label="DataFrame outputs"),
    gr.Textbox(label="Dropdown outputs"),
    gr.Textbox(label="File outputs"),
    gr.Textbox(label="Image outputs"),
    gr.Textbox(label="Number outputs"),
    gr.Textbox(label="Radio outputs"),
    gr.Textbox(label="Slider outputs"),
    gr.Textbox(label="Textbox outputs"),
    gr.Textbox(label="TextArea outputs"),
    gr.Textbox(label="Video outputs"),
]


def input_and_output(*input_data):
    return input_data


iface = gr.Interface(fn=input_and_output,
                     inputs=input_list,
                     outputs=output_list,
                     title="Input and outputs",
                     description="This is a test of all input types.",
                     live=True,
                     )

iface.launch()
