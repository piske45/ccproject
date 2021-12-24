# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
快速回復QuickReply
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort
import pandas 
# import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('OxsptkqLALtCQH+hhPm+6an0EMha/JuvKM2Lx/e8jcLRsQmIz96qzPF7WgShwBhrWOLwDbmcjanacZ/SrtpbPDvXsBuAnXQvgtQh7O1IMUQgHv0x3pDbM3d05QvAsnQAKS7UmZhmd7JtrFA0uKA6OwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('141933d571faadf594a7b875a8ad6b5d')

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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     message = text=event.message.text
#     if re.match('告訴我秘密',message):
#         flex_message = TextSendMessage(text='以下有雷，請小心',
#                                quick_reply=QuickReply(items=[
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！")),
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！")),
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！")),
#                                    QuickReplyButton(action=MessageAction(label="別按我", text="你按屁喔！爆炸了拉！！")),
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！")),
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！")),
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！")),
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！")),
#                                    QuickReplyButton(action=MessageAction(label="按我", text="按！"))
#                                ]))
#         line_bot_api.reply_message(event.reply_token, flex_message)
#     else:
#         line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
from linebot.models import FlexSendMessage




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    top_five = {"公司":"123", "怪人":"456"}
    message = text = event.message.text
    if event.message.text in top_five:
        company_name = input()
        content = { "type": "carousel",
                    "contents": [
                     {
                        "type": "bubble",
                        "size": "micro",
                        "hero": {
                            "type": "image",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "320:213"
                             },
                            "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                    "type": "text",
                                    "text": "中國時報",
                                    "weight": "bold",
                                    "size": "sm",
                                    "wrap": True
                                    },
                                    {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                    "type": "text",
                                    "text": "長榮",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xs",
                                    "flex": 5
                                    }
                                    ]
                                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "news1",
                        "uri": "http://linecorp.com/"
                        }
                    },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "news2",
                  "uri": "http://linecorp.com/"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "more",
                  "uri": "http://linecorp.com/"
                }
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "經濟日報",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "長榮",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "news1",
                  "uri": "http://linecorp.com/"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "news2",
                  "uri": "http://linecorp.com/"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "more",
                  "uri": "http://linecorp.com/"
                }
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip12.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Ettoday",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "長榮",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "news1",
                  "uri": "http://linecorp.com/"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "news2",
                  "uri": "http://linecorp.com/"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "more",
                  "uri": "http://linecorp.com/"
                }
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
                    }
                }
            ]
        }
        flex_message = TemplateSendMessage(alt_text = f'{company_name}相關新聞',
        template=CarouselTemplate, #alt_text
            contents= content
        )
        line_bot_api.reply_message(event.reply_token, flex_message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
