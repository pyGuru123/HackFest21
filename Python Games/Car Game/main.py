import pygame, time, keyboard, random


def car4():
    try:
        coins = int(open("cars_coins").read())
        prevcoins = coins
    except:
        file = open("cars_coins", "w")
        file.write("100")
        file.close()
        coins = 100
        prevcoins = 100
    try:
        highscore = int(open("cars_highscore").read())
    except:
        file = open("cars_highscore", "w")
        file.write("0")
        file.close()
        highscore = 0
    px, py = 120.0, 175.0
    lane = 2
    speed = 1.2
    q1x, q2x = 70.0, 870.0
    bright1, bright2 = 100, 0
    d = 0
    move = 0
    count = 0
    lifes = 6
    score = 0
    stop = 0
    coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
    coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
    collected = [0 for i in range(11)]
    barrierx = [[1700.0, 2300.0, 3000.0], [1500.0, 1600.0, 2900.0, 2400.0, 800.0],
                [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
    barriery = [[205.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0], [205.0, 205.0, 335.0, 75.0, 335.0, 335.0]]
    b_set = 0
    check = 0
    gameover = largefont.render("GAME OVER!", True, red, yellow)
    g = 1
    start = 0
    startt = smallfont.render("Press 'ENTER' to start.", True, red, yellow)
    coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
    while 1:
        screen.fill((20, 10, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(screen, (250, 0, 250), (0, 0, 1100, 30))
        pygame.draw.rect(screen, (250, 250, 250), (0, 30, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 160, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 290, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 420, 1100, 20))
        pygame.draw.circle(screen, (bright1, 200, 0), (int(q1x), 40), 8)
        pygame.draw.circle(screen, (200, bright2, 0), (int(q1x), 300), 8)
        pygame.draw.circle(screen, (200, bright1, 0), (int(q2x), 170), 8)
        pygame.draw.circle(screen, (bright2, 200, 0), (int(q2x), 430), 8)
        screen.blit(car_4s, (int(px), int(py) - 10))
        screen.blit(coin, (0, 0))
        if start == 0:
            screen.blit(startt, (440, 200))
            pygame.display.update()
            time.sleep(0.1)
            if keyboard.is_pressed('enter'):
                start = 1
            continue
        q1x = (q1x - speed) % 1600
        q2x = (q2x - speed) % 1600
        bright1 = (bright1 + 1) % 200
        bright2 = (bright2 + 1) % 200
        score += 1
        check = 0
        if score > highscore:
            highscore = score
        if score % 2000 == 0:
            speed += 0.1 * speed
        scoret = smallfont.render(f"Score: {int(score)}", True, yellow, red)
        highscoret = smallfont.render(f"Highscore: {int(highscore)}", True, (0, 0, 0))
        screen.blit(scoret, (470, 0))
        for i in range(11):
            if collected[i] == 0:
                if coinx[i] <= 1100:
                    screen.blit(coin_p, (int(coinx[i]), int(coiny[i])))
                coinx[i] -= speed
                if (0 <= px - coinx[i] <= 50 or 0 <= coinx[i] - px <= 100) and (
                        0 <= py - coiny[i] <= 40 or 0 <= coiny[i] - py <= 100):
                    coins += 10
                    collected[i] = 1
                if coinx[i] <= -100:
                    collected[i] = 1
        coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
        if collected.count(0) == 0:
            coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
            coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
            collected = [0 for i in range(11)]
        for i in range(len(barriery[b_set])):
            screen.blit(barrier_p, (int(barrierx[b_set][i]), int(barriery[b_set][i])))
            barrierx[b_set][i] -= speed
            if barrierx[b_set][i] >= -100:
                check += 1
            if (not stop) and (0 <= px - barrierx[b_set][i] <= 50 or 0 <= barrierx[b_set][i] - px <= 100) and (
                    0 <= py - barriery[b_set][i] <= 40 or 0 <= barriery[b_set][i] - py <= 100):
                g += 1
        if check == 0:
            b_set = (b_set + 1) % 3
            barrierx = [[1100.0, 1800, 2300.0, 3000.0], [1500.0, 1600.0, 2400.0, 2400.0, 2800.0],
                        [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
            barriery = [[205.0, 75.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0],
                        [205.0, 205.0, 335.0, 75.0, 205.0, 335.0]]
        if g != 0:
            lifes -= 1
            g = 0
            stop = 1
        lifest = smallfont.render(f"Lifes: {int(lifes)}", True, (0, 0, 0))
        screen.blit(lifest, (250, 0))
        if stop != 0:
            stop = (stop + 1) % 200
        screen.blit(highscoret, (770, 0))
        if lifes == 0:
            screen.blit(gameover, (450, 200))
        if keyboard.is_pressed('up') and move == 0 and lane != 1:
            d = -speed
            move = 1
            lane -= 1
        if keyboard.is_pressed('down') and move == 0 and lane != 3:
            d = speed
            move = 1
            lane += 1
        if move == 1:
            if count >= 129:
                move = 0
                count = -abs(d)
            py += d
            count += abs(d)
        pygame.display.update()
        if lifes == 0:
            file = open("cars_highscore", "w")
            file.write(str(highscore))
            file.close()
            file = open("cars_coins", "w")
            file.write(str(coins))
            file.close()
            time.sleep(1)
            menu()


def car3():
    try:
        coins = int(open("cars_coins").read())
        prevcoins = coins
    except:
        file = open("cars_coins", "w")
        file.write("100")
        file.close()
        coins = 100
        prevcoins = 100
    try:
        highscore = int(open("cars_highscore").read())
    except:
        file = open("cars_highscore", "w")
        file.write("0")
        file.close()
        highscore = 0
    px, py = 120.0, 175.0
    lane = 2
    speed = 1.7
    q1x, q2x = 70.0, 870.0
    bright1, bright2 = 100, 0
    d = 0
    move = 0
    count = 0
    lifes = 4
    score = 0
    stop = 0
    coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
    coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
    collected = [0 for i in range(11)]
    barrierx = [[1700.0, 2300.0, 3000.0], [1500.0, 1600.0, 2900.0, 2400.0, 800.0],
                [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
    barriery = [[205.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0], [205.0, 205.0, 335.0, 75.0, 335.0, 335.0]]
    b_set = 0
    check = 0
    gameover = largefont.render("GAME OVER!", True, red, yellow)
    g = 1
    start = 0
    startt = smallfont.render("Press 'ENTER' to start.", True, red, yellow)
    coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
    while 1:
        screen.fill((20, 10, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(screen, (250, 0, 250), (0, 0, 1100, 30))
        pygame.draw.rect(screen, (250, 250, 250), (0, 30, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 160, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 290, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 420, 1100, 20))
        pygame.draw.circle(screen, (bright1, 200, 0), (int(q1x), 40), 8)
        pygame.draw.circle(screen, (200, bright2, 0), (int(q1x), 300), 8)
        pygame.draw.circle(screen, (200, bright1, 0), (int(q2x), 170), 8)
        pygame.draw.circle(screen, (bright2, 200, 0), (int(q2x), 430), 8)
        screen.blit(car_3s, (int(px), int(py)))
        screen.blit(coin, (0, 0))
        if start == 0:
            screen.blit(startt, (440, 200))
            pygame.display.update()
            time.sleep(0.1)
            if keyboard.is_pressed('enter'):
                start = 1
            continue
        q1x = (q1x - speed) % 1600
        q2x = (q2x - speed) % 1600
        bright1 = (bright1 + 1) % 200
        bright2 = (bright2 + 1) % 200
        score += 1
        check = 0
        if score > highscore:
            highscore = score
        if score % 2000 == 0:
            speed += 0.1 * speed
        scoret = smallfont.render(f"Score: {int(score)}", True, yellow, red)
        highscoret = smallfont.render(f"Highscore: {int(highscore)}", True, (0, 0, 0))
        screen.blit(scoret, (470, 0))
        for i in range(11):
            if collected[i] == 0:
                if coinx[i] <= 1100:
                    screen.blit(coin_p, (int(coinx[i]), int(coiny[i])))
                coinx[i] -= speed
                if (0 <= px - coinx[i] <= 50 or 0 <= coinx[i] - px <= 100) and (
                        0 <= py - coiny[i] <= 40 or 0 <= coiny[i] - py <= 100):
                    coins += 15
                    collected[i] = 1
                if coinx[i] <= -100:
                    collected[i] = 1
        coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
        if collected.count(0) == 0:
            coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
            coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
            collected = [0 for i in range(11)]
        for i in range(len(barriery[b_set])):
            screen.blit(barrier_p, (int(barrierx[b_set][i]), int(barriery[b_set][i])))
            barrierx[b_set][i] -= speed
            if barrierx[b_set][i] >= -100:
                check += 1
            if (not stop) and (0 <= px - barrierx[b_set][i] <= 50 or 0 <= barrierx[b_set][i] - px <= 100) and (
                    0 <= py - barriery[b_set][i] <= 40 or 0 <= barriery[b_set][i] - py <= 100):
                g += 1
        if check == 0:
            b_set = (b_set + 1) % 3
            barrierx = [[1100.0, 1800, 2300.0, 3000.0], [1500.0, 1600.0, 2400.0, 2400.0, 2800.0],
                        [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
            barriery = [[205.0, 75.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0],
                        [205.0, 205.0, 335.0, 75.0, 205.0, 335.0]]
        if g != 0:
            lifes -= 1
            g = 0
            stop = 1
        lifest = smallfont.render(f"Lifes: {int(lifes)}", True, (0, 0, 0))
        screen.blit(lifest, (250, 0))
        if stop != 0:
            stop = (stop + 1) % 200
        screen.blit(highscoret, (770, 0))
        if lifes == 0:
            screen.blit(gameover, (450, 200))
        if keyboard.is_pressed('up') and move == 0 and lane != 1:
            d = -speed
            move = 1
            lane -= 1
        if keyboard.is_pressed('down') and move == 0 and lane != 3:
            d = speed
            move = 1
            lane += 1
        if move == 1:
            if count >= 129:
                move = 0
                count = -abs(d)
            py += d
            count += abs(d)
        pygame.display.update()
        if lifes == 0:
            file = open("cars_highscore", "w")
            file.write(str(highscore))
            file.close()
            file = open("cars_coins", "w")
            file.write(str(coins))
            file.close()
            time.sleep(1)
            menu()


def car2():
    try:
        coins = int(open("cars_coins").read())
        prevcoins = coins
    except:
        file = open("cars_coins", "w")
        file.write("100")
        file.close()
        coins = 100
        prevcoins = 100
    try:
        highscore = int(open("cars_highscore").read())
    except:
        file = open("cars_highscore", "w")
        file.write("0")
        file.close()
        highscore = 0
    px, py = 120.0, 175.0
    lane = 2
    speed = 1.2
    q1x, q2x = 70.0, 870.0
    bright1, bright2 = 100, 0
    d = 0
    move = 0
    count = 0
    lifes = 3
    score = 0
    stop = 0
    coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
    coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
    collected = [0 for i in range(11)]
    barrierx = [[1700.0, 2300.0, 3000.0], [1500.0, 1600.0, 2900.0, 2400.0, 800.0],
                [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
    barriery = [[205.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0], [205.0, 205.0, 335.0, 75.0, 335.0, 335.0]]
    b_set = 0
    check = 0
    gameover = largefont.render("GAME OVER!", True, red, yellow)
    g = 1
    start = 0
    startt = smallfont.render("Press 'ENTER' to start.", True, red, yellow)
    coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
    while 1:
        screen.fill((20, 10, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(screen, (250, 0, 250), (0, 0, 1100, 30))
        pygame.draw.rect(screen, (250, 250, 250), (0, 30, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 160, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 290, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 420, 1100, 20))
        pygame.draw.circle(screen, (bright1, 200, 0), (int(q1x), 40), 8)
        pygame.draw.circle(screen, (200, bright2, 0), (int(q1x), 300), 8)
        pygame.draw.circle(screen, (200, bright1, 0), (int(q2x), 170), 8)
        pygame.draw.circle(screen, (bright2, 200, 0), (int(q2x), 430), 8)
        screen.blit(car_2s, (int(px), int(py)))
        screen.blit(coin, (0, 0))
        if start == 0:
            screen.blit(startt, (440, 200))
            pygame.display.update()
            time.sleep(0.1)
            if keyboard.is_pressed('enter'):
                start = 1
            continue
        q1x = (q1x - speed) % 1600
        q2x = (q2x - speed) % 1600
        bright1 = (bright1 + 1) % 200
        bright2 = (bright2 + 1) % 200
        score += 2
        check = 0
        if score > highscore:
            highscore = score
        if score % 2000 == 0:
            speed += 0.1 * speed
        scoret = smallfont.render(f"Score: {int(score)}", True, yellow, red)
        highscoret = smallfont.render(f"Highscore: {int(highscore)}", True, (0, 0, 0))
        screen.blit(scoret, (470, 0))
        for i in range(11):
            if collected[i] == 0:
                if coinx[i] <= 1100:
                    screen.blit(coin_p, (int(coinx[i]), int(coiny[i])))
                coinx[i] -= speed
                if (0 <= px - coinx[i] <= 50 or 0 <= coinx[i] - px <= 100) and (
                        0 <= py - coiny[i] <= 40 or 0 <= coiny[i] - py <= 100):
                    coins += 10
                    collected[i] = 1
                if coinx[i] <= -100:
                    collected[i] = 1
        coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
        if collected.count(0) == 0:
            coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
            coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
            collected = [0 for i in range(11)]
        for i in range(len(barriery[b_set])):
            screen.blit(barrier_p, (int(barrierx[b_set][i]), int(barriery[b_set][i])))
            barrierx[b_set][i] -= speed
            if barrierx[b_set][i] >= -100:
                check += 1
            if (not stop) and (0 <= px - barrierx[b_set][i] <= 50 or 0 <= barrierx[b_set][i] - px <= 100) and (
                    0 <= py - barriery[b_set][i] <= 40 or 0 <= barriery[b_set][i] - py <= 100):
                g += 1
        if check == 0:
            b_set = (b_set + 1) % 3
            barrierx = [[1100.0, 1800, 2300.0, 3000.0], [1500.0, 1600.0, 2400.0, 2400.0, 2800.0],
                        [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
            barriery = [[205.0, 75.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0],
                        [205.0, 205.0, 335.0, 75.0, 205.0, 335.0]]
        if g != 0:
            lifes -= 1
            g = 0
            stop = 1
        lifest = smallfont.render(f"Lifes: {int(lifes)}", True, (0, 0, 0))
        screen.blit(lifest, (250, 0))
        if stop != 0:
            stop = (stop + 1) % 200
        screen.blit(highscoret, (770, 0))
        if lifes == 0:
            screen.blit(gameover, (450, 200))
        if keyboard.is_pressed('up') and move == 0 and lane != 1:
            d = -speed
            move = 1
            lane -= 1
        if keyboard.is_pressed('down') and move == 0 and lane != 3:
            d = speed
            move = 1
            lane += 1
        if move == 1:
            if count >= 129:
                move = 0
                count = -abs(d)
            py += d
            count += abs(d)
        pygame.display.update()
        if lifes == 0:
            file = open("cars_highscore", "w")
            file.write(str(highscore))
            file.close()
            file = open("cars_coins", "w")
            file.write(str(coins))
            file.close()
            time.sleep(1)
            menu()


def car1():
    try:
        coins = int(open("cars_coins").read())
        prevcoins = coins
    except:
        file = open("cars_coins", "w")
        file.write("100")
        file.close()
        coins = 100
        prevcoins = 100
    try:
        highscore = int(open("cars_highscore").read())
    except:
        file = open("cars_highscore", "w")
        file.write("0")
        file.close()
        highscore = 0
    px, py = 120.0, 175.0
    lane = 2
    speed = 0.9
    q1x, q2x = 70.0, 870.0
    bright1, bright2 = 100, 0
    d = 0
    move = 0
    count = 0
    lifes = 3
    score = 0
    stop = 0
    coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
    coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
    collected = [0 for i in range(11)]
    barrierx = [[1700.0, 2300.0, 3000.0], [1500.0, 1600.0, 2900.0, 2400.0, 800.0],
                [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
    barriery = [[205.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0], [205.0, 205.0, 335.0, 75.0, 335.0, 335.0]]
    b_set = 0
    check = 0
    gameover = largefont.render("GAME OVER!", True, red, yellow)
    g = 1
    start = 0
    startt = smallfont.render("Press 'ENTER' to start.", True, red, yellow)
    coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
    while 1:
        screen.fill((20, 10, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(screen, (250, 0, 250), (0, 0, 1100, 30))
        pygame.draw.rect(screen, (250, 250, 250), (0, 30, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 160, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 290, 1100, 20))
        pygame.draw.rect(screen, (250, 250, 250), (0, 420, 1100, 20))
        pygame.draw.circle(screen, (bright1, 200, 0), (int(q1x), 40), 8)
        pygame.draw.circle(screen, (200, bright2, 0), (int(q1x), 300), 8)
        pygame.draw.circle(screen, (200, bright1, 0), (int(q2x), 170), 8)
        pygame.draw.circle(screen, (bright2, 200, 0), (int(q2x), 430), 8)
        screen.blit(car_1s, (int(px), int(py)))
        screen.blit(coin, (0, 0))
        if start == 0:
            screen.blit(startt, (440, 200))
            pygame.display.update()
            time.sleep(0.1)
            if keyboard.is_pressed('enter'):
                start = 1
            continue
        q1x = (q1x - speed) % 1600
        q2x = (q2x - speed) % 1600
        bright1 = (bright1 + 1) % 200
        bright2 = (bright2 + 1) % 200
        score += 1
        check = 0
        if score > highscore:
            highscore = score
        if score % 2000 == 0:
            speed += 0.1 * speed
        scoret = smallfont.render(f"Score: {int(score)}", True, yellow, red)
        highscoret = smallfont.render(f"Highscore: {int(highscore)}", True, (0, 0, 0))
        screen.blit(scoret, (470, 0))
        for i in range(11):
            if collected[i] == 0:
                if coinx[i] <= 1100:
                    screen.blit(coin_p, (int(coinx[i]), int(coiny[i])))
                coinx[i] -= speed
                if (0 <= px - coinx[i] <= 50 or 0 <= coinx[i] - px <= 100) and (
                        0 <= py - coiny[i] <= 40 or 0 <= coiny[i] - py <= 100):
                    coins += 10
                    collected[i] = 1
                if coinx[i] <= -100:
                    collected[i] = 1
        coin = smallfont.render(f"COINS: {coins - prevcoins}", True, yellow, red)
        if collected.count(0) == 0:
            coinx = [1150.0, 1550.0, 1750.0, 2050.0, 2050.0, 2550.0, 2950.0, 3550.0, 3950.0, 4550.0, 5150.0]
            coiny = [205.0, 75.0, 75.0, 335.0, 205.0, 75.0, 335.0, 205.0, 205.0, 75.0, 335.0]
            collected = [0 for i in range(11)]
        for i in range(len(barriery[b_set])):
            screen.blit(barrier_p, (int(barrierx[b_set][i]), int(barriery[b_set][i])))
            barrierx[b_set][i] -= speed
            if barrierx[b_set][i] >= -100:
                check += 1
            if (not stop) and (0 <= px - barrierx[b_set][i] <= 50 or 0 <= barrierx[b_set][i] - px <= 100) and (
                    0 <= py - barriery[b_set][i] <= 40 or 0 <= barriery[b_set][i] - py <= 100):
                g += 1
        if check == 0:
            b_set = (b_set + 1) % 3
            barrierx = [[1100.0, 1800, 2300.0, 3000.0], [1500.0, 1600.0, 2400.0, 2400.0, 2800.0],
                        [1300.0, 1700.0, 1700.0, 2100.0, 2100.0, 2400.0]]
            barriery = [[205.0, 75.0, 335.0, 205.0], [75.0, 335.0, 205.0, 75.0, 335.0],
                        [205.0, 205.0, 335.0, 75.0, 205.0, 335.0]]
        if g != 0:
            lifes -= 1
            g = 0
            stop = 1
        lifest = smallfont.render(f"Lifes: {int(lifes)}", True, (0, 0, 0))
        screen.blit(lifest, (250, 0))
        if stop != 0:
            stop = (stop + 1) % 200
        screen.blit(highscoret, (770, 0))
        if lifes == 0:
            screen.blit(gameover, (450, 200))
        if keyboard.is_pressed('up') and move == 0 and lane != 1:
            d = -speed
            move = 1
            lane -= 1
        if keyboard.is_pressed('down') and move == 0 and lane != 3:
            d = speed
            move = 1
            lane += 1
        if move == 1:
            if count >= 129:
                move = 0
                count = -abs(d)
            py += d
            count += abs(d)
        pygame.display.update()
        if lifes == 0:
            file = open("cars_highscore", "w")
            file.write(str(highscore))
            file.close()
            file = open("cars_coins", "w")
            file.write(str(coins))
            file.close()
            time.sleep(1)
            menu()


def play(car):
    if car == 0:
        car1()
    elif car == 1:
        car2()
    elif car == 2:
        car3()
    elif car == 3:
        car4()


def store():
    try:
        coins = int(open("cars_coins").read())
    except:
        file = open("cars_coins", "w")
        file.write("100")
        file.close()
        coins = 100
    try:
        purchased = open("cars_purchased").read()
        purchased = [int(i) for i in purchased.split()]
    except:
        file = open("cars_purchased", "w")
        file.write("1 0 0 0")
        file.close()
        purchased = [1, 0, 0, 0]
    try:
        position = int(open("cars_pos").read())
    except:
        file = open("cars_pos", "w")
        file.write("0")
        file.close()
        position = 0
    rate = [0, 1500, 5000, 15000]
    sleep = 0
    car = 0
    text = largefont.render('STORE:', True, red, blue)
    textrect = text.get_rect()
    textrect.center = (550, 40)
    cointext = smallfont.render('Coins: $' + str(coins), True, (0, 0, 0), yellow)
    ctext1 = smallfont.render('4-Wheeler', True, red, blue)
    ctext2 = smallfont.render('Jeep', True, red, blue)
    ctext3 = smallfont.render('Racing Car', True, red, blue)
    ctext4 = smallfont.render('Tank', True, red, blue)
    ctext1rect = ctext1.get_rect()
    ctext1rect.center = (175, 105)
    ctext2rect = ctext2.get_rect()
    ctext2rect.center = (425, 105)
    ctext3rect = ctext3.get_rect()
    ctext3rect.center = (675, 105)
    ctext4rect = ctext4.get_rect()
    ctext4rect.center = (925, 105)
    c1pur = smallfont.render('Purchased', True, (0, 0, 0))
    if purchased[1] == 0:
        c2pur = smallfont.render('$1500', True, (0, 0, 0))
    else:
        c2pur = smallfont.render('Purchased', True, (0, 0, 0))
    if purchased[2] == 0:
        c3pur = smallfont.render('$5000', True, (0, 0, 0))
    else:
        c3pur = smallfont.render('Purchased', True, (0, 0, 0))
    if purchased[3] == 0:
        c4pur = smallfont.render('$15000', True, (0, 0, 0))
    else:
        c4pur = smallfont.render('Purchased', True, (0, 0, 0))
    c1purrect = c1pur.get_rect()
    c1purrect.center = (175, 320)
    c2purrect = c2pur.get_rect()
    c2purrect.center = (420, 320)
    c3purrect = c3pur.get_rect()
    c3purrect.center = (670, 320)
    c4purrect = c4pur.get_rect()
    c4purrect.center = (920, 320)
    minifont = pygame.font.Font('freesansbold.ttf', 20)
    feature = smallfont.render('Features:', True, blue)
    speed1 = minifont.render('Speed: 80 kmph', True, (0, 0, 0))
    speed2 = minifont.render('Speed: 100 kmph', True, (0, 0, 0))
    speed3 = minifont.render('Speed: 160 kmph', True, (0, 0, 0))
    speed4 = minifont.render('Speed: 80 kmph', True, (0, 0, 0))
    life1 = minifont.render('Lifes: 2', True, (0, 0, 0))
    life2 = minifont.render('Lifes: 2', True, (0, 0, 0))
    life3 = minifont.render('Lifes: 3', True, (0, 0, 0))
    life4 = minifont.render('Lifes: 5', True, (0, 0, 0))
    special1 = minifont.render('Special: Nil', True, (0, 0, 0))
    special2 = minifont.render('Special: Score= 2X', True, (0, 0, 0))
    special3 = minifont.render('Special: Coins= 1.5X', True, (0, 0, 0))
    special4 = minifont.render('Special: 5 lifes', True, (0, 0, 0))
    goback = minifont.render('Press "shift" or "0" to go back', True, (0, 0, 0), yellow)
    while 1:
        screen.fill((250, 80, 0))
        screen.blit(text, textrect)
        screen.blit(cointext, (0, 0))
        screen.blit(goback, (800, 0))
        screen.blit(ctext1, ctext1rect)
        screen.blit(ctext2, ctext2rect)
        screen.blit(ctext3, ctext3rect)
        screen.blit(ctext4, ctext4rect)
        if purchased[1] == 0:
            c2pur = smallfont.render('$1500', True, (0, 0, 0))
        else:
            c2pur = smallfont.render('Purchased', True, (0, 0, 0))
        if purchased[2] == 0:
            c3pur = smallfont.render('$5000', True, (0, 0, 0))
        else:
            c3pur = smallfont.render('Purchased', True, (0, 0, 0))
        if purchased[3] == 0:
            c4pur = smallfont.render('$15000', True, (0, 0, 0))
        else:
            c4pur = smallfont.render('Purchased', True, (0, 0, 0))
        c1purrect = c1pur.get_rect()
        c1purrect.center = (175, 320)
        c2purrect = c2pur.get_rect()
        c2purrect.center = (425, 320)
        c3purrect = c3pur.get_rect()
        c3purrect.center = (675, 320)
        c4purrect = c4pur.get_rect()
        c4purrect.center = (925, 320)
        if keyboard.is_pressed('enter'):
            if purchased[position] == 1:
                sleep = 1
                stext = largefont.render("Selected", True, (0, 0, 0), (250, 200, 200))
                car = position
                file = open("cars_pos", "w")
                file.write(str(position))
                file.close()
            elif coins >= rate[position]:
                purchased[position] = 1
                file = open("cars_purchased", "w")
                file.write(
                    str(purchased[0]) + " " + str(purchased[1]) + " " + str(purchased[2]) + " " + str(purchased[3]))
                file.close()
                coins -= rate[position]
                cointext = smallfont.render('Coins: $' + str(coins), True, (0, 0, 0), yellow)
                file = open("cars_coins", "w")
                file.write(str(coins))
                file.close()
                car = position
                file = open("cars_pos", "w")
                file.write(str(position))
                file.close()
                sleep = 1
                stext = largefont.render("Purchased", True, (0, 0, 0), (250, 200, 200))
            else:
                sleep = 1
                stext = largefont.render("Earn More :(", True, (0, 0, 0), (250, 200, 200))
        if keyboard.is_pressed('shift') or keyboard.is_pressed('0'):
            return car
        if keyboard.is_pressed('right'):
            position = (position + 1) % 4
            time.sleep(0.2)
        elif keyboard.is_pressed('left'):
            position = (position - 1) % 4
            time.sleep(0.2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for i in [50, 300, 550, 800]:
            pygame.draw.rect(screen, green, (i + 25, 120, 200, 180))
            screen.blit(feature, (i + 55, 330))
        pygame.draw.rect(screen, yellow, (position * 250 + 75, 120, 200, 180))
        screen.blit(car_1s, (75 + 36, 120 + 36))
        screen.blit(car_2s, (325 + 36, 120 + 36))
        screen.blit(car_3s, (575 + 36, 120 + 36))
        screen.blit(car_4s, (825 + 36, 120 + 36))
        screen.blit(c1pur, c1purrect)
        screen.blit(c2pur, c2purrect)
        screen.blit(c3pur, c3purrect)
        screen.blit(c4pur, c4purrect)
        screen.blit(speed1, (100, 360))
        screen.blit(speed2, (350, 360))
        screen.blit(speed3, (600, 360))
        screen.blit(speed4, (850, 360))
        screen.blit(life1, (100, 380))
        screen.blit(life2, (350, 380))
        screen.blit(life3, (600, 380))
        screen.blit(life4, (850, 380))
        screen.blit(special1, (100, 400))
        screen.blit(special2, (350, 400))
        screen.blit(special3, (600, 400))
        screen.blit(special4, (850, 400))
        if sleep:
            screen.blit(stext, (450, 200))
        pygame.display.update()
        if sleep:
            sleep = 0
            time.sleep(0.5)


def menu():
    position = 0
    bright = 0
    r = 0
    increase = 1
    try:
        car = int(open("cars_pos").read())
    except:
        file = open("cars_pos", "w")
        file.write("0")
        file.close()
        car = 0
    while 1:
        r = (r + 1) % 150
        if increase == 1:
            bright = bright + 1
            if bright == 199:
                increase = 0
        else:
            bright -= 1
            if bright == 0:
                increase = 1
        screen.fill((r, 255, bright))
        screen.blit(text_menu, text_menu_rect)
        screen.blit(text_play, text_play_rect)
        screen.blit(text_store, text_store_rect)
        screen.blit(stats, stats_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if keyboard.is_pressed('enter'):
            if position == 0:
                play(car)
            elif position == 1:
                car = store()
            else:
                openstats()
        if keyboard.is_pressed('down'):
            position = (position + 1) % 3
            time.sleep(0.2)
        elif keyboard.is_pressed('up'):
            position = (position - 1) % 3
            time.sleep(0.2)
        if position == 0:
            text_play_dup = smallfont.render('PLAY', True, yellow, red)
            text_play_dup_rect = text_play.get_rect()
            text_play_dup_rect.center = (550, 160)
            screen.blit(text_play_dup, text_play_dup_rect)
        elif position == 1:
            text_store_dup = smallfont.render('STORE', True, yellow, red)
            text_store_dup_rect = text_store.get_rect()
            text_store_dup_rect.center = (550, 210)
            screen.blit(text_store_dup, text_store_dup_rect)
        else:
            stats_dup = smallfont.render('STATS', True, yellow, red)
            stats_dup_rect = stats.get_rect()
            stats_dup_rect.center = (550, 260)
            screen.blit(stats_dup, stats_dup_rect)
        pygame.display.update()


def openstats():
    try:
        highscore = int(open("cars_highscore").read())
    except:
        highscore = 0
    try:
        coins = int(open("cars_coins").read())
    except:
        coins = 0
    stat = largefont.render("STATS:", True, red, yellow)
    hs = smallfont.render(f"Highscore: {highscore}", True, (0, 0, 0))
    cs = smallfont.render(f"Coins Left: {coins}", True, (0, 0, 0))
    gb = minifont.render("Press '0' or 'SHIFT' to go back", True, (0, 0, 0), yellow)
    ms = smallfont.render("     ~This game is developed by ANKAN MAHAPATRA", True, (0, 0, 0))
    while 1:
        screen.fill((250, 0, 250))
        screen.blit(stat, (460, 60))
        screen.blit(hs, (430, 150))
        screen.blit(cs, (430, 200))
        screen.blit(ms, (250, 300))
        screen.blit(gb, (800, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if keyboard.is_pressed("0") or keyboard.is_pressed("shift"):
            return
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((1100, 440))
pygame.display.set_caption("car_game")
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
largefont = pygame.font.Font('freesansbold.ttf', 50)
smallfont = pygame.font.Font('freesansbold.ttf', 30)
minifont = pygame.font.Font('freesansbold.ttf', 20)
text_menu = largefont.render('MAIN MENU:', True, red, blue)
text_play = smallfont.render('PLAY', True, yellow, blue)
text_store = smallfont.render('STORE', True, yellow, blue)
stats = smallfont.render('STATS', True, yellow, blue)
text_menu_rect = text_menu.get_rect()
text_play_rect = text_play.get_rect()
text_store_rect = text_store.get_rect()
stats_rect = stats.get_rect()
text_menu_rect.center = (550, 80)
text_play_rect.center = (550, 160)
text_store_rect.center = (550, 210)
stats_rect.center = (550, 260)
car_1s = pygame.image.load(r'car_1s.png')
car_2s = pygame.image.load(r'car_2s.png')
car_3s = pygame.image.load(r'car_3s.png')
car_4s = pygame.image.load(r'car_4s.png')
barrier_p = pygame.image.load(r'traffic-cone.png')
coin_p = pygame.image.load(r'wealth.png')
position = 0
menu()
