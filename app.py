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

from linebot.models import FlexSendMessage
from linebot.models import TemplateSendMessage

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text = event.message.text
    #前五大字典
    top_five = {"aple": '20', 'orange': "30"}
    #推播前五大當沖股
    top_five_pawn = "apple"
    if re.match('前五大', message):
        replymessage = top_five_pawn 
        line_bot_api.reply_message(event.reply_token, TextSendMessage(replymessage))
    #前五大相關新聞
    elif message in top_five:
        rep = 'ko'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(rep))
    
    else:
        #error_message = '不好意思'
        error_message = TextMessage({
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "昨日前五大當沖交易股",
        "weight": "bold",
        "size": "xl",
        "margin": "none"
      },
      {
        "type": "text",
        "text": "以及平均三日振福",
        "size": "lg",
        "color": "#000000",
        "wrap": True
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "6485   點序",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "3.48",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "3169   亞信",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "3.84",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "2615   萬海",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "3.11",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "2609   陽明",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "2.29",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "5608  四維航",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "2.31",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": False
    }
  }
})
        line_bot_api.reply_message(event.reply_tolen, TextSendMessage(error_message))
            # 
            # line_bot_api.reply_message(event.reply_token, flex_message)    
    #推播新聞
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
