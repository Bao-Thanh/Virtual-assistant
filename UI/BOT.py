# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BOT.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pickle
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
import wikipedia
import matplotlib.pyplot as plt
from UrlFeaturizer import UrlFeaturizer
wikipedia.set_lang('vi')
language = 'vi'
from time import gmtime, strftime
from googletrans import Translator, constants
import open_app as apps
import joblib
import hinh
from nhom_ui import *
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
import pandas as pd
import cv2
import imutils
        
path = ChromeDriverManager().install()

def word(password):
    character=[]
    for i in password:
        character.append(i)
    return character
    
class Ui_MainWindow(object):
    def nhom(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()
    def feedback(self):
        url = 'mailto:19110019@student.hcmute.edu.vn?subject=Feedback'
        webbrowser.open(url)
    def about_bot(self):
        url = 'https://github.com/Bao-Thanh/Virtual-assistant'
        webbrowser.open(url)      
    def time(self):
        now = datetime.datetime.now()
        self.speak('Bây giờ là %d giờ %d phút %d giây ngày %d tháng %d năm %d' %
                (now.hour, now.minute, now.second, now.day, now.month, now.year))
        self.plainTextEdit.insertPlainText("______________________________\n")
    def translate(self):      
        text = self.lineEdit.text()
        if text == "":
            self.speak('Hãy nhập nội dung cần dịch')
            self.lineEdit.setFocus()
            self.plainTextEdit.insertPlainText("______________________________\n")
        else:
            translator = Translator()
            translation = translator.translate(text)
            self.plainTextEdit.insertPlainText("You: " + text + "\n")
            self.speak(translation.text)
            self.plainTextEdit.insertPlainText("______________________________\n")
            self.lineEdit.clear()
    def calendar(self):
        apps.open_app('Calendar')
    def calculator(self):
        apps.open_app('Calculator')
    def setting(self):
        apps.open_app('Setting')
    def learn_English(self):
        url = 'https://www.tienganh123.com'
        webbrowser.open(url) 
    def math_formulas(self):
        url = 'https://www.cuemath.com/math-formulas'
        webbrowser.open(url)
    def Check_URL(self):
        order = ['bodyLength', 'bscr', 'dse', 'dsr', 'entropy', 'hasHttp', 'hasHttps',
       'has_ip', 'numDigits', 'numImages', 'numLinks', 'numParams',
       'numTitles', 'num_%20', 'num_@', 'sbr', 'scriptLength', 'specialChars',
       'sscr', 'urlIsLive', 'urlLength']
        url = self.lineEdit.text()
        if url == "":
            self.speak('Hãy nhập URL để kiểm tra')
            self.lineEdit.setFocus()
            self.plainTextEdit.insertPlainText("______________________________\n")
        else:
            a = UrlFeaturizer(url).run()
            test = []
            for i in order:
                test.append(a[i])
            encoder = LabelEncoder()
            encoder.classes_ = np.load('models/NN_lblenc.npy',allow_pickle=True)
            scalerfile = 'models/NN_scaler.sav'
            scaler = pickle.load(open(scalerfile, 'rb'))
            model = load_model("models/NN.h5")#
            test = pd.DataFrame(test).replace(True,1).replace(False,0).to_numpy().reshape(1,-1)
            predicted = np.argmax(model.predict(scaler.transform(test)),axis=1)
            self.plainTextEdit.insertPlainText(url + " là trang web " + encoder.inverse_transform(predicted)[0] + "\n")
            self.plainTextEdit.insertPlainText("______________________________\n")
    def check_pass(self):
        password = self.lineEdit.text()
        if password == "":
            self.speak('Hãy nhập password để kiểm tra')
            self.lineEdit.setFocus()
            self.plainTextEdit.insertPlainText("______________________________\n")
        else:
            model = pickle.load(open('models/RandomForestClassifier.pkl', 'rb'))
            tf = pickle.load(open('models/tdif.pkl', 'rb'))
            test = tf.transform([password]).toarray()
            output = model.predict(test)
            self.plainTextEdit.insertPlainText(str('Password: ' + password + ' có độ bảo mật ' + output) + '\n')
            self.plainTextEdit.insertPlainText("______________________________\n")
    def sort_contours(self, cnts, method="left-to-right"):
        reverse = False
        i = 0
        if method == "right-to-left" or method == "bottom-to-top":
            reverse = True
        if method == "top-to-bottom" or method == "bottom-to-top":
            i = 1
        boundingBoxes = [cv2.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
        key=lambda b:b[1][i], reverse=reverse))
        # return the list of sorted contours and bounding boxes
        return (cnts, boundingBoxes)
    def get_letters(self, img):
        letters = []
        image = cv2.imread(img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret,thresh1 = cv2.threshold(gray ,127,255,cv2.THRESH_BINARY_INV)
        dilated = cv2.dilate(thresh1, None, iterations=2)

        cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = self.sort_contours(cnts, method="left-to-right")[0]
        # loop over the contours
        for c in cnts:
            if cv2.contourArea(c) > 10:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = gray[y:y + h, x:x + w]
            thresh = cv2.threshold(roi, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            thresh = cv2.resize(thresh, (32, 32), interpolation = cv2.INTER_CUBIC)
            thresh = thresh.astype("float32") / 255.0
            thresh = np.expand_dims(thresh, axis=-1)
            thresh = thresh.reshape(1,32,32,1)
            model = load_model("models/Sequential.h5")
            LB = pickle.load(open('models/lb.pkl', 'rb'))
            ypred = model.predict(thresh)
            ypred = LB.inverse_transform(ypred)
            [x] = ypred
            letters.append(x)
        return letters, image

    def get_word(self, letter):
        word = "".join(letter)
        return word

    def image_to_text(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        pixmap.save('Test\\test.png', "PNG")
        letter,image = self.get_letters("Test/test.png")
        word = self.get_word(letter)
        self.plainTextEdit.insertPlainText(word + "\n")
        self.plainTextEdit.insertPlainText("______________________________\n")
        # print(word)
        # plt.imshow(image)
    def audio_book(self):
        import pyttsx3
        import PyPDF2
        path, _ = QFileDialog.getOpenFileName()
        sach = open(path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(sach)
        pages = pdfReader.numPages

        bot = pyttsx3.init()
        voices = bot.getProperty('voices')
        bot.setProperty('voice', voices[1].id)

        for num in range(8, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            print(text)
            bot.say(text)
            bot.runAndWait()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 10, 561, 661))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 680, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.voice)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 680, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Ask BOT")
        self.lineEdit.returnPressed.connect(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menufeatures = QtWidgets.QMenu(self.menubar)
        self.menufeatures.setObjectName("menufeatures")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuFeedback = QtWidgets.QMenu(self.menubar)
        self.menuFeedback.setObjectName("menuFeedback")
        self.menuFeedback.aboutToShow.connect(self.feedback)
        self.menu_V = QtWidgets.QMenu(self.menubar)
        self.menu_V.setObjectName("menu_V")
        self.menu_V.aboutToShow.connect(self.turn_up)
        self.menu_V_2 = QtWidgets.QMenu(self.menubar)
        self.menu_V_2.setObjectName("menu_V_2")
        self.menu_V_2.aboutToShow.connect(self.turn_down)
        self.menuCalender = QtWidgets.QMenu(self.menubar)
        self.menuCalender.setObjectName("menuCalender")
        self.menuCalender.aboutToShow.connect(self.calendar)
        self.menuTime = QtWidgets.QMenu(self.menubar)
        self.menuTime.aboutToShow.connect(self.time)
        self.menuTime.setObjectName("menuTime")
        MainWindow.setMenuBar(self.menubar)
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionSetting.triggered.connect(self.setting)
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionAbout_Us.triggered.connect(self.nhom)
        self.actionturn_up = QtWidgets.QAction(MainWindow)
        self.actionturn_up.setObjectName("actionturn_up")
        self.actionturn_down = QtWidgets.QAction(MainWindow)
        self.actionturn_down.setObjectName("actionturn_down")
        self.actionnow = QtWidgets.QAction(MainWindow)
        self.actionnow.setObjectName("actionnow")
        self.actionopen_calendar = QtWidgets.QAction(MainWindow)
        self.actionopen_calendar.setObjectName("actionopen_calendar")
        self.actiontime = QtWidgets.QAction(MainWindow)
        self.actiontime.setObjectName("actiontime")
        self.actiontranslate = QtWidgets.QAction(MainWindow)
        self.actiontranslate.setObjectName("actiontranslate")
        self.actiontranslate.triggered.connect(self.translate)
        self.actionCalculator = QtWidgets.QAction(MainWindow)
        self.actionCalculator.setObjectName("actionCalculator")
        self.actionCalculator.triggered.connect(self.calculator)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(QCoreApplication.instance().quit)
        self.menuAbout_BOT = QtWidgets.QMenu(self.menubar)
        self.menuAbout_BOT.setObjectName("menuAbout_BOT")
        self.menuAbout_BOT.aboutToShow.connect(self.about_bot)
        self.actionLearn_English = QtWidgets.QAction(MainWindow)
        self.actionLearn_English.setObjectName("actionLearn_English")
        self.actionLearn_English.triggered.connect(self.learn_English)
        self.actionMath_Formulas = QtWidgets.QAction(MainWindow)
        self.actionMath_Formulas.setObjectName("actionMath_Formulas")
        self.actionMath_Formulas.triggered.connect(self.math_formulas)
        self.menuSecurity = QtWidgets.QMenu(self.menufeatures)
        self.menuSecurity.setObjectName("menuSecurity")
        self.actionImg_toText = QtWidgets.QAction(MainWindow)
        self.actionImg_toText.setObjectName("actionImg_toText")
        self.actionImg_toText.triggered.connect(self.image_to_text)
        self.actionAudio_Book = QtWidgets.QAction(MainWindow)
        self.actionAudio_Book.setObjectName("actionAudio_Book")
        self.actionAudio_Book.triggered.connect(self.audio_book)
        self.actionCheck_URL = QtWidgets.QAction(MainWindow)
        self.actionCheck_URL.setObjectName("actionCheck_URL")
        self.actionCheck_URL.triggered.connect(self.Check_URL)
        self.actionCheck_Password = QtWidgets.QAction(MainWindow)
        self.actionCheck_Password.setObjectName("actionCheck_Password")
        self.actionCheck_Password.triggered.connect(self.check_pass)
        self.menu.addAction(self.actionSetting)
        self.menu.addSeparator()
        self.menu.addAction(self.actionAbout_Us)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menuSecurity.addAction(self.actionCheck_URL)
        self.menuSecurity.addAction(self.actionCheck_Password)
        self.menufeatures.addAction(self.actiontranslate)
        self.menufeatures.addAction(self.actionCalculator)
        self.menufeatures.addAction(self.actionLearn_English)
        self.menufeatures.addAction(self.actionMath_Formulas)
        self.menufeatures.addAction(self.menuSecurity.menuAction())
        self.menufeatures.addAction(self.actionImg_toText)
        self.menufeatures.addAction(self.actionAudio_Book)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menufeatures.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.menubar.addAction(self.menu_V_2.menuAction())
        self.menubar.addAction(self.menuCalender.menuAction())
        self.menubar.addAction(self.menuTime.menuAction())
        self.menubar.addAction(self.menuFeedback.menuAction())
        self.menubar.addAction(self.menuAbout_BOT.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOT"))
        self.pushButton.setText(_translate("MainWindow", "Micro"))
        self.menu.setTitle(_translate("MainWindow", "..."))
        self.menufeatures.setTitle(_translate("MainWindow", "Features"))
        self.menuSecurity.setTitle(_translate("MainWindow", "Security"))
        self.menuFeedback.setTitle(_translate("MainWindow", "Feedback"))
        self.menu_V.setTitle(_translate("MainWindow", "+V"))
        self.menu_V_2.setTitle(_translate("MainWindow", "-V"))
        self.menuCalender.setTitle(_translate("MainWindow", "Calender"))
        self.menuTime.setTitle(_translate("MainWindow", "Time"))
        self.menuAbout_BOT.setTitle(_translate("MainWindow", "About BOT"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About us"))
        self.actionturn_up.setText(_translate("MainWindow", "Turn up"))
        self.actionturn_down.setText(_translate("MainWindow", "Turn down"))
        self.actionnow.setText(_translate("MainWindow", "Now"))
        self.actionopen_calendar.setText(_translate("MainWindow", "Open"))
        self.actiontime.setText(_translate("MainWindow", "Time"))
        self.actiontranslate.setText(_translate("MainWindow", "Translate"))
        self.actionCalculator.setText(_translate("MainWindow", "Calculator"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLearn_English.setText(_translate("MainWindow", "Learn English"))
        self.actionMath_Formulas.setText(_translate("MainWindow", "Math Formulas"))
        self.actionImg_toText.setText(_translate("MainWindow", "Image to Text"))
        self.actionAudio_Book.setText(_translate("MainWindow", "Audio Book"))
        self.actionCheck_URL.setText(_translate("MainWindow", "Check URL"))
        self.actionCheck_Password.setText(_translate("MainWindow", "Check Password"))
    
    def turn_up(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolume = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolume + 1, None)
    
    def turn_down(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolume = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolume - 1, None)
    
    def speak(self, text):
        print("AI:  {}".format(text))
        self.plainTextEdit.insertPlainText("AI: "+text+"\n")
        tts = gTTS(text=text, lang='vi', slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", False)
        os.remove("sound.mp3")
    def get_audio(self):
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
    def hello(self):
        day_time = int(strftime('%H'))
        if day_time < 11:
            self.speak("Chào buổi sáng tốt lành.AI có thể giúp gì được cho bạn.")
        elif 11 <= day_time < 13:
            self.speak("Chào buổi trưa tốt lành.AI có thể giúp gì được cho bạn.")
        elif 13 <= day_time < 18:
            self.speak("Chào buổi chiều tốt lành.AI có thể giúp gì được cho bạn.")
        else:
            self.speak("Chào buổi tối tốt lành.AI có thể giúp gì được cho bạn.")
        time.sleep(5)
    def get_time(self, text):
        now = datetime.datetime.now()
        now1 = datetime.datetime.now().strftime("%w")
        now2 = int(now1)
        now3 = "Chủ Nhật"
        if "giờ" in text:
            self.speak('Bây giờ là %d giờ %d phút %d giây' %
                (now.hour, now.minute, now.second))
        elif "ngày" in text:
            self.speak("Hôm nay là ngày %d tháng %d năm %d" %
                (now.day, now.month, now.year))
        elif "thứ" in text and now2 != 0:
            self.speak('Hôm nay là thứ %s' % (now2+1))
        elif "thứ" in text and now2 == 0:
            self.speak('Hôm nay là %s' % (now3))
        else:
            self.speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
            time.sleep(6)
        time.sleep(5)
    def open_application(self, text):
        if "mở ứng dụng" in text or "mở phần mềm" in text:
            text = text[12:]
        elif "mở" in text:
            text = text[3:] 
        if "cốc cốc" in text:
            apps.open_app('C?C C?C')
            self.speak("Cốc Cốc được mở")
        else:
            flag = 0
            text = text.lower()
            list_app = apps.get_apps().keys()
            for ap in list_app:
                if text in str(ap).lower():
                    flag = 1
                    apps.open_app(ap) 
            if (flag):       
                self.speak(text + " được mở")
            else:
                self.speak(text + " chưa được cài đặt trong máy của bạn")
                url = 'https://www.google.com/search?query=tải ' + text
                webbrowser.open(url) 
            time.sleep(6)
         
        
    def open_website(self, text):
        reg_ex = re.search('mở website (.+)', text)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            self.speak("Trang web bạn yêu cầu đã được mở.")
        else:
            self.speak("AI không nghe rõ bạn nói lại được không?.")
        time.sleep(5)
        
    def tell_me_about(self, text):
        try:
            text = text[:-5]
            contents = wikipedia.summary(text).split('\n')
            self.speak(contents[0])
        except:
            self.speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")   
        
    def open_google_and_search(self, text):
        search_for = text.split("tìm", 1)[1]
        self.speak('AI đang tìm kiếm giúp bạn')
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.google.com")
        que = driver.find_element("xpath", "//input[@name='q']")
        que.send_keys(str(search_for))
        que.send_keys(Keys.RETURN)
        time.sleep(6)
        
    def weather(self, text):
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

    def current_weather(self):
        self.speak("Bạn muốn xem thời tiết ở đâu vậy.")
        time.sleep(3)
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = self.get_audio()
        self.plainTextEdit.insertPlainText("You: "+city+"\n")
        if city == "":
            self.current_weather()
        else:
            api_key = "b0d4f9bfd2bbc40d10976e6fd3ea7514"
            call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
            response = requests.get(call_url)
            data = response.json()
            if data["cod"] != "404":
                city_res = data["main"]
                current_humidity = city_res["humidity"]
                current_temperature = city_res["temp"]
                temperature1 = self.temperature(current_temperature)
                suntime = data["sys"]
                sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
                sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

                weather_description = data["weather"][0]["description"]
                weather1 = self.weather(weather_description)
                content = """
        -Thời tiết hôm nay {temperature} có nhiệt độ trung bình là {temp} độ C 
        -Độ ẩm là {humidity}%
        -{weather}
        -Mặt trời mọc vào {hourrise} giờ {minrise} phút
        -Mặt trời lặn vào {hourset} giờ {minset} phút.""".format(hourrise=sunrise.hour, minrise=sunrise.minute,
                                                                weather=weather1, temperature=temperature1,
                                                                hourset=sunset.hour, minset=sunset.minute,
                                                                temp=current_temperature, humidity=current_humidity)
                self.speak(content)
                time.sleep(21)
            else:
                self.speak("Không tìm thấy địa chỉ của bạn")
                time.sleep(2)
                self.current_weather()

    def youtube_search(self):
        self.speak('Xin mời bạn chọn tên để tìm kiếm trên youtube')
        time.sleep(3.5)
        text = self.get_audio()
        self.plainTextEdit.insertPlainText("You: "+text+"\n")
        if text == "":
            self.speak("Lỗi tìm kiếm. Do bạn chưa nói tên tìm kiếm.")
            time.sleep(4)
        else:
            search = SearchVideos(text, offset=1, mode="json",
                                max_results=20).result()
            data = json.loads(search)
            url = data["search_result"][0]["link"]
            print(url)
            webbrowser.open(url)
            if "bài hát" in text:
                self.speak("Bài hát bạn yêu cầu đã được mở.")
            elif "phim" in text:
                self.speak("Bộ phim bạn yêu cầu đã được mở.")
            else:
                self.speak("Yêu cầu của bạn đã hoàn thành.")
            time.sleep(7)
    def voice(self):
            you = ""
            ai_brain = ""
            you = self.get_audio()
            self.plainTextEdit.insertPlainText("You: "+you+"\n")
            if "xin chào" in you or "hello" in you:
                self.hello()
            elif "thời tiết" in you:
                self.current_weather()
            elif "ngày mấy" in you or "mấy giờ" in you or "thứ mấy" in you:
                self.get_time(you)
            elif "mở ứng dụng" in you or "mở phần mềm" in you or "mở" in you and "website" not in you:
                self.open_application(you)
            elif "mở website" in you:
                self.open_website(you)
            elif "tìm" in you:
                self.open_google_and_search(you)
            elif "nghe nhạc" in you or "xem phim" in you or "mở youtube" in you or "bài hát" in you:
                self.youtube_search()
            elif "là gì" in you or "là ai" in you:
                self.tell_me_about(you)
            elif "dừng lại" in you:
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
            elif "hẹn gặp lại" in you or "tạm biệt" in you or "cảm ơn" in you or "thoát" in you:
                ai_brain = "Rất vui khi giúp đỡ bạn. Hẹn gặp lại bạn sau."
                self.speak(ai_brain)
                time.sleep(4)
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
                playsound.playsound("Ping.mp3", False)
                time.sleep(0.5)
                playsound.playsound("Ping.mp3", False)
                time.sleep(1)
                exit()
            else:
                ai_brain = "Xin lỗi tôi không thể giúp được yêu cầu của bạn"
                self.speak(ai_brain)
                # notFound="<a href=\"http://www.google.com/search?q= " + you + "\">'Tìm kiếm " + you + "'</a>" 
                # self.plainTextEdit.insertPlainText(notFound)
                time.sleep(4)
            self.plainTextEdit.insertPlainText("______________________________\n")
            you = ""
    def textEdit(self):
        you = ""
        ai_brain = ""
        you = self.lineEdit.text()
        self.lineEdit.clear()   
        self.plainTextEdit.insertPlainText("You: "+you+"\n")
        if "xin chào" in you or "hello" in you:
            self.hello()
        elif "thời tiết" in you:
            self.current_weather()
        elif "ngày mấy" in you or "mấy giờ" in you or "thứ mấy" in you:
            self.get_time(you)
        elif "mở ứng dụng" in you or "mở phần mềm" in you or "mở" in you and "website" not in you:
            self.open_application(you)
        elif "mở website" in you:
            self.open_website(you)
        elif "tìm" in you: 
            self.open_google_and_search(you)
        elif "nghe nhạc" in you or "xem phim" in you or "mở youtube" in you or "bài hát" in you:
            self.youtube_search()
        elif "là gì" in you or "là ai" in you:
            self.tell_me_about(you)
        elif "dừng lại" in you:
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
        elif "hẹn gặp lại" in you or "tạm biệt" in you or "cảm ơn" in you or "thoát" in you:
            ai_brain = "Rất vui khi giúp đỡ bạn. Hẹn gặp lại bạn sau."
            self.speak(ai_brain)
            time.sleep(4)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            exit()
        else:
            ai_brain = "Xin lỗi tôi không thể giúp được yêu cầu của bạn"
            self.speak(ai_brain)
            # notFound="<a href=\"http://www.google.com/search?q= " + you + "\">'Tìm kiếm " + you + "'</a>" 
            # self.plainTextEdit.append(notFound)
            time.sleep(4)
        self.plainTextEdit.insertPlainText("______________________________\n")
        you = ""
 
        
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
