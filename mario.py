import pygame
import sys

pygame.init()
pygame.mixer.init()

running = True
pause = False

audio_super = pygame.mixer.music.load("super.mp3")
pygame.mixer.music.play()
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)
keys = pygame.key.get_pressed()


largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

xGround = 0
xGround2 = xGround+128
xGround3 = xGround+(128*2)
xGround4 = xGround+(128*3)
xGround5 = xGround+(128*4)
xGround6 = xGround+(128*5)
xGround7 = xGround+(128*6)
xGround8 = xGround+(128*7)
xGround9 = xGround+(128*8)

xNuvem = 800
xNuvem2 = 1600
xPipe = 550
xPipe2 = 150
xBackground = 100
xBackground1 = 200
def keyboard_keydown(keys):
    if keys[pygame.K_i]:
        pygame.mixer.music.play()
    elif keys[pygame.K_m]:
        pygame.mixer.music.pause()
    elif keys[pygame.K_c]:
        pygame.mixer.music.unpause()
    elif keys[pygame.K_u]:
        pygame.mixer.music.stop()

def keyboard_keyup(keys):
    pass


xBackground2 = 450
xBackground3 = 550
xBackground4 = 620
nuvemSpeed = 7
state = running

background = pygame.image.load(r'mario_background.png')
nuvem = pygame.image.load('mario_cloud.png')
ground = pygame.image.load('mario_ground.png')
pipe = pygame.image.load('mario_pipe.png')
tela.fill('Sky Blue')
TelaDePause = pygame.image.load('TelaDePause.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p : state = pause
            if event.key == pygame.K_s: state = running

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                keyboard_keydown(keys)
            if event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                keyboard_keyup(keys)
            
            keyboard_keydown(keys)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if state == True:
        pygame.display.flip()
        tela.fill('Sky Blue')
        tela.blit(background, (xBackground, 230))
        tela.blit(background, (xBackground1, 230))
        tela.blit(background, (xBackground2, 230))
        tela.blit(background, (xBackground3, 230))
        tela.blit(background, (xBackground4, 230))
        tela.blit(nuvem, (xNuvem, 0))
        tela.blit(nuvem, (xNuvem2, 0))
        tela.blit(pipe, (xPipe, 400))
        tela.blit(pipe, (xPipe2, 380))
        tela.blit(ground, (xGround, 475))
        tela.blit(ground, (xGround2, 475))
        tela.blit(ground, (xGround3, 475))
        tela.blit(ground, (xGround4, 475))
        tela.blit(ground, (xGround5, 475))
        tela.blit(ground, (xGround6, 475))
        tela.blit(ground, (xGround7, 475))
        tela.blit(ground, (xGround8, 475))
        
        xGround -= 3
        xGround2 -= 3
        xGround3 -= 3
        xGround4 -= 3
        xGround5 -= 3
        xGround6 -= 3
        xGround7 -= 3
        xGround8 -= 3
        xGround9 -= 3
        
        xPipe -= 3
        xPipe2 -= 3
        xNuvem -= nuvemSpeed
        xNuvem2 -= (nuvemSpeed+1)

        xBackground -= 1.5
        xBackground1 -= 1.5
        xBackground2 -= 1
        xBackground3 -= 1.5
        xBackground4 -= 1
    
        #while xGround < 800:
         #   tela.blit(ground, (xGround, 475))
         #   xGround+=80
        #if xGround <= 800:
            #xGround = 0
        pygame.display.update()
        pygame.time.Clock().tick(60)
        if xNuvem <= -250:
            xNuvem = 1000
        if xNuvem2 <= -250:
            xNuvem2 = 2000
        
        if xPipe <= -250:
            xPipe = 800
        if xPipe2 <= -250:
            xPipe2 = 800

        if xBackground < -250:
            xBackground = 800
        if xBackground1 < -250:
            xBackground1 = 950
        if xBackground2 < -250:
            xBackground2 = 925
        if xBackground3 < -250:
            xBackground3 = 915
        if xBackground4 < -250:
            xBackground = 920
            
        if xGround < -125:
            xGround = xGround8+120
        if xGround2 < -125:
            xGround2 = xGround+120
        if xGround3 < -125:
            xGround3 = xGround2+120
        if xGround4 < -125:
            xGround4 = xGround3+120
        if xGround5 < -125:
            xGround5 = xGround4+120
        if xGround6 < -125:
            xGround6 = xGround5+120
        if xGround7 < -125:
            xGround7 = xGround6+120
        if xGround8 < -125:
            xGround8 = xGround7+120
    else:
        tela.fill('Sky Blue')
        tela.blit(TelaDePause, (0, 0))
        pygame.display.flip()
