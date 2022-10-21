from sound_audio import sound_audio as sa
from times import times
from google import google
from youtube import youtube
from search_wikipedia import wikipedia 
from software import software
from gmail import email
from weather import weather
from bot import bot
# from news import news 

def assistant():
    sa.speak("Xin chào, bạn tên là gì nhỉ?")
    name = "Thanh"
    if name:
        sa.speak("Chào bạn {}".format(name))
        sa.speak("Bạn cần Bot Alex có thể giúp gì ạ?")
        while True:
            text = sa.get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                bot.stop()
                break
            elif "có thể làm gì" in text:
                bot.help_me()
            elif "chào trợ lý ảo" in text:
                bot.hello(name)
            elif "hiện tại" in text:
                times.get_time(text)
            elif "mở" in text:
                if 'tìm kiếm' or 'tìm' or 'kiếm' in text:
                    google.open_google_and_search(text)
                elif "." in text:
                    google.open_website(text)
                else:
                    software.open_application(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                email.send_email(text)
            elif "thời tiết" in text:
                weather.current_weather()
            elif "chơi nhạc" in text:
                youtube.play_song()
            # elif "hình nền" in text:
            #     change_wallpaper()
            #elif "đọc báo" in text:
                # news.read_news()
            elif "định nghĩa" in text:
                wikipedia.tell_me_about()
            else:
                sa.speak("Bạn cần Bot giúp gì ạ?"  )

assistant()