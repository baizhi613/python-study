import gradio as gr
import pytesseract
from PIL import Image


# 定义OCR函数
def ocr_image(image):
    # 使用pytesseract进行OCR处理
    text = pytesseract.image_to_string(image)
    return text


# 创建Gradio接口
interface = gr.Interface(
    fn=ocr_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="图片文字识别",
    description="上传图片并提取图片中的文字"
)

# 启动接口
interface.launch()
