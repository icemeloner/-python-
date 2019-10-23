import sys, pygame
from pygame import *
import threading
import time
import os


from PIL import ImageTk, Image

pygame.init()
size = width, height = 500, 330
window = pygame.display.set_mode(size)


def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files


imagebox = []
Path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat10"
files = getfiles(Path)
for i in range(0, 50):
    imagebox.append(pygame.image.load(Path + '\\' + files[i]))
def toc(t1):
    t = time.time()
    return (t-t1)*1000
t = 5000
t1 = time.time()
t2 = 0
for i in range(0, 50):
    while t2 < t * i:
        t2 = toc(t1)
        # for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_RIGHT:
                print('right')
                t2 = t*i
                print(t2)
                continue

                #
                # # 检测按键是否是d或者right
                # elif event.key == K_d or event.key == K_RIGHT:
                #     print('right')
                # # 检测按键是否是w或者up
                # elif event.key == K_w or event.key == K_UP:
                #     print("up")
                # # 检测按键是否是s或者down
                # elif event.key == K_s or event.key == K_DOWN:
                #     print("down")
                #
                # # 检测按键是否是空格键
                # elif event.key == K_SPACE:
                #     print('space')

    window.blit(imagebox[i], (0, 0))
    print(t2)
    pygame.display.update()

