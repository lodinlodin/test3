
import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, StickerSendMessage)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('y0wxrie0yCSsxFMortNFIhu9c+k0ZtpmoXiajRGT8MzDOx/bk72V2K0mEp6PDrKwRDZcI65EC0BKC0yr/GDNjSipYiyRgXfI3k6yVZD+rLhxafXUnBLaBnHzFiJkLwWUMhGl0DEA1HRqeaa6k/PnnAdB04t89/1O/w1cDnyilFU='))
handler = WebhookHandler(os.environ.get('41a783d27aadf8cb3165519b1694f29c'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook bodyeeee
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

    # 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
