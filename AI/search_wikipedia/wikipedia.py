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

'''Tính năng Tìm kiếm trên Wikipedia'''
def tell_me_about():
    try:
        sa.speak("Bạn muốn nghe về gì ạ")
        text = sa.get_text()
        contents = wikipedia.summary(text).split('\n')
        sa.speak(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            sa.speak("Bạn muốn nghe thêm không")
            ans = sa.get_text()
            if "có" not in ans:
                break    
            sa.speak(content)
            time.sleep(10)

        sa.speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        sa.speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
