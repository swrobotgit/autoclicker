# игра волк ловит яйца https://yandex.ru/games/app/233425
# координаты определяем тут по принскрину https://programminghead.com/Projects/find-coordinates-of-image-online.html
from tkinter import *
import numpy as np
import pyautogui
from PIL import ImageGrab

# Создаем окно
window = Tk()
window.title('SW Autoclicker')
window.geometry('100x50')  # Устанавливаем размер окна 300x50 пикселей
window.wm_attributes('-topmost', True) #Задаем атрибут Поверх всех окон

# координаты кнопок по которым надо нажимать 248,715,250,853,1459,707,1465,848
btn1_click = [248,715]
btn2_click = [250,853]
btn3_click = [1459,707]
btn4_click = [1465,848]
# координаты падающих яйц за 1 шаг до падения пример https://disk.yandex.ru/i/4CSkPZlFtr16Ng
# 606,513,608,646,1109,513,1109,645
egg1_detect =[606,513]
egg2_detect =[608,646]
egg3_detect =[1109,513]
egg4_detect =[1109,645]

running = False
status = 0
def click_btn():
    global status
    if status ==0:
        status = 1
        button['text'] = 'Stop'
        button['fg'] = 'red'
        window.update()
        while status==1:
            window.update()
            # Захват скриншота всего экрана
            # документация по созданию Pillow принтскрина https://docs-python.ru/packages/biblioteka-pillow-python/sozdanie-skrinshota/
            screenshot = ImageGrab.grab(bbox=None,
                            include_layered_windows=False,
                            all_screens=False, xdisplay=None)
            screenshot = np.array(screenshot)
            # print(screenshot)
            # Чтение цветов пикселей по заданным координатам
            egg1_color = screenshot[egg1_detect[1], egg1_detect[0]]
            egg2_color = screenshot[egg2_detect[1], egg2_detect[0]]
            egg3_color = screenshot[egg3_detect[1], egg3_detect[0]]
            egg4_color = screenshot[egg4_detect[1], egg4_detect[0]]
            # если значение любого канала цвета ниже 100 значит это тёмный цвет, вывод катится яичко.
            if egg1_color[0] < 100:
                pyautogui.moveTo(btn1_click) # перемещаем курсор
                pyautogui.doubleClick(btn1_click) # кликаем по координате
            elif egg2_color[0] < 100:
                pyautogui.moveTo(btn2_click)
                pyautogui.doubleClick(btn2_click)
            elif egg3_color[0] < 100:
                pyautogui.moveTo(btn3_click)
                pyautogui.doubleClick(btn3_click)
            elif egg4_color[0] < 100:
                pyautogui.moveTo(btn4_click)
                pyautogui.doubleClick(btn4_click)

    elif status ==1:
        status = 0
        button['text'] = 'Start'
        button['fg'] = 'green'
        window.update()



# Создаем кнопку Start/Stop
button = Button(window, text='Start', fg='green', command=click_btn)
button.grid(row=0, column=0)

window.mainloop()




