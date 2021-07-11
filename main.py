
                          # ****** Project :  MULTIPLAYER CAR RACING GAME  *******
                                     #  using python and pygame

                          #   ********  importing IMPORTANT modules  *******

import pygame # it will import all the pygame modules in the code
import random  # random function is used here to generate arriving cars at random position
import math  #  math module is used for sqrt function as by which i am checking the collision b/w player and hurdle
import time  # i have used it to use the sleep function( as after the collision the screen suddenly closes
             # and shows the result but after using it it stays for some time


# colors used for buttons are set here as we know (red, green, blue)
white = (255,255,255)
black = (0,0,0)
aqua = (0,128,128)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
silver = (192,192,192)
light_blue = (135,206,235)
light_white = (255,228,181)
navy = (0,0,128)
lime_green = (50,205,50)
crimsion = (220,20,60)

# used to initialize the pygame module
pygame.init()

# setting game display
screen = pygame.display.set_mode((1024,600))

# Title and icon( shown as title in the title bar)
pygame.display.set_caption("CAR RACING")


# intro image( image show at home or menu page)
intro_img = pygame.image.load('intro_img2.jpg')

# background other than the main menu
ce_image = pygame.image.load("image_ce.jpg")

# game Background
background = pygame.image.load('road.png')

# huddle image and position
huddleImg = pygame.image.load('hurdle.png')

# starting the mixer in order to play music files in pygame
pygame.mixer.init()


loadingpageImg = pygame.image.load('startflag.jpg')
level1Img = pygame.image.load('level1.png')
level2Img = pygame.image.load('level2.png')
level3Img = pygame.image.load('level3.png')
level4Img = pygame.image.load('level4.png')
level5Img = pygame.image.load('level5.png')

# huddleX = random.randint(30,120)
# huddleY = random.randint(-80,-50)

# number_of_players' game
n_of_pl = 0

# used to take name of file which we want to play
game_mus = pygame.mixer.Sound("racing-cars-sounds.wav")


# last msg for single player game
def last_msg(scor ) :
    exit = False

    while not exit:

        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button(300, 500, "Main Menu ", lime_green, black, green)
        button(700, 500, " Quit ", crimsion, black, red)

        message("    GAME  OVER  !!!!       score  :  " + str(scor), 200, 200, silver, False, True, "large")
        pygame.display.update()

# last msg for player1 of 2 player game
def last_msg1() :
    exit = False

    while not exit:

        screen.fill(black)
        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                pygame.quit()
                quit()

        button(300, 550, "Main Menu ", lime_green, black, green)
        button(700, 550, " Quit ", crimsion, black, red)

        message("Player 2   won  ", 340, 200, silver, False, True, "large")
        message("GAME  OVER  !!!!  ", 330, 350, silver, False, True, "medium")

        # message("score  :    "+ str(scor) , 400, 350, silver, False, True, "medium")

        pygame.display.update()

#  last msg for player2 of 2 player game

def last_msg2() :
    exit = False

    while not exit:

        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button(300, 550, "Main Menu ", lime_green, black, green)
        button(700, 550, " Quit ", crimsion, black, red)

        message("Player 1   won  ", 340, 200, silver, False, True, "large")
        message("GAME  OVER  !!!!  ", 330, 350, silver, False, True, "medium")

        # message("score  :    "+ str(scor) , 400, 350, silver, False, True, "medium")

        pygame.display.update()


# checking if the collision occurs
def dist_collision(plyr_x, plyr_y, hdl_x, hdl_y) :
    dist = math.sqrt( (math.pow(plyr_x - hdl_x ,2)) + (math.pow(plyr_y - hdl_y , 2)) )
    if dist < 80 :
        return True

    else :
        return False


# showing current score on the game window
def show_score(x, y, score_value, font) :
    score = font.render("Score  : " + str(score_value), True, (155, 155, 155))
    screen.blit(score, (x, y))
    return score_value


# creating huddle
def huddle(huddleX , huddleY) :
    screen.blit(huddleImg, (huddleX, huddleY))


# creating many huddles
def chng_hdl_pos_y(hdl_Y, speed_hdl):
    if hdl_Y >= 580 :
        hdl_Y = random.randint(-500, -20)
    else :
        hdl_Y += speed_hdl

    return hdl_Y

