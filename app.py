from Flex_msg import flex_message_carousel
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
#from message import *
#from new import *
#from Function import *
from stock_news import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========
import re
import json

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token 
#這行初始畫了一個 LineBotApi的物件，該物件有一個方法reply_message
#彥伯的
line_bot_api = LineBotApi('2HpPsP97HX8RxipZZ3xq48amAwz6ZquRmepUjQx3m6UKp3DyMLpdXRen78e8fqND15An8ccGrvvDDT0BUl8vDq+efvtKkamWYg6HF1HoH3Te1NQS/rCbADxjsSb4risQtL8JvPyT2F/UptwMaG5SygdB04t89/1O/w1cDnyilFU=')
#line_bot_api = LineBotApi('Io6gQPcag33LY2Nusga5vxQs4Uh7VfkB1K6LRwiOxlCxGOjL4mmzV3gx1NXdSQpq0gGyw/GLtzuAveRCTmEYs2sEvOIfZp2UGC3pRslk7s/j+uh2DTiOlks8CeB1KZzL/RnTXiToNqLcXragQdsv7wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('20e10d583baaa5e37c81fa47e7972b93')
#handler = WebhookHandler('6e28f7f4deebc6a496e80fe58336cce0')

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

#line_bot_api.reply_message(*參數一,*參數二) 接收到其他 LINE 使用者的時候回覆信息
#參數一: reply_token 其他使用者傳送信息給機器人，產生一個reply_token
#參數二: TextSendMessage(text=event.message.text)
#line_bot_api.reply_message(欲回傳者的 token, 回傳的訊息)
#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text #使用者傳入訊息
    emoji = [
        {
            "index": 10,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "038" #>_<_rabbit
        },
        {
            "index": 29,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "079" #nervous_chicken
        },
        {
            "index": 44,
            "productId": "5ac22775040ab15980c9b44c",
            "emojiId": "054" #money_cat
        },
    ]         
    if re.match("前五大", msg):
        FlexMessage = json.load(open('style.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('前五大',FlexMessage))
    elif re.match("長榮", msg):
        message = carousel_news()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "感謝您傳送訊息給我!$\n很抱歉，我沒有辦法對用戶個別回覆。$\n\n敬請期待下次的訊息內容!$", emojis=emoji))

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)

@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
