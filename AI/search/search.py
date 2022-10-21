from sound_audio import sound_audio as sa
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
from selenium.webdriver.chrome.options import Options

wikipedia.set_lang('vi')
language = 'vi'

path = ChromeDriverManager().install()


'''Tín thể thao (bóng đá)'''
def read_sport():
    sa.speak('Bạn muốn giải nào?')
    query = sa.get_text()
    url = 'https://coccoc.com/search?query=' + query
    webbrowser.open(url)

'''Tín thể thao (bóng đá)'''
def read_xoso():
    sa.speak('Bạn muốn dò tỉnh nào?')
    query = sa.get_text()
    url = 'https://coccoc.com/search?query=xổ số ' + query
    webbrowser.open(url)