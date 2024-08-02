import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab(label="txt.img"):
        with gr.Row():
            with gr.Column(scale=15):
                txt1 = gr.Textbox(lines=2, label="")
                txt2 = gr.Textbox(lines=2, label="")
            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button(value="1")
                button2 = gr.Button(value="2")
                button3 = gr.Button(value="3")
                button4 = gr.Button(value="4")
            with gr.Column(scale=6):
                generate_button = gr.Button(value="Generate", variant="primary", scale=1)
                with gr.Row():
                    dropdown1 = gr.Dropdown(["1", "2", "3", "4"], label="Style1")
                    dropdown2 = gr.Dropdown(["1", "2", "3", "4"], label="Style2")
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    dropdown3 = gr.Dropdown(["1", "2", "3", "4"], label="Sampling method")
                    slider1 = gr.Slider(minimum=0, maximum=100, label="Sampling steps")
                checkboxgroup = gr.Checkboxgroup(["Restore faces", "Tilling", "Hires.fix"], label="Style3")
                with gr.Row():
                    slider2 = gr.Slider(minimum=0, maximum=100, label="Width")
                    slider3 = gr.Slider(minimum=0, maximum=100, label="Batch count")
                with gr.Row():
                    slider4 = gr.Slider(minimum=0, maximum=100, label="Height")
                    slider5 = gr.Slider(minimum=0, maximum=100, label="Batch size")
                slider6 = gr.Slider(minimum=0, maximum=100, label="CFG scale")
                with gr.Row():
                    number1 = gr.Number(label="Seed", scale=5)
                    button5 = gr.Button(value="Randomize", min_width=1)
                    button6 = gr.Button(value="Reset", min_width=1)
                    checkbox1 = gr.Checkbox(label="Extra", min_width=10)
                dropdown4 = gr.Dropdown(["1", "2", "3", "4"], label="Script")
            with gr.Column():
                gallery = gr.Gallery(["D:/code/python/python-gradio/GenshinImpactCloudGame/1.jpg",
                                      "D:/code/python/python-gradio/GenshinImpactCloudGame/108758166_p0_master1200.jpg",
                                      "D:/code/python/python-gradio/GenshinImpactCloudGame/113784387_p0_master1200.jpg",
                                      "D:/code/python/python-gradio/GenshinImpactCloudGame/116645978_p0.jpg",
                                      "D:/code/python/python-gradio/GenshinImpactCloudGame/116723029_p.png"], columns=3)
                with gr.Row():
                    button7 = gr.Button(value="Save", min_width=1)
                    button8 = gr.Button(value="Save", min_width=1)
                    button9 = gr.Button(value="Zip", min_width=1)
                    button10 = gr.Button(value="Send to img2img", min_width=1)
                    button11 = gr.Button(value="Send to inpaint", min_width=1)
                    button12 = gr.Button(value="Send to extras", min_width=1)

                txt3 = gr.Textbox(lines=4, label="")
demo.launch()
