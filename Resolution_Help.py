import pyautogui as pya
import pygame as py
from screeninfo import get_monitors

# def determineRes():

#     x, y = pya.size()

#     return x, y

ratio = 3.2

def get_total_pixels():
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height
        total_pixels = width * height
    return total_pixels

def pygameScreenSize(ratio):

    monitor_x, monitor_y = pya.size()

    x = monitor_x/ratio
    y = monitor_y/ratio

    return x, y

def determinePongSize(ratio):   

    x, y = pygameScreenSize(ratio)

    # Paddle proportions
    # position in x, position in y, rectangle width, rectangle height
    rect_width, rect_height = x/90, y/5

    return rect_width, rect_height

def determineInitialPosition(ratio, player):
    
    x1, y1 = pygameScreenSize(ratio)
    x2, y2 = determinePongSize(ratio)

    if player == 1:
        rect_x = 100

    elif player == 2:
        rect_x = x1 - 100

    rect_y = y1/2 - y2/2

    return rect_x, rect_y

x, y = pygameScreenSize(ratio)

rect1_x, rect1_y = determineInitialPosition(ratio, 1)
rect2_x, rect2_y = determineInitialPosition(ratio, 2)

rect1_width, rect1_height = determinePongSize(ratio)
rect2_width, rect2_height = determinePongSize(ratio)

print("Screen size is (x, y):", x, y)
print("Pong1 size is (x, y):", rect1_width, rect1_height)
print("Pong2 size is (x, y):", rect2_width, rect2_height)
print("Pong1 position is (x, y):", rect1_x, rect1_y)
print("Pong2 position is (x, y):", rect2_x, rect2_y)
