import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QProcess, QTextCodec
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QPlainTextEdit

import os
from gtts import gTTS
import playsound
import speech_recognition
from time import strftime
import time
import datetime
import random
import re
import webbrowser
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from youtubesearchpython import SearchVideos
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
from selenium.webdriver.chrome.options import Options
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

path = ChromeDriverManager().install()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.resize(563, 799)
centralwidget = QtWidgets.QWidget(MainWindow)
centralwidget.setObjectName("centralwidget")
plainTextEdit = QtWidgets.QPlainTextEdit(centralwidget)
plainTextEdit.setGeometry(QtCore.QRect(0, 10, 561, 661))
font = QtGui.QFont()
font.setPointSize(20)
plainTextEdit.setFont(font)
plainTextEdit.setObjectName("plainTextEdit")
pushButton = QtWidgets.QPushButton(centralwidget)
pushButton.setGeometry(QtCore.QRect(460, 680, 101, 61))
font = QtGui.QFont()
font.setPointSize(20)
pushButton.setFont(font)
pushButton.setObjectName("pushButton")

def speak(text):
        print("AI:  {}".format(text))
        plainTextEdit.insertPlainText("AI: "+text+"\n")
        tts = gTTS(text=text, lang='vi', slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", False)
        os.remove("sound.mp3")
def get_audio():
        playsound.playsound("Ping.mp3", False)
        time.sleep(1)
        print("\nAi:  Đang nghe ...")
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("You: ")
            audio = r.listen(source, phrase_time_limit=6)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                print(text)
                return text.lower()
            except:
                print("\n")
                return ""
def hello():
        day_time = int(strftime('%H'))
        if day_time < 11:
            speak("Chào buổi sáng tốt lành.AI có thể giúp gì được cho bạn.")
        elif 11 <= day_time < 13:
            speak("Chào buổi trưa tốt lành.AI có thể giúp gì được cho bạn.")
        elif 13 <= day_time < 18:
            speak("Chào buổi chiều tốt lành.AI có thể giúp gì được cho bạn.")
        else:
            speak("Chào buổi tối tốt lành.AI có thể giúp gì được cho bạn.")
        time.sleep(5)
def get_time(text):
        now = datetime.datetime.now()
        now1 = datetime.datetime.now().strftime("%w")
        now2 = int(now1)
        now3 = "Chủ Nhật"
        if "giờ" in text:
            speak('Bây giờ là %d giờ %d phút %d giây' %
                (now.hour, now.minute, now.second))
        elif "ngày" in text:
            speak("Hôm nay là ngày %d tháng %d năm %d" %
                (now.day, now.month, now.year))
        elif "thứ" in text and now2 != 0:
            speak('Hôm nay là thứ %s' % (now2+1))
        elif "thứ" in text and now2 == 0:
            speak('Hôm nay là %s' % (now3))
        else:
            speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
            time.sleep(6)
        time.sleep(5)
def open_application(text):
        if "cốc cốc" in text:
            os.startfile('C:\\Users\\ACER\\Desktop\\Cốc Cốc')
            speak("Cốc Cốc được mở")
        elif "word" in text:
            os.startfile('C:\\Users\\ACER\\Desktop\\Microsoft Word 2010')
            speak("Microsoft Word được mở")
        elif "excel" in text:
            os.startfile('C:\\Users\\ACER\\Desktop\\Microsoft Excel 2010')
            speak("Microsoft Excel được mở")
        elif "chrome" in text:
            os.startfile(
                'C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe')
            speak("Google Chrome được mở")
        elif "team" in text:
            os.startfile('C:\\Users\\ACER\\Desktop\\Microsoft Teams')
            speak("Microsoft Teams được mở")
        else:
            speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
        time.sleep(6)
def open_website(text):
        reg_ex = re.search('mở website (.+)', text)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak("Trang web bạn yêu cầu đã được mở.")
        else:
            speak("AI không nghe rõ bạn nói lại được không?.")
        time.sleep(5)
def open_google_and_search(text):
        search_for = text.split("kiếm", 1)[1]
        speak('AI đang tìm kiếm giúp bạn')
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.google.com")
        que = driver.find_element("xpath", "//input[@name='q']")
        que.send_keys(str(search_for))
        que.send_keys(Keys.RETURN)
        time.sleep(6)
        
def weather(text):
        temp = "Trời quang mây tạnh"
        if "moderate rain" in text:
            temp = "Trời hôm nay có mưa vừa, bạn ra ngoài nhớ mang theo áo mưa"
        elif "heavy intensity rain" in text or "thunderstorm with light rain" in text or "very heavy rain" in text:
            temp = "Trời hôm nay có mưa rất lớn kèm theo giông sét, bạn nhớ đem ô dù khi ra ngoài"
        elif "light rain" in text:
            temp = "Trời hôm nay mưa nhẹ, rải rác một số nơi"
        elif "heavy intensity shower rain" in text:
            temp = "Trời hôm nay có mưa rào với cường độ lớn"
        elif "broken clouds" in text or "few clouds" in text:
            temp = "Trời hôm nay có mây rải rác, không mưa"
        elif "overcast clouds" in text:
            temp = "Trời hôm nay nhiều mây, u ám, dễ có mưa"
        elif "scattered clouds" in text:
            temp = "Trời hôm nay có nắng, có mây rải rác"
        return temp
def temperature(self, text):
        temp = "mát mẻ"
        if text < 15:
            temp = "lạnh buốt giá"
        elif text < 20:
            temp = "khá lạnh"
        elif text < 30:
            temp = "mát mẻ"
        elif text < 33:
            temp = "khá nóng"
        else:
            temp = "nóng bức"

        return temp

def current_weather():
        speak("Bạn muốn xem thời tiết ở đâu vậy.")
        time.sleep(3)
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = get_audio()
        plainTextEdit.insertPlainText("You: "+city+"\n")
        if city == "":
            current_weather()
        else:
            api_key = "b0d4f9bfd2bbc40d10976e6fd3ea7514"
            call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
            response = requests.get(call_url)
            data = response.json()
            if data["cod"] != "404":
                city_res = data["main"]
                current_humidity = city_res["humidity"]
                current_temperature = city_res["temp"]
                temperature1 = temperature(current_temperature)
                suntime = data["sys"]
                sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
                sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

                weather_description = data["weather"][0]["description"]
                weather1 = weather(weather_description)
                content = """
        -Thời tiết hôm nay {temperature} có nhiệt độ trung bình là {temp} độ C 
        -Độ ẩm là {humidity}%
        -{weather}
        -Mặt trời mọc vào {hourrise} giờ {minrise} phút
        -Mặt trời lặn vào {hourset} giờ {minset} phút.""".format(hourrise=sunrise.hour, minrise=sunrise.minute,
                                                                weather=weather1, temperature=temperature1,
                                                                hourset=sunset.hour, minset=sunset.minute,
                                                                temp=current_temperature, humidity=current_humidity)
                speak(content)
                time.sleep(21)
            else:
                speak("Không tìm thấy địa chỉ của bạn")
                time.sleep(2)
                current_weather()
def sleep_time(x):
        if x == 1:
            time.sleep(13)
        elif x == 2:
            time.sleep(10)
        elif x == 3:
            time.sleep(7)
        elif x == 4:
            time.sleep(13)
        elif x == 5:
            time.sleep(11)
        elif x == 6:
            time.sleep(11)
        else:
            time.sleep(21)
    
def youtube_search():
        speak('Xin mời bạn chọn tên để tìm kiếm trên youtube')
        time.sleep(3.5)
        text = get_audio()
        plainTextEdit.insertPlainText("You: "+text+"\n")
        if text == "":
            speak("Lỗi tìm kiếm. Do bạn chưa nói tên tìm kiếm.")
            time.sleep(4)
        else:
            search = SearchVideos(text, offset=1, mode="json",
                                max_results=20).result()
            data = json.loads(search)
            url = data["search_result"][0]["link"]
            print(url)
            webbrowser.open(url)
            if "bài hát" in text:
                speak("Bài hát bạn yêu cầu đã được mở.")
            elif "phim" in text:
                speak("Bộ phim bạn yêu cầu đã được mở.")
            else:
                speak("Yêu cầu của bạn đã hoàn thành.")
            time.sleep(7)

def bot():
    r = speech_recognition.Recognizer()
    you = ""
    ai_brain = ""
    plainTextEdit.insertPlainText("AI:  Đang nghe ...\n")
    you = get_audio()
    plainTextEdit.insertPlainText("You: "+you+"\n")
    if "xin chào" in you or "hello" in you:
                hello()
    elif "thời tiết" in you:
                current_weather()
    elif "ngày mấy" in you or "mấy giờ" in you or "thứ mấy" in you:
                get_time(you)
    elif "mở ứng dụng" in you or "mở phần mềm" in you:
                open_application(you)
    elif "mở website" in you:
                open_website(you)
    elif "mở google và tìm kiếm" in you:
                open_google_and_search(you)
    elif "nghe nhạc" in you or "xem phim" in you or "mở youtube" in you or "bài hát" in you:
                youtube_search()
    elif "dừng lại" in you:
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
    elif "hẹn gặp lại" in you or "tạm biệt" in you or "cảm ơn" in you:
                ai_brain = "Rất vui khi giúp đỡ bạn. Hẹn gặp lại bạn sau."
                speak(ai_brain)
                time.sleep(4)
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
                playsound.playsound("Ping.mp3", False)
                time.sleep(1)
                exit()
    else:
                ai_brain = "Tôi không nghe rõ gì cả !!!"
                speak(ai_brain)
                time.sleep(4)

    plainTextEdit.insertPlainText("______________________________")
    you = ""
            
            

                

pushButton.clicked.connect(bot)
plainTextEdit_2 = QtWidgets.QPlainTextEdit(centralwidget)
plainTextEdit_2.setGeometry(QtCore.QRect(0, 680, 461, 61))
font = QtGui.QFont()
font.setPointSize(20)
plainTextEdit_2.setFont(font)
plainTextEdit_2.setObjectName("plainTextEdit_2")
plainTextEdit_2.setPlaceholderText("Ask BOT") 
MainWindow.setCentralWidget(centralwidget)
statusbar = QtWidgets.QStatusBar(MainWindow)
statusbar.setObjectName("statusbar")
MainWindow.setStatusBar(statusbar)
menubar = QtWidgets.QMenuBar(MainWindow)
menubar.setGeometry(QtCore.QRect(0, 0, 563, 27))
menu = QtWidgets.QMenu(menubar)
menu.setObjectName("menu")
menufeatures = QtWidgets.QMenu(menubar)
menufeatures.setObjectName("menufeatures")
menuaudio = QtWidgets.QMenu(menufeatures)
menuaudio.setObjectName("menuaudio")
menucalendar = QtWidgets.QMenu(menufeatures)
menucalendar.setObjectName("menucalendar")
menuhelp = QtWidgets.QMenu(menubar)
menuhelp.setObjectName("menuhelp")
menuFeedback = QtWidgets.QMenu(menubar)
menuFeedback.setObjectName("menuFeedback")
MainWindow.setMenuBar(menubar)
actionSetting = QtWidgets.QAction(MainWindow)
actionSetting.setObjectName("actionSetting")
actionGuide = QtWidgets.QAction(MainWindow)
actionGuide.setObjectName("actionGuide")
actionAbout_Us = QtWidgets.QAction(MainWindow)
actionAbout_Us.setObjectName("actionAbout_Us")
actioninrease = QtWidgets.QAction(MainWindow)
actioninrease.setObjectName("actioninrease")
actionturn_down = QtWidgets.QAction(MainWindow)
actionturn_down.setObjectName("actionturn_down")
actionnow = QtWidgets.QAction(MainWindow)
actionnow.setObjectName("actionnow")
actionopen_calendar = QtWidgets.QAction(MainWindow)
actionopen_calendar.setObjectName("actionopen_calendar")
actiontime = QtWidgets.QAction(MainWindow)
actiontime.setObjectName("actiontime")
actiontranslate = QtWidgets.QAction(MainWindow)
actiontranslate.setObjectName("actiontranslate")
actionCalculator = QtWidgets.QAction(MainWindow)
actionCalculator.setObjectName("actionCalculator")
actionExit = QtWidgets.QAction(MainWindow)
actionExit.setObjectName("actionExit")
actionGuide_2 = QtWidgets.QAction(MainWindow)
actionGuide_2.setObjectName("actionGuide_2")
actionAbout_BOT = QtWidgets.QAction(MainWindow)
actionAbout_BOT.setObjectName("actionAbout_BOT")
menu.addAction(actionSetting)
menu.addSeparator()
menu.addAction(actionAbout_Us)
menu.addSeparator()
menu.addAction(actionExit)
menuaudio.addAction(actioninrease)
menuaudio.addAction(actionturn_down)
menucalendar.addAction(actionnow)
menucalendar.addAction(actionopen_calendar)
menufeatures.addAction(menuaudio.menuAction())
menufeatures.addAction(menucalendar.menuAction())
menufeatures.addAction(actiontime)
menufeatures.addAction(actiontranslate)
menufeatures.addAction(actionCalculator)
menuhelp.addAction(actionGuide_2)
menuhelp.addAction(actionAbout_BOT)
menubar.addAction(menu.menuAction())
menubar.addAction(menufeatures.menuAction())
menubar.addAction(menuFeedback.menuAction())
menubar.addAction(menuhelp.menuAction())
_translate = QtCore.QCoreApplication.translate
MainWindow.setWindowTitle(_translate("MainWindow", "BOT"))
pushButton.setText(_translate("MainWindow", "Micro"))
menu.setTitle(_translate("MainWindow", "..."))
menufeatures.setTitle(_translate("MainWindow", "Features"))
menuaudio.setTitle(_translate("MainWindow", "Audio"))
menucalendar.setTitle(_translate("MainWindow", "Calendar"))
menuhelp.setTitle(_translate("MainWindow", "Help"))
menuFeedback.setTitle(_translate("MainWindow", "Feedback"))
actionSetting.setText(_translate("MainWindow", "Setting"))
actionGuide.setText(_translate("MainWindow", "Guide"))
actionAbout_Us.setText(_translate("MainWindow", "About us"))
actioninrease.setText(_translate("MainWindow", "Turn up"))
actionturn_down.setText(_translate("MainWindow", "Turn down"))
actionnow.setText(_translate("MainWindow", "Now"))
actionopen_calendar.setText(_translate("MainWindow", "Open"))
actiontime.setText(_translate("MainWindow", "Time"))
actiontranslate.setText(_translate("MainWindow", "Translate"))
actionCalculator.setText(_translate("MainWindow", "Calculator"))
actionExit.setText(_translate("MainWindow", "Exit"))
actionGuide_2.setText(_translate("MainWindow", "How to use"))
actionAbout_BOT.setText(_translate("MainWindow", "About BOT"))
QtCore.QMetaObject.connectSlotsByName(MainWindow)  








MainWindow.show()
sys.exit(app.exec_())
