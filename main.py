from tkinter import *
from tkinter import ttk
import cv2
#import hikvisionapi

# TODO 1. Нужно сделать счетчик фото, который обновляется ежедневно после 00:00
# TODO 2. Реализовать выбор папки сохранения сделанных фото через GUI
# TODO 3. Исправить по возможности визуальную составляющую: установить положение окна по умолчанию по центру экрана
# + размер под экран
# TODO 4. Реализовать поиск и подключение к определенной камере (у меня будет hikvision) - под нее есть API библ выше
# TODO 5.Правильно скомпоновать проект и сделать установочный exe файл

def click_button():
    global cap
    global id
    ret, frame = cap.read()
    cv2.imwrite(f'photo{id}.jpeg', frame)
    id = id + 1;

def connect():
    global  connected
    global  cap
    cap = cv2.VideoCapture(0)
    connected = cap.isOpened()
    update()

def update():
    if connected:
        btn.state(["!disabled"])
        text.insert(1.0, "Connection enabled")
        text.pack()
        btn.pack()
    else:
        #todo find text.clera
        text.insert(1.0, "Connection lost")
        text.pack()
        btn.pack()

id = 0
cap = None;
root = Tk()
root.title("Снимок для камеры Hiwatch")
root.geometry("500x250")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

connected = False

#if connected:
#    btn = ttk.Button(text="Сделать снимок", state="enabled", command=click_button)
#    text = Text(width=20, height=3, bg="white", fg='black', wrap=WORD)
#    text.insert(1.0, "Connection enabled")
#    text.pack()
#    btn.pack()

btn = ttk.Button(text="Сделать снимок", state="disabled", command=click_button)
text = Text(width=20, height=3, bg="white", fg='black', wrap=WORD)
text.insert(1.0, "Пожалуйста, подключите камеру")
text.pack()
btn.pack()

btn_connect = ttk.Button(text="Установить соединение с камерой", state="enabled", command=connect)
btn_connect.pack()

root.mainloop()

cap.release() # disconect cam