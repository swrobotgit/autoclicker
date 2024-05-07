# игра волк ловит яйца https://yandex.ru/games/app/233425
# координаты определяем тут по принскрину https://programminghead.com/Projects/find-coordinates-of-image-online.html

import numpy as np
import pyautogui
import keyboard

# координаты кнопок по которым надо нажимать 253,690,244,825,1372,691,1381,816
btn1_click = [253,690]
btn2_click = [244,825]
btn3_click = [1372,691]
btn4_click = [1381,816]
# координаты падающих яйц за 1 шаг до падения пример https://disk.yandex.ru/i/4CSkPZlFtr16Ng
# 581,504,580,626,1046,507,1049,626
egg1_detect =[581,504]
egg2_detect =[580,626]
egg3_detect =[1046,507]
egg4_detect =[1047,628]

running = False

# Функция, которая будет выполняться в цикле
def main_loop():
    while running:
        # Захват скриншота всего экрана
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
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


# Функция для переключения флага running
def toggle_running():
    global running
    running = not running

# Привязка функции к нажатию клавиши пробела
keyboard.add_hotkey('space', toggle_running)

# Основной цикл программы
while True:
    main_loop()

