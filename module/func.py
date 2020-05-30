from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
import datetime
from datetime import date
import time
import calendar
import gspread
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials
from module import todatabase
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def fix(event): #系統
    reply="系統維護中"
    try:
        message = TextSendMessage(  
            text = reply
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def unauthorize(event):#沒權限
    try:
        message = TextSendMessage(  
            text = "您沒有新增及刪除的權限"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def manual(event): #功能簡介
    reply="請開啟選單開始使用本系統\n\n"
    reply+="使用方法\n"
    reply+="https://hackmd.io/TOAK5TdJSS-4Un4BuO2T2w\n"
    reply+="版本紀錄\n"
    reply+="https://hackmd.io/YvYW8hDkSwG3ZDgm1p0VRg\n"
    reply+="本程式官方網站\n"
    reply+="http://cbfhss.nctu.me/\n"
    reply+="錯誤回報&給予建議\n"
    reply+="https://forms.gle/ynVoyBhhJNyvypP9A\n"
    reply+="隱私權條款\n"
    reply+="https://www.ppt.cc/fkorqx"
    try:
        message = TextSendMessage(  
            text = reply
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
