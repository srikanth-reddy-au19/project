import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((650, 500))
white = (255, 255, 255)
pygame.display.set_caption("Snake And Ladder")

# background

board = pygame.image.load("board.jpeg")
stg = pygame.image.load("background.jpg")
arrow = pygame.image.load("arrow.png")

# players
s = pygame.image.load("player1.png")
r = pygame.image.load("player2.png")

sx = 100
sy = 251

rx = 100
ry = 362

bx = 150
by = 5


def bck():
    screen.blit(stg, (0, 0))
    screen.blit(board, (bx, by))
    screen.blit(arrow, (10, 50))


def splayer(x, y):
    screen.blit(s, (x, y))


def rplayer(x, y):
    screen.blit(r, (x, y))


button = pygame.Rect(10, 50, 40, 40)

score_font = pygame.font.SysFont("comicsansms", 35)
score_font1 = pygame.font.SysFont("comicsansms", 25)
score_font2 = pygame.font.SysFont("comicsansms", 20)

clock = pygame.time.Clock()


def players():
    value2 = score_font1.render("Player 1", True, (255, 0, 0))
    screen.blit(value2, [5, 251])
    value3 = score_font1.render("Player 2", True, (0, 0, 255))
    screen.blit(value3, [5, 362])


def rolls():
    value1 = score_font2.render("Your Turn", True, (255, 255, 255))
    screen.blit(value1, [20, 290])
    # print(value1)


def rollr():
    value = score_font2.render("Your Turn", True, (255, 255, 255))
    screen.blit(value, [20, 400])
    # print(value)


def pickNumber():
    diceroll = random.randint(1, 6)
    if diceroll == 1:
        dice = pygame.image.load("dice1.png")
    elif diceroll == 2:
        dice = pygame.image.load("dice2.png")
    elif diceroll == 3:
        dice = pygame.image.load("dice3.png")
    elif diceroll == 4:
        dice = pygame.image.load("dice4.png")
    elif diceroll == 5:
        dice = pygame.image.load("dice5.png")
    elif diceroll == 6:
        dice = pygame.image.load("dice6.png")
    return (dice, diceroll)


# game loop

running = True

