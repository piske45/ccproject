from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def carousel_news():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='經濟日報',
                    text='長榮',
                    actions=[
                        URITemplateAction(
                            label='新聞一',
                            uri = 'https://money.udn.com/search/result/1001/%E9%95%B7%E6%A6%AE'
                        ),
                        URITemplateAction(
                            label='新聞二',
                            uri = 'https://money.udn.com/search/result/1001/%E9%95%B7%E6%A6%AE'
                        ),
                        URITemplateAction(
                            label='更多新聞',
                            uri='https://money.udn.com/search/result/1001/%E9%95%B7%E6%A6%AE'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.chinatimes.com/images/2020/logo-chinatimes2020.svg',
                    title='中國時報',
                    text='長榮',
                    actions=[
                        URITemplateAction(
                            label='新聞一',
                            uri = "https://wantrich.chinatimes.com/search/%E9%95%B7%E6%A6%AE"
                        ),
                        URITemplateAction(
                            label='新聞二',
                            uri = "https://wantrich.chinatimes.com/search/%E9%95%B7%E6%A6%AE"
                        ),
                        URITemplateAction(
                            label='更多新聞',
                            uri='https://wantrich.chinatimes.com/search/%E9%95%B7%E6%A6%AE'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn2.ettoday.net/style/finance2020/images/logo.png',
                    title='Ettoday',
                    text='長榮',
                    actions=[
                        URITemplateAction(
                            label='新聞一',
                            uri = "https://wantrich.chinatimes.com/search/%E9%95%B7%E6%A6%AE"
                        ),
                        URITemplateAction(
                            label='新聞二',
                            uri = "https://wantrich.chinatimes.com/search/%E9%95%B7%E6%A6%AE"
                        ),
                        URITemplateAction(
                            label='更多新聞',
                            uri='https://wantrich.chinatimes.com/search/%E9%95%B7%E6%A6%AE'
                        )
                    ]
                )
            ]
        )
    )
    return message