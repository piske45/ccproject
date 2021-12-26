from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message
def Recipe_Template():
    message = FlexSendMessage(
        alt_text='當沖前五',
        contents={  "type": "bubble",
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
                                    }
                                )
    return message