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
root = Tk()
text_area = Text(root, height=26, width=45)
scroll = Scrollbar(root, command=text_area.yview)


def speak(text):
    print("AI:  {}".format(text))
    text_area.insert(INSERT, "AI: "+text+"\n")
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
    image1 = Image.open("image\\hacker1.jpg")
    image_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    day_time = int(strftime('%H'))
    if day_time < 11:
        speak("Chào buổi sáng tốt lành.AI có thể giúp gì được cho bạn.")
    elif 11 <= day_time < 13:
        speak("Chào buổi trưa tốt lành.AI có thể giúp gì được cho bạn.")
    elif 13 <= day_time < 18:
        speak("Chào buổi chiều tốt lành.AI có thể giúp gì được cho bạn.")
    else:
        speak("Chào buổi tối tốt lành.AI có thể giúp gì được cho bạn.")
    root.update()
    time.sleep(5)


def get_time(text):
    image1 = Image.open("image\\thoigian.jpg")
    image_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
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
    root.update()
    time.sleep(5)


def open_application(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
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
    root.update()
    time.sleep(6)


def open_website(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    reg_ex = re.search('mở website (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
    else:
        speak("AI không nghe rõ bạn nói lại được không?.")
    root.update()
    time.sleep(5)


def open_google_and_search(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

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
    root.update()
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

    if "rain" in text:
        image1 = Image.open("image\\thoitiet2.jpg")
        image_1 = ImageTk.PhotoImage(image1)
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
    else:
        image1 = Image.open("image\\thoitiet1.jpg")
        image_1 = ImageTk.PhotoImage(image1)
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

    return temp


def temperature(text):
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
    root.update()
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_audio()
    text_area.insert(INSERT, "You: "+city+"\n")
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
            root.update()
            time.sleep(21)
        else:
            speak("Không tìm thấy địa chỉ của bạn")
            root.update()
            time.sleep(2)
            current_weather()


def week(x):
    switcher = {
        0: 'có môn Lập trình mạng do thầy Mai Văn Hà quản lí..Phòng B3-203. Tiết 2 3 4 .Giờ bắt đầu học 6 giờ.Và có môn Đô án chuyên ngành do cô Vũ Thị Trà quản lí. Tiết 6 7 .Giờ bắt đầu học 13 giờ',
        1: 'có môn Hệ Quản Trị Cơ Sở dữ liệu do cô Phạm Dương Thu Hằng quản lí.Phòng A5-210 . Tiết 6 7 8 9 .Giờ bắt đầu học 13 giờ',
        2: 'có môn Công nghệ phần mềm do cô Lê Thị Thanh Bình quản lí. Tiết 4 5 .Giờ bắt đầu học 10 giờ',
        3: 'bạn được nghỉ. Hãy tranh thủ đi chơi với người yêu đi nha.',
        4: 'có môn Đường lối Đảng Cộng sản Việt Nam do thầy Nguyễn Hải Như quản lí.Phòng B3-302. Tiết 6 7 .Giờ bắt đầu học 13 giờ',
        5: 'có môn An toàn thông tin do thầy Phan Phú Cường quản lí.Phòng B3-403. Tiết 4 5 .Giờ bắt đầu học 10 giờ',
        6: 'có môn Thiết kế website do thầy Nguyễn Thanh Tuấn quản lí.Phòng A5-206. Tiết 1 2 3 .Giờ bắt đầu học 7 giờ',
    }
    return switcher.get(x, "nothing")


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


def subject(text):
    image1 = Image.open("image\\TKB.jpg")
    image_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now1 = datetime.datetime.now().strftime("%w")
    if "hôm nay" in text:
        now2 = int(now1)
        speak("Hôm nay "+week(now2))
        root.update()
        sleep_time(now2)
    elif "ngày mai" in text:
        now2 = int(now1)+1
        if now2 > 6:
            now2 = 0
        speak("Ngày mai "+week(now2))
        root.update()
        sleep_time(now2)


def subject_day(text):
    image1 = Image.open("image\\TKB.jpg")
    image_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "thứ hai" in text:
        speak("Thứ Hai có môn Hệ Quản Trị Cơ Sở dữ liệu do cô Phạm Dương Thu Hằng quản lí.Phòng A5-210 . Tiết 6 7 8 9 .Giờ bắt đầu học 13 giờ")
        root.update()
        sleep_time(1)
    elif "thứ ba" in text:
        speak("Thứ Ba có môn Công nghệ phần mềm do cô Lê Thị Thanh Bình quản lí. Tiết 4 5 .Giờ bắt đầu học 10 giờ")
        root.update()
        sleep_time(2)
    elif "thứ tư" in text:
        speak("Thứ Tư bạn được nghỉ. Hãy tranh thủ đi chơi với người yêu đi nha.")
        root.update()
        sleep_time(3)
    elif "thứ năm" in text:
        speak("Thứ Năm có môn Đường lối Đảng Cộng sản Việt Nam do thầy Nguyễn Hải Như quản lí.Phòng B3-302. Tiết 6 7 .Giờ bắt đầu học 13 giờ")
        root.update()
        sleep_time(4)
    elif "thứ sáu" in text:
        speak("Thứ Sáu có môn An toàn thông tin do thầy Phan Phú Cường quản lí.Phòng B3-403. Tiết 4 5 .Giờ bắt đầu học 10 giờ")
        root.update()
        sleep_time(5)
    elif "thứ bảy" in text:
        speak("Thứ Bảy có môn Thiết kế website do thầy Nguyễn Thanh Tuấn quản lí.Phòng A5-206. Tiết 1 2 3 .Giờ bắt đầu học 7 giờ")
        root.update()
        sleep_time(6)
    elif "chủ nhật" in text:
        speak("Chủ mật có môn Lập trình mạng do thầy Mai Văn Hà quản lí. Tiết 2 3 4 .Phòng B3-203.Giờ bắt đầu học 6 giờ.\n\tVà có môn Đô án chuyên ngành do cô Vũ Thị Trà quản lí. Tiết 6 7 .Giờ bắt đầu học 13 giờ")
        root.update()
        sleep_time(0)


def get_math():
    speak("Bạn nói phép tính đi, AI sẽ giúp bạn.")
    root.update()
    time.sleep(4)
    text1 = get_audio()
    text_area.insert(INSERT, "You: "+text1+"\n")
    root.update()
    image_1 = ImageTk.PhotoImage(Image.open("image\\math.jpg"))
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    if "+" in text1:
        text2 = text1.replace("+", "-")
        try:
            math_a = re.search('(.+) -', text2)
            a = math_a.group(1)
            math_b = re.search('- (.+)', text2)
            b = math_b.group(1)
            c = float(a)+float(b)
            speak("Kết quả phép tính "+a+" cộng "+b+" là: "+str(c))
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "/" in text1 or "chia" in text1:
        text2 = text1.replace("chia", "/")
        try:
            math_a = re.search('(.+) /', text2)
            a = math_a.group(1)
            math_b = re.search('/ (.+)', text2)
            b = math_b.group(1)
            c = float(a)/float(b)
            speak("Kết quả phép tính "+a+" chia "+b+" là: "+str(c))
            root.update()
            time.sleep(3)
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "x" in text1 or "nhân" in text1:
        text2 = text1.replace("nhân", "x")
        try:
            math_a = re.search('(.+) x', text2)
            a = math_a.group(1)
            math_b = re.search('x (.+)', text2)
            b = math_b.group(1)
            c = float(a)*float(b)
            speak("Kết quả phép tính "+a+" nhân "+b+" là: "+str(c))
            time.sleep(2)
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "-" in text1:
        try:
            math_a = re.search('(.+) - ', text1)
            a = math_a.group(1)
            math_b = re.search(' - (.+)', text1)
            b = math_b.group(1)
            c = float(a)-float(b)
            speak("Kết quả phép tính "+a+" trừ "+b+" là: "+str(c))
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    else:
        speak("Phép tính không hợp lệ")
        root.update()

    time.sleep(6)


def youtube_search():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    speak('Xin mời bạn chọn tên để tìm kiếm trên youtube')
    root.update()
    time.sleep(3.5)
    text = get_audio()
    text_area.insert(INSERT, "You: "+text+"\n")
    root.update()
    if text == "":
        speak("Lỗi tìm kiếm. Do bạn chưa nói tên tìm kiếm.")
        root.update()
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


def love_you():
    mylist = ["Thiếu 500 nghìn là em tròn một củ. Thiếu anh nữa là em đủ một đôi.",
              "Đố ai quyét sạch được lá rừng. Đố ai khuyên được em ngừng yêu anh!",
              "Trời không xanh, Mây cũng không trắng, Em không say nắng, Nhưng lại say anh.",
              "Cho em một cốc trà đào, Tiện cho em hỏi lối vào tim anh!",
              "Em đây rất thích đồng hồ, Thích luôn cả việc làm bồ của anh.",
              "Vertor chỉ có một chiều, Em dân chuyên toán chỉ yêu 1 người.",
              "Hoa vô tình bỏ rơi cành lá, Người vô tình bỏ lỡ tơ duyên",
              "Ngoài kia bão táp mưa sa, Bôn ba mệt quá về nhà với em",
              "Trăng kia ai vẽ mà tròn, Lòng anh ai trộm mà hoài nhớ thương",
              "Nhân gian vốn lắm bộn bề. Sao không bỏ hết mà về với em.",
              "Thức khuya em tỉnh bằng trà, yêu anh em trả bằng tình được không?",
              "Suốt bao năm lòng em luôn yên tĩnh. Gặp anh rồi, tĩnh lặng hóa phong ba.",
              "Nắng kia là của ông trời, còn anh đã của ai rồi hay chưa? ",
              "Mây kia là của hạt mưa, anh xem đã thích em chưa hay rồi?",
              "Cánh đồng xanh xanh, làn mây trăng trắng. Tưởng là say nắng ai ngờ say em."]
    love = random.choice(mylist)
    speak(love)
    root.update()
    time.sleep(7)


def func():
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    content = """
    Tôi có những chức năng sau đây:
    1.Chào hỏi
    2.Thông báo thời gian 
    3.Dự báo thời tiết 
    4.Thời khóa biểu
    5.Thực hiện phép tính đơn giản 
    6.Thả thính crush
    7.Mở ứng dụng,mở website 
    8.Tìm kiếm thông tin trên google 
    9.Mở nhạc,phim trên youtube 
    10.Tạm biệt"""
    speak(content)
    root.update()
    time.sleep(23)


def color():
    mylist = ["#009999", "black", "green", "grey",
              "blue", "orange", "#cc0099", "#00ff00", "brown"]
    aa = random.choice(mylist)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here", background=aa)
    root.update()


def color1():
    mylist1 = ["yellow", "#0000ff", "white", "#00ff00", "black"]
    bb = random.choice(mylist1)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here", foreground=bb)
    root.update()


def info():
    mbox.showinfo("Giới thiệu", "-Nhấn Micro để bắt đầu thực hiện nói với AI.\n-Nhấn Làm mới để xóa toàn bộ cuộc trò chuyện.\n-Bạn có thể thay đổi màu nền hoặc màu chữ ngẫu nhiên.\n-Tiếng Pip xuất hiện là lúc AI đang nghe bạn nói.\n-Nói 'dừng lại' để tạm hoãn cuộc trò chuyện. \n-Nhấn Thoát để tắt chương trình.")


def r_set():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    text_area.delete("1.0", "1000000000.0")

def set_volumn(text):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    currentVolume= volume.GetMasterVolumeLevel()
    if "tăng" in text:
        speak("Bạn muốn tăng bao nhiêu")
        vol = get_audio()
        volume.SetMasterVolumeLevel(currentVolume + float(vol), None)
    elif "giảm" in text:
        speak("Bạn muốn giảm bao nhiêu")
        vol = get_audio()
        volume.SetMasterVolumeLevel(currentVolume - float(vol), None)
    
def main():
    r = speech_recognition.Recognizer()
    you = ""
    ai_brain = ""
    while True:
        with speech_recognition.Microphone() as source:
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            print("AI:  Dang nghe ...")
            audio = r.listen(source, phrase_time_limit=6)
            print("AI:  ...")
        try:
            you = r.recognize_google(audio, language="vi-VN")
            print("\nYou: " + you)
            you = you.lower()
        except:
            ai_brain = "Tôi nghe không rõ. Bạn nói lại được không"
            print("\nAI: " + ai_brain)

        text_area.insert(INSERT, "You: "+you+"\n")
        root.update()
        
        if "xin chào" in you or "hello" in you:
            hello()
        elif "thời tiết" in you:
            current_weather()
        elif "ngày mấy" in you or "mấy giờ" in you or "thứ mấy" in you:
            get_time(you)
        elif "phép tính" in you or "tính toán" in you:
            get_math()
        elif "mở ứng dụng" in you or "mở phần mềm" in you:
            open_application(you)
        elif "mở website" in you:
            open_website(you)
        elif "mở google và tìm kiếm" in you:
            open_google_and_search(you)
        elif ("hôm nay" in you and "môn" in you) or ("ngày mai" in you and "môn" in you):
            subject(you)
        elif ("thứ" in you and "môn" in you) or ("chủ nhật" in you and "môn" in you):
            subject_day(you)
        elif "nghe nhạc" in you or "xem phim" in you or "mở youtube" in you or "bài hát" in you:
            youtube_search()
        elif "thả thính" in you or "bạn thích tôi à" in you:
            love_you()
        elif "bạn có" in you and "chức năng" in you:
            func()
        elif "đổi màu nền" in you:
            color()
        elif "đổi màu chữ" in you:
            color1()
        elif "âm lượng" in you:
            set_volumn(you)
        elif "dừng lại" in you:
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            break
        elif "hẹn gặp lại" in you or "tạm biệt" in you or "cảm ơn" in you:
            ai_brain = "Rất vui khi giúp đỡ bạn. Hẹn gặp lại bạn sau."
            speak(ai_brain)
            root.update()
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
            root.update()
            time.sleep(4)

        text_area.insert(
            INSERT, "_____________________________________________")
        you = ""

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Trợ lí ảo")
        self.style = Style()
        self.style.theme_use("default")

        scroll.pack(side=RIGHT, fill=Y)
        text_area.configure(yscrollcommand=scroll.set)
        text_area.pack(side=RIGHT)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        image3 = Image.open("image\\micro.png")
        image_3 = ImageTk.PhotoImage(image3)
        label = Label(image=image_3)
        label.image = image_3
        label.place(x=540, y=475)

        closeButton = Button(self, text="Thoát", command=exit,
                             width=10, fg="white", bg="#009999", bd=3)
        closeButton.pack(side=RIGHT, padx=11, pady=10)
        okButton = Button(self, text="Micro", command=main,
                          width=10, fg="white", bg="#009999", bd=3)
        okButton.pack(side=RIGHT, padx=11, pady=10)
        doimau = Button(self, text="Đổi màu nền", command=color,
                        width=10, fg="white", bg="#009999", bd=3)
        doimau.pack(side=RIGHT, padx=11, pady=10)
        doimau = Button(self, text="Đổi màu chữ", command=color1,
                        width=10, fg="white", bg="#009999", bd=3)
        doimau.pack(side=RIGHT, padx=11, pady=10)
        thongtin = Button(self, text="Giới thiệu", command=info,
                          width=10, fg="white", bg="#009999", bd=3)
        thongtin.pack(side=RIGHT, padx=11, pady=10)
        lammoi = Button(self, text="Làm mới", command=r_set,
                        width=10, fg="white", bg="#009999", bd=3)
        lammoi.pack(side=RIGHT, padx=11, pady=10)

        # self.pack(fill=BOTH, expand=1)
        # Style().configure("TFrame", background="#333")

        image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))
        label1 = Label(self, image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

        l = Label(root, text='Lịch sử trò chuyện', fg='White', bg='blue')
        l.place(x=850, y=10, width=120, height=25)
        l1 = Label(root, text='THNH', fg='yellow', bg='black')
        l1.place(x=250, y=11, width=120, height=25)


root.geometry("1100x510+350+50")
root.resizable(False, False)
app = App(root)
root.mainloop()

# http://api.openweathermap.org/data/2.5/weather?appid=b0d4f9bfd2bbc40d10976e6fd3ea7514&q=da%20nang&units=metric