turn = 'red'
while running:
    screen.fill((0, 255, 195))
    bck()
    players()

    if turn == 'red':
        rolls()

    if turn == 'blue':
        rollr()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if button.collidepoint(mouse_pos):
                pickNumber()
                dice, diceroll = pickNumber()
                screen.blit(dice, (58, 48))
                print(diceroll)

            # for player 1

            ## 1st row

            if pickNumber() and turn == 'red':
                turn = 'blue'
                if diceroll == 6 and sx < 162 and sy == 251:
                    sx = sx + 62
                    sy = 447
                    turn = 'red'
                elif sx >= 162 and sx < 358 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55) and diceroll != 6:
                    sx = sx + (49 * diceroll)

                    if sx == 309 and sy == 447:
                        sx = 358
                        sy = 349
                    elif sx == 456 and sy == 349:
                        sx = 358
                        sy = 447
                    elif sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                    elif sx == 603 and sy == 251:
                        sx = 554
                        sy = 153
                    elif sx == 407 and sy == 153:
                        sx = 358
                        sy = 251
                    elif sx == 554 and sy == 55:
                        sx = 505
                        sy = 202

                elif sx >= 162 and sx < 358 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55) and diceroll == 6:
                    sx = sx + (49 * diceroll)

                    if sx == 309 and sy == 447:
                        sx = 358
                        sy = 349
                    elif sx == 456 and sy == 349:
                        sx = 358
                        sy = 447
                    elif sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                    elif sx == 603 and sy == 251:
                        sx = 554
                        sy = 153
                    elif sx == 407 and sy == 153:
                        sx = 358
                        sy = 251
                    elif sx == 554 and sy == 55:
                        sx = 505
                        sy = 202
                    turn = 'red'

                elif sx >= 358 and sx < 407 and diceroll != 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * diceroll)

                    if sx == 456 and sy == 349:
                        sx = 358
                        ry = 447
                    elif sx == 603 and sy == 251:
                        sx = 554
                        sy = 153
                    elif sx == 407 and sy == 153:
                        sx = 358
                        sy = 251
                    elif sx == 554 and sy == 55 and diceroll == 4:
                        sx = 505
                        sy = 202

                elif sx >= 358 and sx < 407 and diceroll == 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 5) - (49 * (diceroll - 6))
                    sy = sy - 49
                    turn = 'red'

                elif sx >= 407 and sx < 456 and diceroll <= 4 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * diceroll)
                    if sx == 456 and sy == 349:
                        sx = 358
                        sy = 447
                    elif sx == 603 and sy == 251:
                        sx = 554
                        sy = 153
                    elif sx == 554 and sy == 55 and diceroll == 3:
                        sx = 505
                        sy = 202
                elif sx >= 407 and sx < 456 and diceroll > 4 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * (diceroll - 5))
                    sy = sy - 49
                elif sx >= 407 and sx < 456 and diceroll == 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 4) - (49 * (diceroll - 5))
                    sy = sy - 49
                    turn = 'red'

                elif sx >= 456 and sx < 505 and diceroll <= 3 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * diceroll)
                    if rx == 603 and ry == 251:
                        sx = 554
                        sy = 153
                    elif sx == 554 and sy == 55 and diceroll == 2:
                        sx = 505
                        sy = 202
                elif sx >= 456 and sx < 505 and diceroll > 3 and diceroll != 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 3) - (49 * (diceroll - 4))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                elif sx >= 456 and sx < 505 and diceroll == 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 3) - (49 * (diceroll - 4))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    turn = 'red'
                elif sx >= 505 and sx < 554 and diceroll <= 2 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * diceroll)
                    if sx == 603 and sy == 251:
                        sx = 554
                        sy = 153
                    elif sx == 554 and sy == 55 and diceroll == 1:
                        sx = 505
                        sy = 202
                elif sx >= 505 and sx < 554 and diceroll > 2 and diceroll != 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 2) - (49 * (diceroll - 3))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    elif sx == 456 and sy == 202:
                        sx = 603
                        sy = 300
                    elif sx == 456 and sy == 104:
                        sx = 554
                        sy = 6
                elif sx >= 505 and sx < 554 and diceroll == 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 2) - (49 * (diceroll - 3))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    elif sx == 456 and sy == 202:
                        sx = 603
                        sy = 300
                    elif sx == 456 and sy == 104:
                        sx = 554
                        sy = 6
                    turn = 'red'

                elif sx >= 554 and sx < 603 and diceroll == 1 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * diceroll)
                    if sx == 603 and sy == 251:
                        sx = 554
                        sy = 153
                elif sx >= 554 and sx < 603 and diceroll > 1 and diceroll != 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 1) - (49 * (diceroll - 2))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    elif sx == 456 and sy == 202:
                        sx = 603
                        sy = 300
                    elif sx == 456 and sy == 104:
                        sx = 554
                        sy = 6

                elif sx >= 554 and sx < 603 and diceroll == 6 and (
                        sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55):
                    sx = sx + (49 * 1) - (49 * (diceroll - 2))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    elif sx == 456 and sy == 202:
                        sx = 603
                        sy = 300
                    elif sx == 456 and sy == 104:
                        sx = 554
                        sy = 6
                    turn = 'red'

                elif sx >= 603 and (sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55) and diceroll != 6:
                    sx = sx - (49 * (diceroll - 1))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    elif sx == 456 and sy == 202:
                        sx = 603
                        sy = 300
                    elif sx == 456 and sy == 104:
                        sx = 554
                        sy = 6
                    elif sx == 358 and sy == 104:
                        sx = 260
                        sy = 202
                elif sx >= 603 and (sy == 447 or sy == 349 or sy == 251 or sy == 153 or sy == 55) and diceroll == 6:
                    sx = sx - (49 * (diceroll - 1))
                    sy = sy - 49
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    elif sx == 456 and sy == 202:
                        sx = 603
                        sy = 300
                    elif sx == 456 and sy == 104:
                        sx = 554
                        sy = 6
                    elif sx == 358 and sy == 104:
                        sx = 260
                        sy = 202
                    turn = 'red'

                # c2 starts from here

                elif sx > 358 and sx <= 603 and (
                        sy == 398 or sy == 300 or sy == 202 or sy == 104 or sy == 6) and diceroll != 6:
                    sx = sx - (49 * diceroll)
                    if sx == 505 and sy == 398:
                        sx = 407
                        sy = 251
                    elif sx == 505 and sy == 300:
                        sx = 554
                        sy = 251
                    elif sx == 456 and sy == 202:
                        sx = 603
                        sy = 300
                    elif sx == 456 and sy == 104:
                        sx = 554
                        sy = 6
                    elif sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                    elif sx == 358 and sy == 104:
                        sx = 260
                        sy = 202

                elif sx > 407 and sx <= 603 and diceroll != 6 and (
                        sy == 398 or sy == 300 or sy == 202 or sy == 104 or sy == 6):
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6:
                        sx = 162
                        sy = 251
                    elif sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                    elif sx == 211 and sy == 6:
                        sx = 162
                        sy = 251
                elif sx > 407 and sx <= 603 and diceroll == 6 and (
                        sy == 398 or sy == 300 or sy == 202 or sy == 104 or sy == 6):
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6:
                        sx = 162
                        sy = 251
                    elif sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                    elif sx == 211 and sy == 6:
                        sx = 162
                        sy = 251
                    turn = 'red'

                elif sx == 407 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll != 6:
                    sx = sx - (49 * diceroll)
                    if sx == 358 and sy == 104:
                        sx = 260
                        sy = 202
                    elif sx == 211 and sy == 6:
                        sx = 162
                        sy = 251

                elif sx == 407 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll == 6:
                    sx = sx - (49 * 5)
                    sy = sy - 49
                    if sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                    turn = 'red'

                elif sx == 358 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll < 5:
                    sx = sx - (49 * diceroll)
                    if sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                elif sx == 358 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll == 5:
                    sx = sx - (49 * 4) + (49 * (diceroll - 5))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                elif sx == 358 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll == 6:
                    sx = sx - (49 * 4) + (49 * (diceroll - 5))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    turn = 'red'
                elif sx == 309 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll < 4:
                    sx = sx - (49 * diceroll)
                    if sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                elif sx == 309 and (
                        sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll >= 4 and diceroll != 6:
                    sx = sx - (49 * 3) + (49 * (diceroll - 4))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                elif sx == 309 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll == 6:
                    sx = sx - (49 * 3) + (49 * (diceroll - 4))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                    turn = 'red'
                elif sx == 260 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll < 3:
                    sx = sx - (49 * diceroll)
                    if sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                elif sx == 260 and (
                        sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll >= 3 and diceroll != 6:
                    sx = sx - (49 * 2) + (49 * (diceroll - 3))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                elif sx == 260 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll == 6:
                    sx = sx - (49 * 2) + (49 * (diceroll - 3))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                    turn = 'red'
                elif sx == 211 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll < 2:
                    sx = sx - (49 * diceroll)
                    if sx == 162 and sy == 300:
                        sx = 260
                        sy = 447
                elif sx == 211 and (
                        sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll != 6 and diceroll >= 2:
                    sx = sx - 49 + (49 * (diceroll - 2))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                elif sx == 211 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll == 6:
                    sx = sx - 49 + (49 * (diceroll - 2))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                    turn = 'red'

                elif sx == 162 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll != 6:
                    sx = sx + (49 * (diceroll - 1))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                    elif sx == 407 and sy == 153:
                        sx = 358
                        sy = 251
                elif sx == 162 and (sy == 398 or sy == 300 or sy == 202 or sy == 104) and diceroll == 6:
                    sx = sx + (49 * (diceroll - 1))
                    sy = sy - 49
                    if sx == 211 and sy == 251:
                        sx = 260
                        sy = 153
                    elif sx == 211 and sy == 153:
                        sx = 162
                        sy = 55
                    elif sx == 260 and sy == 251:
                        sx = 260
                        sy = 398
                    elif sx == 407 and sy == 153:
                        sx = 358
                        sy = 251
                    turn = 'red'

                # final row
                elif sy == 6 and (sx == 554 or sx == 603) and diceroll != 6:
                    sx = sx - (49 * diceroll)
                elif sy == 6 and (sx == 554 or sx == 603) and diceroll == 6:
                    sx = sx - (49 * diceroll)
                    turn = 'red'
                elif sy == 6 and sx == 456 and diceroll < 5:
                    sx = sx - (49 * diceroll)
                elif sy == 6 and sx == 456 and diceroll == 5:
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6 and diceroll == 5:
                        sx = 162
                        sy = 251
                elif sy == 6 and sx == 456 and diceroll == 6:
                    sx = sx
                elif sy == 6 and sx == 505 and diceroll != 6:
                    sx = sx - (49 * diceroll)
                elif sy == 6 and sx == 505 and diceroll == 6:
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6 and diceroll == 6:
                        sx = 162
                        sy = 251

                elif sy == 6 and sx == 407 and diceroll < 6:
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6 and diceroll == 4:
                        sx = 162
                        sy = 251
                elif sy == 6 and sx == 407 and sx >= 162 and diceroll == 6:
                    sx = sx

                elif sy == 6 and sx == 358 and sx >= 162 and diceroll >= 5:
                    sx = sx
                elif sy == 6 and sx == 358 and sx >= 162 and diceroll < 5:
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6 and diceroll == 3:
                        sx = 162
                        sy = 251

                elif sy == 6 and sx == 309 and sx >= 162 and diceroll >= 4:
                    sx = sx
                elif sy == 6 and sx == 309 and sx >= 162 and diceroll < 4:
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6 and diceroll == 2:
                        sx = 162
                        sy = 251

                elif sy == 6 and sx == 260 and sx >= 162 and diceroll >= 3:
                    sx = sx
                elif sy == 6 and sx == 260 and sx >= 162 and diceroll < 3:
                    sx = sx - (49 * diceroll)
                    if sx == 211 and sy == 6 and diceroll == 1:
                        sx = 162
                        sy = 251
                elif sy == 6 and sx == 211 and rx > 162 and diceroll >= 2:
                    sx = sx








            # for player 2

            elif pickNumber() and turn == 'blue':
                turn = 'red'
                if diceroll == 6 and rx < 162 and ry == 362:
                    rx = rx + 62
                    ry = 450
                    turn = 'blue'
                elif rx >= 162 and rx < 358 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58) and diceroll != 6:
                    rx = rx + (49 * diceroll)

                    if rx == 309 and ry == 450:
                        rx = 358
                        ry = 352
                    elif rx == 456 and ry == 352:
                        rx = 358
                        ry = 450
                    elif rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                    elif rx == 603 and ry == 254:
                        rx = 554
                        ry = 156
                    elif rx == 407 and ry == 156:
                        rx = 358
                        ry = 254
                    elif rx == 554 and ry == 58:
                        rx = 505
                        ry = 205

                elif rx >= 162 and rx < 358 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58) and diceroll == 6:
                    rx = rx + (49 * diceroll)

                    if rx == 309 and ry == 450:
                        rx = 358
                        ry = 352
                    elif rx == 456 and ry == 352:
                        rx = 358
                        ry = 450
                    elif rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                    elif rx == 603 and ry == 254:
                        rx = 554
                        ry = 156
                    elif rx == 407 and ry == 156:
                        rx = 358
                        ry = 254
                    elif rx == 554 and ry == 58:
                        rx = 505
                        ry = 205
                    turn = 'blue'

                elif rx >= 358 and rx < 407 and diceroll != 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * diceroll)

                    if rx == 456 and ry == 352:
                        rx = 358
                        ry = 450
                    elif rx == 603 and ry == 254:
                        rx = 554
                        ry = 156
                    elif rx == 407 and ry == 156:
                        rx = 358
                        ry = 254
                    elif rx == 554 and ry == 58 and diceroll == 4:
                        rx = 505
                        ry = 205

                elif rx >= 358 and rx < 407 and diceroll == 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 5) - (49 * (diceroll - 6))
                    ry = ry - 49
                    turn = 'blue'

                elif rx >= 407 and rx < 456 and diceroll <= 4 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * diceroll)
                    if rx == 456 and ry == 352:
                        rx = 358
                        ry = 450
                    elif rx == 603 and ry == 254:
                        rx = 554
                        ry = 156
                    elif rx == 554 and ry == 58 and diceroll == 3:
                        rx = 505
                        ry = 205
                elif rx >= 407 and rx < 456 and diceroll > 4 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * (diceroll - 5))
                    ry = ry - 49
                elif rx >= 407 and rx < 456 and diceroll == 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 4) - (49 * (diceroll - 5))
                    ry = ry - 49
                    turn = 'blue'

                elif rx >= 456 and rx < 505 and diceroll <= 3 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * diceroll)
                    if rx == 603 and ry == 254:
                        rx = 554
                        ry = 156
                    elif rx == 554 and ry == 58 and diceroll == 2:
                        rx = 505
                        ry = 205
                elif rx >= 456 and rx < 505 and diceroll > 3 and diceroll != 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 3) - (49 * (diceroll - 4))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                elif rx >= 456 and rx < 505 and diceroll == 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 3) - (49 * (diceroll - 4))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    turn = 'blue'
                elif rx >= 505 and rx < 554 and diceroll <= 2 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * diceroll)
                    if rx == 603 and ry == 254:
                        rx = 554
                        ry = 154
                    elif rx == 554 and ry == 58 and diceroll == 1:
                        rx = 505
                        ry = 205
                elif rx >= 505 and rx < 554 and diceroll > 2 and diceroll != 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 2) - (49 * (diceroll - 3))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    elif rx == 456 and ry == 205:
                        rx = 603
                        ry = 303
                    elif rx == 456 and ry == 107:
                        rx = 554
                        ry = 9
                elif rx >= 505 and rx < 554 and diceroll == 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 2) - (49 * (diceroll - 3))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    elif rx == 456 and ry == 205:
                        rx = 603
                        ry = 303
                    elif rx == 456 and ry == 107:
                        rx = 554
                        ry = 9
                    turn = 'blue'

                elif rx >= 554 and rx < 603 and diceroll == 1 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * diceroll)
                    if rx == 603 and ry == 254:
                        rx = 554
                        ry = 156
                elif rx >= 554 and rx < 603 and diceroll > 1 and diceroll != 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 1) - (49 * (diceroll - 2))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    elif rx == 456 and ry == 205:
                        rx = 603
                        ry = 303
                    elif rx == 456 and ry == 107:
                        rx = 554
                        ry = 9

                elif rx >= 554 and rx < 603 and diceroll == 6 and (
                        ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58):
                    rx = rx + (49 * 1) - (49 * (diceroll - 2))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    elif rx == 456 and ry == 205:
                        rx = 603
                        ry = 303
                    elif rx == 456 and ry == 107:
                        rx = 554
                        ry = 9
                    turn = 'blue'

                elif rx >= 603 and (ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58) and diceroll != 6:
                    rx = rx - (49 * (diceroll - 1))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    elif rx == 456 and ry == 205:
                        rx = 603
                        ry = 303
                    elif rx == 456 and ry == 107:
                        rx = 554
                        ry = 9
                    elif rx == 358 and ry == 107:
                        rx = 260
                        ry = 205
                elif rx >= 603 and (ry == 450 or ry == 352 or ry == 254 or ry == 156 or ry == 58) and diceroll == 6:
                    rx = rx - (49 * (diceroll - 1))
                    ry = ry - 49
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    elif rx == 456 and ry == 205:
                        rx = 603
                        ry = 303
                    elif rx == 456 and ry == 107:
                        rx = 554
                        ry = 9
                    elif rx == 358 and ry == 107:
                        rx = 260
                        ry = 205
                    turn = 'blue'

                # c2 starts from here

                elif rx > 358 and rx <= 603 and (
                        ry == 401 or ry == 303 or ry == 205 or ry == 107 or ry == 9) and diceroll != 6:
                    rx = rx - (49 * diceroll)
                    if rx == 505 and ry == 401:
                        rx = 407
                        ry = 254
                    elif rx == 505 and ry == 303:
                        rx = 554
                        ry = 254
                    elif rx == 456 and ry == 205:
                        rx = 603
                        ry = 303
                    elif rx == 456 and ry == 107:
                        rx = 554
                        ry = 9
                    elif rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                    elif rx == 358 and ry == 107:
                        rx = 260
                        ry = 205

                elif rx > 407 and rx <= 603 and diceroll != 6 and (
                        ry == 401 or ry == 303 or ry == 205 or ry == 107 or ry == 9):
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9:
                        rx = 162
                        ry = 254
                    elif rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                    elif rx == 211 and ry == 9:
                        rx = 162
                        ry = 254
                elif rx > 407 and rx <= 603 and diceroll == 6 and (
                        ry == 401 or ry == 303 or ry == 205 or ry == 107 or ry == 9):
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9:
                        rx = 162
                        ry = 254
                    elif rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                    elif rx == 211 and ry == 9:
                        rx = 162
                        ry = 254
                    turn = 'blue'

                elif rx == 407 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll != 6:
                    rx = rx - (49 * diceroll)
                    if rx == 358 and ry == 107:
                        rx = 260
                        ry = 203
                    elif rx == 211 and ry == 9:
                        rx = 162
                        ry = 254

                elif rx == 407 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll == 6:
                    rx = rx - (49 * 5)
                    ry = ry - 49
                    if rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                    turn = 'blue'

                elif rx == 358 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll < 5:
                    rx = rx - (49 * diceroll)
                    if rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                elif rx == 358 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll == 5:
                    rx = rx - (49 * 4) + (49 * (diceroll - 5))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                elif rx == 358 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll == 6:
                    rx = rx - (49 * 4) + (49 * (diceroll - 5))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    turn = 'blue'
                elif rx == 309 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll < 4:
                    rx = rx - (49 * diceroll)
                    if rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                elif rx == 309 and (
                        ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll >= 4 and diceroll != 6:
                    rx = rx - (49 * 3) + (49 * (diceroll - 4))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                elif rx == 309 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll == 6:
                    rx = rx - (49 * 3) + (49 * (diceroll - 4))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                    turn = 'blue'
                elif rx == 260 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll < 3:
                    rx = rx - (49 * diceroll)
                    if rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                elif rx == 260 and (
                        ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll >= 3 and diceroll != 6:
                    rx = rx - (49 * 2) + (49 * (diceroll - 3))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 155:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                elif rx == 260 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll == 6:
                    rx = rx - (49 * 2) + (49 * (diceroll - 3))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                    turn = 'blue'
                elif rx == 211 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll < 2:
                    rx = rx - (49 * diceroll)
                    if rx == 162 and ry == 303:
                        rx = 260
                        ry = 450
                elif rx == 211 and (
                        ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll != 6 and diceroll >= 2:
                    rx = rx - 49 + (49 * (diceroll - 2))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                elif rx == 211 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll == 6:
                    rx = rx - 49 + (49 * (diceroll - 2))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                    turn = 'blue'

                elif rx == 162 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll != 6:
                    rx = rx + (49 * (diceroll - 1))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                    elif rx == 407 and ry == 156:
                        rx = 358
                        ry = 254
                elif rx == 162 and (ry == 401 or ry == 303 or ry == 205 or ry == 107) and diceroll == 6:
                    rx = rx + (49 * (diceroll - 1))
                    ry = ry - 49
                    if rx == 211 and ry == 254:
                        rx = 260
                        ry = 156
                    elif rx == 211 and ry == 156:
                        rx = 162
                        ry = 58
                    elif rx == 260 and ry == 254:
                        rx = 260
                        ry = 401
                    elif rx == 407 and ry == 156:
                        rx = 358
                        ry = 254
                    turn = 'blue'

                # final row
                elif ry == 9 and (rx == 554 or rx == 603) and diceroll != 6:
                    rx = rx - (49 * diceroll)
                elif ry == 9 and (rx == 554 or rx == 603) and diceroll == 6:
                    rx = rx - (49 * diceroll)
                    turn = 'blue'
                elif ry == 9 and rx == 456 and diceroll < 5:
                    rx = rx - (49 * diceroll)
                elif ry == 9 and rx == 456 and diceroll == 5:
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9 and diceroll == 5:
                        rx = 162
                        ry = 254
                elif ry == 9 and rx == 456 and diceroll == 6:
                    rx = rx
                elif ry == 9 and rx == 505 and diceroll != 6:
                    rx = rx - (49 * diceroll)
                elif ry == 9 and rx == 505 and diceroll == 6:
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9 and diceroll == 6:
                        rx = 162
                        ry = 254

                elif ry == 9 and rx == 407 and diceroll < 6:
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9 and diceroll == 4:
                        rx = 162
                        ry = 254
                elif ry == 9 and rx == 407 and rx >= 162 and diceroll == 6:
                    rx = rx

                elif ry == 9 and rx == 358 and rx >= 162 and diceroll >= 5:
                    rx = rx
                elif ry == 9 and rx == 358 and rx >= 162 and diceroll < 5:
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9 and diceroll == 3:
                        rx = 162
                        ry = 254

                elif ry == 9 and rx == 309 and rx >= 162 and diceroll >= 4:
                    rx = rx
                elif ry == 9 and rx == 309 and rx >= 162 and diceroll < 4:
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9 and diceroll == 2:
                        rx = 162
                        ry = 254

                elif ry == 9 and rx == 260 and rx >= 162 and diceroll >= 3:
                    rx = rx
                elif ry == 9 and rx == 260 and rx >= 162 and diceroll < 3:
                    rx = rx - (49 * diceroll)
                    if rx == 211 and ry == 9 and diceroll == 1:
                        rx = 162
                        ry = 254
                elif ry == 9 and rx == 211 and rx > 162 and diceroll >= 2:
                    rx = rx

    splayer(sx, sy)
    rplayer(rx, ry)
    pygame.display.update()

    if sx == 162 and sy == 6:
        screen.fill((50, 153, 213))
        value = score_font.render("Red won", True, (255, 255, 102))
        screen.blit(value, [250, 200])
        running = False

    if rx == 162 and ry == 9:
        screen.fill((50, 153, 213))
        value = score_font.render("Blue won", True, (255, 255, 102))
        screen.blit(value, [250, 200])
        running = False

    time.sleep(1.3)

pygame.display.update()
clock.tick(40)
#pygame.quit()
#quit()
