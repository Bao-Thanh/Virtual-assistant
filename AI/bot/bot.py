import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
wikipedia.set_lang('vi')
language = 'vi'

from sound_audio import sound_audio as sa

'''Tính năng Chào hỏi'''
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        sa.speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        sa.speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        sa.speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))

'''Thoát chương trình'''
def stop():
    sa.speak("Hẹn gặp lại bạn sau!")
    
    '''Tính năng Hiển thị thông tin các tính năng Bot có thể làm được'''
def help_me():
    sa.speak("""Bot có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Dự báo thời tiết
    7. Mở video nhạc
    8. Thay đổi hình nền máy tính
    9. Đọc báo hôm nay
    10. Kể bạn biết về thế giới """)
    time.sleep(20)