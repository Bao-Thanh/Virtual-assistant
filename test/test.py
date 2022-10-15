import unicodedata
from bs4 import BeautifulSoup
import logging
import argparse
from sys import argv
from subprocess import Popen, check_output, CalledProcessError
from re import search, IGNORECASE
from os.path import isdir, isfile
from pywinauto import application
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
import http.client as httplib
from selenium.webdriver.chrome.options import Options
import math

path = ChromeDriverManager().install()
language = 'vi'


def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s


def create_url(s):
    kq = 'xs' + s[0]
    for i in range(0, len(s)):
        if (s[i] == '-'):
            kq += s[i + 1]
    return kq


tinh = "Bình Dương"
tinh = no_accent_vietnamese(tinh).lower()
temp = tinh.replace(" ", "-")
kq = create_url(temp)
r = requests.get(
    'https://xskt.com.vn/do-ve-so/'+ temp + '-' + kq + '?d=14-10-2022&v=223670')
soup = BeautifulSoup(r.content, 'html.parser')

kq = []
a = soup.find('div', class_='box-table')
b = a.find('div', class_='cau-box2')
lines = b.find_all('b')
print('Kết quả xố số Bình Dương số 223670 ngày 14/10/2022')
for line in lines:
    kq.append(line.text)
print(kq[0], ', vé số của bạn đã trúng', kq[1], 'trị giá', kq[2])