def chng_hdl_pos_x(width_start , width_end, hdl_X,hdl_Y):
    if hdl_Y >= 580 :
        hdl_X = random.randint(width_start, width_end)

    return hdl_X


# increasing score
def check_score(score_value, hdl_Y) :
    if hdl_Y >= 580 :
        score_value += 1
    return score_value
# *************


# instructions page
def instruction():
    control = False

    while not control:

        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                quit()

        # message,x-position,y-position,color,bold,italic,size,style
        message("Instructions", 400, 35, red, False, True, "large")

        message("     For Player 1 : ", 350, 100, crimsion, False, True, "small")

        message(" >>>>   Use   a  to   move   left .", 0, 135, silver, False, True, "small")
        message(" >>>>   Use   d   to   move   right .", 0, 165, silver, False, True, "small")
        message(" >>>>   Use   w   to   move   up .", 0, 195, silver, False, True, "small")
        message(" >>>>   Use   s   to   move   down .", 0, 225, silver, False, True, "small")

        message("     For Player 2 : ", 350, 270, crimsion, False, True, "small")

        message(" >>>>   Use   left key to   move   left .", 0, 300, silver, False, True, "small")
        message(" >>>>   Use   right key  to   move   right .", 0, 330, silver, False, True, "small")
        message(" >>>>   Use   up  key to   move   up .", 0, 370, silver, False, True, "small")
        message(" >>>>   Use   down key  to   move   down .", 0, 410, silver, False, True, "small")

        button(500, 500, " <- Back ", navy, white, blue)

        pygame.display.update()


# exit function
def exit():
    exit = False

    while not exit:

        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                pygame.quit()
                quit()

        # pygame.draw.line(screen, silver, (0, window_height - 668), (window_width, window_height - 668), 1)

        message("Are You Sure, You Want To Exit The Game ", 100, 200, silver, False, True, "medium")

        # (x,y,message,1st block color, text color , 2nd block color)
        button(300, 300, " YES ", lime_green, black, green)
        button(550, 300, " NO ", crimsion, black, red)

        pygame.draw.line(screen, silver, (0,  450), (1024, 450), 1)

        pygame.display.update()


# button function
# position of button from x-axis , from y-axis ,  color of button , text color , color of button when hover
def button(x_button, y_button, msg, color1, color2, color3):
    pygame.draw.rect(screen, color1, [x_button , y_button, 100, 30])

    message(msg, x_button + 5, y_button + 5, color2)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button < mouse[0] < x_button + 100 and y_button < mouse[1] < y_button + 30:
        pygame.draw.rect(screen, color3, [x_button, y_button, 100, 30])
        message(msg, x_button + 5, y_button + 5, color2)
        if click == (1, 0, 0) and msg == " <- Back ":
            welcome_screen()
        elif click == (1, 0, 0) and msg == " YES ":
            pygame.quit()
            quit()
        elif click == (1, 0, 0) and msg == " NO ":
            welcome_screen()
        elif click == (1, 0, 0) and msg == " Controls ":
            game_mus.stop()
            instruction()
        elif click == (1, 0, 0) and msg == " Exit ":
            game_mus.stop()
            exit()
        elif click == (1, 0, 0) and msg == " Play ":
            game_mus.stop()
            players()
        elif click == (1, 0, 0) and msg == " One ":
            n_of_pl = 1
            speed = 0.8
            load_page(n_of_pl,speed)
        elif click == (1, 0, 0) and msg == " Two ":
            choose_mode()
        elif click == (1, 0, 0) and msg == "Main Menu ":
            welcome_screen()
        elif click == (1, 0, 0) and msg == " Quit ":
            pygame.quit()
            quit()
        elif click == (1, 0, 0) and msg == " Slow ":
            n_of_pl = 2
            speed = 0.4
            load_page(n_of_pl,speed)
        elif click == (1, 0, 0) and msg == " Medium ":
            n_of_pl = 2
            speed = 0.8
            load_page(n_of_pl,speed)
        elif click == (1, 0, 0) and msg == " Fast ":
            n_of_pl = 2
            speed = 1.4
            load_page(n_of_pl,speed)
        elif click == (1, 0, 0) and msg == "   Pause ":
            paused()
        elif click == (1,0,0) and msg == " Continue ":
            return 1

