
import json

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    user_id = event.source.user_id
    print("user_id =", user_id)

    from linebot import LineBotApi
    from linebot.models import TextSendMessage, ImageSendMessage
    from linebot.exceptions import LineBotApiError

    CHANNEL_ACCESS_TOKEN = "YOUR CHANNEL TOKEN"
    to = "YOUR USER ID"

    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

    try:
    line_bot_api.push_message(to, TextSendMessage(text='台科大電腦研習社'))
    except LineBotApiError as e:
    # error handle
        raise e
        line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
        image_url = "https://i.imgur.com/eTldj2E.png?1"
    try:
        line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url,  preview_image_url=image_url))
    except LineBotApiError as e:
    # error handle
        raise e

@app.route('/')
def homepage():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()