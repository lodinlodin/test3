# lee
import os
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

line_bot_api = LineBotApi(os.environ.get('YOUR_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('YOUR_CHANNEL_SECRET'))


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
        print("Invalid signature. Please check your channel access token/channel secret.")
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

#文字訊息

try:
    line_bot_api.push_message(to, TextSendMessage(text='台科大電腦研習社'))
except LineBotApiError as e:
    # error handle
    raise e

#圖片訊息
# ImageSendMessage物件中的輸入
# original_content_url 以及 preview_image_url都要寫才不會報錯。
#輸入的網址要是一個圖片，應該說只能是一個圖片，不然不會報錯但是傳過去是灰色不能用的圖
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
image_url = "https://i.imgur.com/eTldj2E.png?1"
try:
    line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
except LineBotApiError as e:
    # error handle
    raise e