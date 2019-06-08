from pynput import keyboard
from speechToText import speechToText
from selenium import webdriver
import threading

driver = webdriver.Chrome()


# def reset_stream():
#     """
#     :return:
#     """
#     p = pa.PyAudio()
#
#     stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)
#
#    # t = Timer(10.0, reset_stream)
#     with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#     print("reset")

# keyword: rock
    # go to rock website, click play now


def rock_play():
    """
    :return:
    """
    #k.stop()
    driver.get("https://www.youtube.com/watch?v=EJaG-ywgHvY")

# keyword: npr
    # go to NPR website and click play


def npr_play():
    """
    :return:
    """
    #k.stop()
    driver.get("https://audio.wbhm.org:8443/live.mp3?ck=1559509996532")

# keyword: off
    # closes out website


def best_play():
    """
    :return:
    """
    driver.get("https://youtu.be/0wlVToO92bk?t=52")


def off():
    """
    :return:
    """
    driver.get("https://www.google.com")


def on_press(key):
    """
    :param key:
    :return:
    """
    if key == keyboard.Key.space:
        s = speechToText()
        txt = s.listen()
        keyword = s.check_command(txt)
        if keyword == "rock":
            keyboard.Listener.stop(k)
            x = threading.Thread(rock_play())
            x.start()
            # k.stop()
            # rock_play()
        elif keyword == "npr" or keyword == "NPR":
            keyboard.Listener.stop(k)
            x = threading.Thread(npr_play())
            x.start()
            # k.stop()
            # npr_play()
        elif keyword == "Best" or keyword == "best":
            keyboard.Listener.stop(k)
            x = threading.Thread(best_play())
            x.start()
            # k.stop()
            # best_play()
        elif keyword == "off":
            keyboard.Listener.stop(k)
            x = threading.Thread(off())
            x.start()
            # k.stop()
            # off()

# t = Timer(10.0, reset_stream)
while True:
    k = keyboard.Listener(on_press=on_press)
    k.start()
    # time.sleep(15)
    k.join()
    # k.stop()
    print("reset")
