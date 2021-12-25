# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from typing import Text
from flask import Flask, request, abort
# import requests
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import *
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import re

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

from linebot.models import FlexSendMessage
from linebot.models import TemplateSendMessage

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text = event.message.text
    top_five = {"aple": '20', 'orange': "30"}
    #推播前五大當沖股
    top_five_pawn = "apple"
    if re.match('前五大', message):
        replymessage = top_five_pawn 
        line_bot_api.reply_message(event.reply_token, TextSendMessage(replymessage))
    elif message in top_five:
        rep = 'ko'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(rep))
    else:
        error_message = '不好意思'
        line_bot_api.reply_message(event.reply_tolen, TextSendMessage(error_message))
            # 
            # line_bot_api.reply_message(event.reply_token, flex_message)    
    #推播新聞
    if re.match('新聞', message):
        flex_message = FlexSendMessage(
            alt_text = '新聞',
            contents =  {"type": "template", "altText": "this is a carousel template", "template": {"type": "carousel", "columns": [{"thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg", "title": "\u7d93\u6fdf\u65e5\u5831", "text": "\u4eca\u65e5\u7126\u9ede", "actions": [{"type": "uri", "label": "\u7b2c\u4e00\u7bc7", "uri": "https://wantrich.chinatimes.com/"}, {"type": "uri", "label": "\u7b2c\u4e8c\u7bc7", "uri": "https://wantrich.chinatimes.com/"}, {"type": "uri", "label": "\u66f4\u591a\u65b0\u805e", "uri": "https://wantrich.chinatimes.com/"}], "imageBackgroundColor": "#FFFFFF"}, {"thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg", "title": "\u4e2d\u6642\u65b0\u805e", "text": "\u4eca\u65e5\u7126\u9ede", "actions": [{"type": "message", "label": "\u52d5\u4f5c\u6211\u4eca\u5929\u5929\u6c23\u5f88\u597d\u597d\u597d\u597d\u597d\u597d\u597d\u8956\u597d\u597d\u597d\u597d", "text": "\u52d5\u4f5c 1"}, {"type": "message", "label": "\u52d5\u4f5c 2", "text": "\u52d5\u4f5c 2"}, {"type": "message", "label": "\u52d5\u4f5c 3", "text": "\u52d5\u4f5c 3"}]}, {"thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg", "title": "ETtoday", "text": "\u4eca\u65e5\u7126\u9ede\u65b0\u805e", "actions": [{"type": "uri", "label": "\u52d5\u4f5c 1", "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"}, {"type": "uri", "label": "\u52d5\u4f5c 2", "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"}, {"type": "uri", "label": "\u52d5\u4f5c 3", "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"}]}, {"thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg", "title": "\u805a\u4ea8", "text": "\u4eca\u65e5\u7126\u9ede\u65b0\u805e", "actions": [{"type": "uri", "label": "\u52d5\u4f5c 1", "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"}, {"type": "uri", "label": "\u52d5\u4f5c 2", "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"}, {"type": "uri", "label": "\u52d5\u4f5c 3", "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"}]}]}}
            )
        line_bot_api.reply_message(event.reply_token, flex_message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
