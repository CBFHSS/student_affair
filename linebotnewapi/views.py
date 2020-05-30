from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from module import func,todatabase,authorize

import math
import sys
import datetime
from datetime import date,timedelta
import time
import calendar
import mysql.connector

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == "使用方法":
                        func.manual(event)
                    #體溫登陸
                    if mtext[0]=="體" and mtext[1]=="溫":
                        destclass="lssh"+mtext[3]+mtext[4]+mtext[5]
                        lssh1 = mysql.connector.connect(
                        host = todatabase.host(),
                        port = "3306",
                        user = "liaojason2",
                        password = "Liaojason123!",
                        database = destclass)
                        try:
                            gcpsql= lssh1.cursor()
                            output=""
                            sql_select_Query = "select * from body_temperture"
                            gcpsql.execute(sql_select_Query)
                            records = gcpsql.fetchall()
                            output+=destclass[4]+destclass[5]+destclass[6]+" 體溫總表：\n\n"
                            for row in records:
                                output+=str(row[1])+". "+str(row[3])+" "+str(row[4])+"\n"
                            output+="\n輸出結束"
                            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=output))
                        except:
                            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="本班級不存在"))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()