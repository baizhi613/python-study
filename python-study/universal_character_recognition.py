import gradio as gr
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import json
import requests
from PIL import Image
import io


class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(self, host, path, schema):
        self.host = host
        self.path = path
        self.schema = schema


# 计算 sha256 并编码为 base64
def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
    return digest


def parse_url(requset_url):
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3:]
    schema = requset_url[:stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise AssembleHeaderException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    return Url(host, path, schema)


# 构建 websocket 认证请求 URL
def assemble_ws_auth_url(requset_url, method="POST", api_key="", api_secret=""):
    u = parse_url(requset_url)
    host = u.host
    path = u.path
    now = datetime.now()
    date = format_date_time(mktime(now.timetuple()))
    signature_origin = f"host: {host}\ndate: {date}\n{method} {path} HTTP/1.1"
    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
    authorization_origin = (f"api_key=\"{api_key}\", algorithm=\"hmac-sha256\", headers=\"host date request-line\", "
                            f"signature=\"{signature_sha}\"")
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }
    return requset_url + "?" + urlencode(values)


def ocr_image(image):
    # 使用你的APPID、APIKey和APISecret替换以下值
    APPId = "d071f0f9"
    APIKey = "7db87320083e1ecdaf39d3d137798266"
    APISecret = "YWI2YzQ3NmJlN2E2MGNhM2NiOTE0NmU4"

    # 将上传的图片转换为字节
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    imageBytes = buf.getvalue()

    url = 'https://api.xf-yun.com/v1/private/sf8e6aca1'
    body = {
        "header": {
            "app_id": APPId,
            "status": 3
        },
        "parameter": {
            "sf8e6aca1": {
                "category": "ch_en_public_cloud",
                "result": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "json"
                }
            }
        },
        "payload": {
            "sf8e6aca1_data_1": {
                "encoding": "jpg",
                "image": str(base64.b64encode(imageBytes), 'UTF-8'),
                "status": 3
            }
        }
    }

    request_url = assemble_ws_auth_url(url, "POST", APIKey, APISecret)
    headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': APPId}

    response = requests.post(request_url, data=json.dumps(body), headers=headers)

    if response.status_code != 200:
        return ""

    tempResult = json.loads(response.content.decode())

    if 'payload' in tempResult and 'result' in tempResult['payload']:
        text = base64.b64decode(tempResult['payload']['result']['text']).decode()
        text_json = json.loads(text)

        words = []
        for page in text_json.get('pages', []):
            for line in page.get('lines', []):
                for word in line.get('words', []):
                    words.append(word.get('content', ' '))

        return ' '.join(words)
    else:
        return ""


# 创建Gradio Blocks界面
with gr.Blocks() as demo:
    gr.Markdown("# 智能阅卷系统\n上传试卷并提取文字")

    with gr.Row():
        with gr.Column():
            img_input = gr.Image(type="pil", label="上传试卷图片")
            ocr_button = gr.Button(value="开始识别", variant="primary")
        with gr.Column():
            ocr_output = gr.Textbox(label="识别结果", lines=10, placeholder="此处为识别结果")

    ocr_button.click(fn=ocr_image, inputs=img_input, outputs=ocr_output)

# 启动界面
demo.launch()
