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
# from flask import Flask, request, abort
import pandas 
import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
# app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('OxsptkqLALtCQH+hhPm+6an0EMha/JuvKM2Lx/e8jcLRsQmIz96qzPF7WgShwBhrWOLwDbmcjanacZ/SrtpbPDvXsBuAnXQvgtQh7O1IMUQgHv0x3pDbM3d05QvAsnQAKS7UmZhmd7JtrFA0uKA6OwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('141933d571faadf594a7b875a8ad6b5d')

line_bot_api.push_message('Ua59fcce6ed5bf04270711fb56e4d8e5f', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = requests.headers['X-Line-Signature']

    # get request body as text
    body = requests.get_data(as_text=True)
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

top_five = {}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

resp = requests.get('https://goodinfo.tw/StockInfo/StockList.asp?MARKET_CAT=%E7%86%B1%E9%96%80%E6%8E%92%E8%A1%8C&INDUSTRY_CAT=%E5%B9%B3%E5%9D%87%E6%8C%AF%E5%B9%85+%28%E4%BB%8A%E5%B9%B4%29%40%40%E5%B9%B3%E5%9D%87%E6%8C%AF%E5%B9%85%40%40%E4%BB%8A%E5%B9%B4&SHEET=%E6%BC%B2%E8%B7%8C%E5%8F%8A%E6%88%90%E4%BA%A4%E7%B5%B1%E8%A8%88&SHEET2=%E5%90%84%E6%9C%9F%E5%B9%B3%E5%9D%87%E6%8C%AF%E5%B9%85%E7%B5%B1%E8%A8%88', headers = headers)

    #將亂碼轉碼
resp.encoding = 'utf - 8'
soup = BeautifulSoup(resp.text, 'lxml')

    #數據被放在txtStockListData裡面
data = soup.select_one('#txtStockListData')
dfs = pandas.read_html(data.prettify())

num = list(dfs[2][:5]['代號'])
name = list(dfs[2][:5]['名稱'])
data3 = dfs[1][:5]
amplitude = list(data3.loc[:5]['3日  平均  振幅'])

    #創建dataframe資料庫
data2 = pandas.DataFrame({
        "代號" : num,
        "名稱" : name,
        "平均三日振幅": amplitude}, 
    index = ['1', '2', '3', '4', '5'])
for i in range(1,6):
    top_five[i] = num+name

print(data2)
print(top_five)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text in top_five:

    # if event.message.text[:2].upper() == "#K":
    #     input_word = event.message.text.replace(" ","") #合併字串取消空白
    #     stock_name = input_word[2:6] #0050
    #     start_date = input_word[6:] #2020-01-01
    #     content = plot_stcok_k_chart(IMGUR_CLIENT_ID,stock_name,start_date)
        company_name = input()
        flex_message = FlexSendMessage(
            alt_text = f'{company_name}相關新聞' #alt_text
            contents={
        "type": "carousel",
        "contents": {"type": "bubble",
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
            {"type": "bubble",
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
                    "wrap": true
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
                            "wrap": true,
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
                            "wrap": true,
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
    #     )
    #     line_bot_api.reply_message(event.reply_token, flex_message)
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
