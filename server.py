
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import  (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
)

app = Flask(__name__)


line_bot_api = LineBotApi('YOUR_Channel_access_token')
handler = WebhookHandler('YOUR_Channel_secret')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):     
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

