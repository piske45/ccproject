# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from typing import Text
from ccClub.template import Carousel_Template, Recipe_Template
from flask import Flask, request, abort
# import requests
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import *
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import re
import json

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('OxsptkqLALtCQH+hhPm+6an0EMha/JuvKM2Lx/e8jcLRsQmIz96qzPF7WgShwBhrWOLwDbmcjanacZ/SrtpbPDvXsBuAnXQvgtQh7O1IMUQgHv0x3pDbM3d05QvAsnQAKS7UmZhmd7JtrFA0uKA6OwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('141933d571faadf594a7b875a8ad6b5d')

#line部屬好主動推播訊息
line_bot_api.push_message('Ua59fcce6ed5bf04270711fb56e4d8e5f', TextSendMessage(text='你可以開始了'))

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
        os.abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg =text = event.message.text
    #前五大字典
    top_five = {"aple": '20', 'orange': "30"}
    #推播前五大當沖股
    top_five_pawn = "apple"
    if re.match('前五大', msg):
        replymessage = top_five_pawn 
        line_bot_api.reply_message(event.reply_token, TextSendMessage(replymessage))
    #前五大相關新聞
    elif msg in top_five:
        # message = Recipe_Template()
        message = "allpyfy"
        line_bot_api.reply_message(event.reply_token, message)
    else:
        # message = Carousel_Template()
        message = "yjbk"
        line_bot_api.reply_message(event.reply_tolen, message)


    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
