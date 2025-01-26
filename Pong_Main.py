import pygame as py
import pandas as pd

def start_pong():
    #Start pygame
    py.init()

    #Variables
    white = (255, 255, 255)
    black =(0, 0, 0)

    fps = 30
    paddle_color = white

    #Creates display and makes it fullscreen (you can change it to a different resolution if you want)
    screen = py.display.set_mode((0, 0), py.FULLSCREEN)

    #Name of the tab
    py.display.set_caption('Pong')

    #Running the actual game
    game_running = True

    clock = py.time.Clock()

    #Making the delay for holding down key so we dont get 5 million inputs
    py.key.set_repeat(0, 100) #0 delay and 100ms interval before next input is registered

    #While game is running, all this happens
    while game_running == True:

        #Update the displace so frame changes
        py.display.flip()

        #running the fps
        clock.tick(fps)

        for event in py.event.get():  
                if event.type == py.QUIT:
                    game_running = False
                
                #Checking what keys are being pressed and defining what happens if they're pressed
                if event.type == py.KEYDOWN:  
                    #if esc is pressed, close the game
                    if event.key == py.K_ESCAPE:
                        game_running = False

        #Fill the screen with a color
        screen.fill(black)

        #Paddle proportions
        rect_x, rect_y, rect_width, rect_height = 100, 100, 33, 125

        #create paddles
        paddle_1 = py.draw.rect(screen, paddle_color, (rect_x, rect_y, rect_width, rect_height))
        paddle_2 = py.draw.rect(screen, paddle_color, (rect_x + 1650, rect_y, rect_width, rect_height))

    #Function to make paddles move
    def paddle_moving(player_number):   
        while game_running == True:
            for event in py.event.get():
                #Moving the paddles
                if event.type == py.K_s:
                    print('s key pressed')
                    if player_number == 1:
                        print('paddle move')
                        paddle_1.y = paddle_1.y - 10
                if event.type == py.K_k:
                    if player_number == 2:
                        print('paddle 2 move')
                        paddle_2.y = paddle_2.y - 10
    
    #Try to make paddles work (it wont)
    while game_running == True:
        paddle_moving(1)

    #Completely resets the game and cleans everything up
    py.quit()

#The game doesnt run unless you run the file
if __name__ == "__main__":
     start_pong()