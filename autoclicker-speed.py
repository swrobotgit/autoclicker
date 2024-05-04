from tkinter import *
import pyautogui
import time

# Создаем окно
window = Tk()
window.title('SW Autoclicker')
window.geometry('300x100')  # Устанавливаем размер окна 300x50 пикселей
window.wm_attributes('-topmost', True)

status = 0
speed_click = 1
# Функция для автоклика
def click_start():
    global  status
    status = 1
    label_status['text'] = 'работает'
    label_status['fg'] = 'green'
    pyautogui.moveTo((100, 100))  # Перемещаем курсор мыши в стартовую позицию позицию (100, 100)

    # цикл работает пока tatus равен состоянию 1
    while status == 1:
        #pyautogui.tripleClick()  # Выполняем тройной клик мышью
        pyautogui.doubleClick() # Выполняем тройной клик мышью
        window.update()  # Обновляем окно
        time.sleep(speed_click)  # Ждем N-секунд
        print(speed_click)

def click_stop():
    global status
    status = 0
    label_status['text'] = 'не работает'
    label_status['fg'] = 'red'

def speed_update():
    global speed_click
    speed_click =int(ent.get())

# Создаем кнопку Start
button = Button(window, text='Start', command=click_start)
button.grid(row=0, column=0)

# Создаем кнопку Start
button = Button(window, text='Stop', command=click_stop)
button.grid(row=0, column=2)

Label(window, text='Статус:').grid(row=1, column=0)
label_status =Label(window, text='не работает', fg='red')
label_status.grid(row=1, column=1)

Label(window, text='Устновить скорость, сек:').grid(row=2, column=0, columnspan=3)
ent = Entry(window)
ent.grid(row=3, column=0, columnspan=2)
button = Button(window, text='up', command=speed_update)
button.grid(row=3, column=2)

window.mainloop()