# message function it is used to display message on the screen
# (message,x-position,y-position,color,bold,italic,size,style)
# style could be another as well like Georgia,Verdana,arial
def message(msg,x_pos,y_pos,color,b=False,i=True,size = "small",style = "Chilanka"):
	if size == "small":
		font=pygame.font.SysFont(style,20,bold = b,italic = i)
	elif size == "medium":
		font=pygame.font.SysFont(style,40,bold = b,italic = i)
	elif size == "large":
		font=pygame.font.SysFont('freesansbold.ttf',60,bold = b,italic = i)

	render=font.render(msg,True,color)
	screen.blit(render,(x_pos,y_pos))


# number of players (page)
def players():
    player_number = False

    while not player_number:

        screen.fill(black)
        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_number = True
                pygame.quit()
                quit()

        pygame.draw.line(screen, silver, (0, 100), (1024, 100), 1)

        message(" Select  the  number  of  players  for  the  game ", 50, 200, silver, False, True, "medium")

        # (x,y,message,1st block color, text color , 2nd block color)
        button(200, 300, " One ",red, white,green)
        button(500, 300, " Two ",red, white,green)

        pygame.draw.line(screen, silver, (0, 450), (1024, 450), 1)

        pygame.display.update()


# game intro loop
def welcome_screen():
    intro = False

    while not intro:
        screen.blit(intro_img, (0, 0))

        pygame.mixer.Sound.play(game_mus)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = True
                pygame.quit()
                quit()

        message("Car  Racing ", 350, 25, white, False, True, "large")

        # x_button,y_button,msg,color1,color2,color3
        button(50, 450, " Play ", lime_green, black, green)
        button(450, 450, " Controls ", blue, black, light_blue)
        button(800, 450, " Exit ", crimsion, black, red)

        pygame.display.update()

def choose_mode() :
    exit = False

    while not exit:

        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        message("Choose the mode : ", 100, 250, silver, False, True, "medium")
        button(150, 400, " Slow ", lime_green, black, green)
        button(500, 400, " Medium ", crimsion, black, red)
        button(850, 400, " Fast ", lime_green, black, red)

        pygame.draw.line(screen, silver, (0, 450), (1024, 450), 1)

        pygame.display.update()

