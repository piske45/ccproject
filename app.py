# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
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
    fruit = {"aple": '20', 'orange': "30"}
    #推播前五大當沖股
    top_five = "apple"
    if re.match('前五大', message):
        replymessage = top_five 
        line_bot_api.reply_message(event.reply_token, TextSendMessage(replymessage))
    else:
        error_message = '不好意思'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(error_message))
        if message in fruit:
            rep = 'ko'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(rep))
    #推播新聞
    #if re.match('新聞', message):


    # top_five = {"公司":"123", "怪人":"456"}
    # # message = text = event.message.text
    # company_name = input()
    # # if event.message.text in top_five:
    # message = {
    #     "type": "template",
    #     "altText": "this is a carousel template",
    #     "template": {
    #         "type": "carousel",
    #         "columns": [
    #         {
    #             "thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg",
    #             "title": "經濟日報",
    #             "text": "今日焦點",
    #             "actions": [
    #             {
    #                 "type": "uri",
    #                 "label": "第一篇",
    #                 "uri": "https://wantrich.chinatimes.com/"
    #             },
    #             {
    #                 "type": "uri",
    #                 "label": "第二篇",
    #                 "uri": "https://wantrich.chinatimes.com/"
    #             },
    #             {
    #                 "type": "uri",
    #                 "label": "更多新聞",
    #                 "uri": "https://wantrich.chinatimes.com/"
    #             }
    #             ],
    #             "imageBackgroundColor": "#FFFFFF"
    #         },
    #         {
    #             "thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg",
    #             "title": "中時新聞",
    #             "text": "今日焦點",
    #             "actions": [
    #             {
    #                 "type": "message",
    #                 "label": "動作我今天天氣很好好好好好好好襖好好好好",
    #                 "text": "動作 1"
    #             },
    #             {
    #                 "type": "message",
    #                 "label": "動作 2",
    #                 "text": "動作 2"
    #             },
    #             {
    #                 "type": "message",
    #                 "label": "動作 3",
    #                 "text": "動作 3"
    #             }
    #             ]
    #         },
    #         {
    #             "thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg",
    #             "title": "ETtoday",
    #             "text": "今日焦點新聞",
    #             "actions": [
    #             {
    #                 "type": "uri",
    #                 "label": "動作 1",
    #                 "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"
    #             },
    #             {
    #                 "type": "uri",
    #                 "label": "動作 2",
    #                 "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"
    #             },
    #             {
    #                 "type": "uri",
    #                 "label": "動作 3",
    #                 "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"
    #             }
    #             ]
    #         },
    #         {
    #             "thumbnailImageUrl": "https://images.chinatimes.com/newsphoto/2021-12-22/1024/20211222004875.jpg",
    #             "title": "聚亨",
    #             "text": "今日焦點新聞",
    #             "actions": [
    #             {
    #                 "type": "uri",
    #                 "label": "動作 1",
    #                 "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"
    #             },
    #             {
    #                 "type": "uri",
    #                 "label": "動作 2",
    #                 "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"
    #             },
    #             {
    #                 "type": "uri",
    #                 "label": "動作 3",
    #                 "uri": "https://taichunmin.idv.tw/blog/2020-04-06-line-devbot.html"
    #             }
    #             ]
    #         }
    #         ]
    #     }
    #     }
    #     # flex_message = TemplateSendMessage(alt_text = f'{company_name}相關新聞',
    #     # template=CarouselTemplate, #alt_text
    #     # columns = Content
    #     # )
    #     # line_bot_api.reply_message(event.reply_token, flex_message)
    
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text = event.message.text))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
