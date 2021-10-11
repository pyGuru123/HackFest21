from Classes.bubbles import Bubble
from GameConstants.constants import *

size = (40, 20);
row_count = WINDOW_HEIGHT // ((size[1] + 5) * 3)
col_count = WINDOW_WIDTH // size[0] + 5

def test(color=LIGHTBLUE):
    l = []
    bubble = Bubble(size[0], size[1], color)  
    bubble.x = 220
    bubble.y = 200
    l.append(bubble)

    return l


def level1(color=LIGHTBLUE):
    global row_count, col_count, size, score_height
    l = []
    for i in range(row_count):
        for j in range(col_count):
            if ((i+j)&1) : continue
            bubble = Bubble(size[0], size[1], color)
            bubble.x = j*(size[0]+5)
            bubble.y = i*(size[1]+5) + score_height + 2
            l.append(bubble)
    return l


def level2(color=LIGHTBLUE):
    global row_count, col_count, size, score_height
    l = []
    for i in range(row_count // 2):
        spaces = col_count / 2  - 2*i
        bl = col_count / 4 + i
        for j in range(col_count):
            if (bl <= 0 and spaces > 0):
                spaces -= 1
                continue
            else:
                bubble = Bubble(size[0], size[1], color)
                bubble.x = j*(size[0]+5)
                bubble.y = i*(size[1]+5) + score_height + 2
                l.append(bubble)
                bl -= 1
            
    for i in range(0, row_count // 2):
        spaces = col_count // 2  - 2 * (row_count // 2 - i)
        bl = col_count / 4 + (row_count // 2 - i)
        for j in range(col_count):
            if (bl <= 0 and spaces > 0):
                spaces -= 1
                continue
            else:
                bubble = Bubble(size[0], size[1], color)
                bubble.x = j*(size[0]+5)
                bubble.y = i*(size[1]+5) + row_count // 2 * size[0] - size[0] / 2 - 4
                l.append(bubble)
                bl -= 1
        
    return l


def level3(color=LIGHTBLUE):
    global row_count, col_count, size, score_height
    l = []
    for i in range(row_count):
        for j in range(col_count):
            bubble = Bubble(size[0], size[1], color)
            bubble.x = j*(size[0]+5)
            bubble.y = i*(size[1]+5) + score_height + 2
            l.append(bubble)
    return l