# used to pause the running game
def paused():
    pause = False

    while not pause:
        screen.blit(ce_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = True
                pygame.quit()
                quit()

        message("Press Continue to return to the Game !!  ", 100, 200, silver, False, True, "large")
        pause = button(300, 550, " Continue ", lime_green, black, green)
        button(700, 550, "Main Menu ", crimsion, black, red)

        pygame.display.update()

def load_page(n_of_pl, speed):
    pause = False
    i=0
    while not pause:
        screen.blit(loadingpageImg, (0, 0))
        message("Loading .... ", 785, 100, white, False, False, "small")

        if (i<200):
            screen.blit(level1Img, (750, 50))
            i +=1
        if (i >= 200):
            screen.blit(level2Img, (750, 50))
            i+=1
        if (i >= 400):
            screen.blit(level3Img, (750, 49))
            i+=1
        if (i >= 600):
            screen.blit(level4Img, (750, 49))
            i+=1
        if (i >= 800):
            screen.blit(level5Img, (750, 49))
            i+=1
        if (i>= 1000):
            gameloop1(n_of_pl, speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = True
                pygame.quit()
                quit()

        pygame.display.update()


# main game loop for both the games i.e. single and 2 players
def gameloop1(n_of_pl,speed_hdl) :
    playerX = 240
    playerY = 470
    playerImg = pygame.image.load('car1.png')
    playerImg2 = pygame.image.load('car2.png')
    collisionImg = pygame.image.load('collision.jpg')

    playerX2 = 530
    playerY2 = 470
    huddleX = random.randint(30, 120)
    huddleY = random.randint(80, 150)
    huddle2X = random.randint(200, 360)
    huddle2Y = random.randint(80, 150)
    huddle3X = random.randint(480, 690)
    huddle3Y = random.randint(80, 150)
    huddle4X = random.randint(740, 900)
    huddle4Y = random.randint(80, 150)

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_X = 18
    text_Y = 8


    running = True
    while running:
        screen.blit(background, (0, 0))

        button(905, 5, "   Pause ",red, white,green)
        score_value = check_score(score_value, huddleY)
        huddleY = chng_hdl_pos_y(huddleY, speed_hdl)
        huddleX = chng_hdl_pos_x(30 ,100, huddleX, huddleY)
        score_value = check_score(score_value, huddle2Y)
        huddle2Y = chng_hdl_pos_y(huddle2Y, speed_hdl)
        huddle2X = chng_hdl_pos_x(200 ,360, huddle2X, huddle2Y)
        score_value = check_score(score_value, huddle3Y)
        huddle3Y = chng_hdl_pos_y(huddle3Y, speed_hdl)
        huddle3X = chng_hdl_pos_x(440 ,690, huddle3X, huddle3Y)
        score_value = check_score(score_value, huddle4Y)
        huddle4Y = chng_hdl_pos_y(huddle4Y, speed_hdl)
        huddle4X = chng_hdl_pos_x(740 ,900, huddle4X, huddle4Y)

        if n_of_pl == 1:
            # blit function is basically used to draw something (here playerImg is drawn at given (playerX, playerY) position ).
            screen.blit(playerImg, (playerX, playerY))

            for event in pygame.event.get():
                # if we click on cross on the title bar the the screen closes
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    # controls for player 1
                    if event.key == pygame.K_d:
                        if (playerX < 895):
                            playerX = playerX + 64
                    if event.key == pygame.K_a:
                        playerX = playerX - 64
                    if event.key == pygame.K_w and playerY>50:
                        playerY = playerY - 64
                    if event.key == pygame.K_s and playerY<450:
                        playerY = playerY + 64
                if (playerX <= 0):
                    playerX += 20

        if n_of_pl == 2 :

            screen.blit(playerImg, (playerX, playerY))
            screen.blit(playerImg2, (playerX2, playerY2))

            for event in pygame.event.get():
                # if we click on cross on the title bar the the screen closes
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # controls for player 1
                    if event.key == pygame.K_d:
                        if (playerX < 895):
                            playerX = playerX + 64
                    if event.key == pygame.K_a:
                        playerX = playerX - 64
                    if event.key == pygame.K_w and playerY > 50:
                        playerY = playerY - 64
                    if event.key == pygame.K_s and playerY < 450:
                        playerY = playerY + 64

                    if event.key == pygame.K_RIGHT:
                        if (playerX2 < 895):
                            playerX2 = playerX2 + 64
                    if event.key == pygame.K_LEFT:
                        playerX2 = playerX2 - 64
                    if event.key == pygame.K_UP and playerY2>50:
                        playerY2 = playerY2 - 64
                    if event.key == pygame.K_DOWN and playerY2<450:
                        playerY2 = playerY2 + 64

                if (playerX2 < playerX):
                    playerX2 = 500 + 20
                if (playerX <= 0):
                    playerX += 20

        # playerX2 = player()
        huddle(huddleX, huddleY)
        huddle(huddle2X, huddle2Y)
        huddle(huddle3X, huddle3Y)
        huddle(huddle4X, huddle4Y)


        score_value = show_score(text_X, text_Y, score_value, font)


        if ( dist_collision(playerX , playerY , huddleX , huddleY ) or dist_collision(playerX , playerY , huddle2X , huddle2Y ) or dist_collision(playerX , playerY , huddle3X , huddle3Y ) or dist_collision(playerX , playerY , huddle4X , huddle4Y )) :

            while running :
                # collision image appear to the screen
                screen.blit(collisionImg, (playerX, playerY-80))
                # collision sound is active
                mus = pygame.mixer.Sound("crash-sound.wav")
                pygame.mixer.Sound.play(mus)
                pygame.display.update()

                time.sleep(1.5)
                if(n_of_pl == 1):
                    last_msg(score_value)
                else:
                    # if number of players are 2 and 1st player is collided
                    # last_msg1(score_value)
                    last_msg1()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

        if n_of_pl == 2 :
            if ( dist_collision(playerX2 , playerY2 , huddleX , huddleY ) or dist_collision(playerX2 , playerY2 , huddle2X , huddle2Y ) or dist_collision(playerX2 , playerY2 , huddle3X , huddle3Y ) or dist_collision(playerX2 , playerY2 , huddle4X , huddle4Y )) :
                print("collide")

                while running :
                    screen.blit(collisionImg, (playerX2, playerY2 -80))
                    mus = pygame.mixer.Sound("crash-sound.wav")
                    pygame.mixer.Sound.play(mus)
                    pygame.display.update()

                    time.sleep(0.5)

                    # last_msg2(score_value)
                    last_msg2()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

        pygame.display.update()

welcome_screen()
