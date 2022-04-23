# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:17:22 2022

@author: lucas
"""


import time
#import pygame, sys



croplist = []
crop_img = '| ~ |'
milho_img = ['| . |', '| ; |', '| Y |']

    
class cronometro:
    def __init__(self, t, event):
        self.t = t
        self.event = event
        while t: # while t > 0 for clarity 
            mins = t // 60
            secs = t % 60
            timer = ' {:02d}:{:02d} '.format(mins, secs)
            print(timer) # overwrite previous line 
            time.sleep(1)
            t -= 1
        event

class farm: #Criador de canteiro
    def __init__(self, qt):
        self.qt = qt
        def farmer():
            for _ in range(qt):
                croplist.append(crop_img)
        farmer()
        
        
class planter: #Plantador
    def __init__(self, alvo, estagio):
        self.estagio = estagio
        self.alvo = alvo
        croplist[self.alvo] = milho_img[estagio]
        

class menu_a:
    def __init__(self):
        print("Bem vindo à fazenda!")
        #global temporada
        #temporada = int(input('Temporada rápida(3min) ou média(6min)?'))
        global qt_canteiro
        qt_canteiro = int(input('Quantos canteiros gostaria de preparar? nº: '))
        
class jogo_a:
    def __init__(self):
        def jogo_inicio():
            cronometro(10, None)
            farm(qt_canteiro)
            print(croplist)
            print('Canteiros preparados!')
            
        def jogo_meio():
            planteiro = input('Plantar sementes de milho? s/n: ')
            if planteiro == 's':
                while croplist.count(crop_img) != 0: 
                    alvo_planter = croplist.index(crop_img)
                    planter(alvo_planter, 0)
                print(croplist)
                print('Sementes plantadas!')
            
        def brotamento():
            while croplist.count(milho_img[0]) != 0: 
                alvo_planter = croplist.index(milho_img[0])
                planter(alvo_planter, 1)
            print(croplist)
            print('As mudas cresceram!')
            
        def planta():
            while croplist.count(milho_img[1]) != 0: 
                alvo_planter = croplist.index(milho_img[1])
                planter(alvo_planter, 2)
            print(croplist)
            print('Pronto para colheita!')
            
        def colher():
            harvest = input('Deseja colher? s/n: ')
            if harvest == 's':
                cronometro(5, None)
                while croplist.count(milho_img[2]) != 0: 
                    alvo_planter = croplist.index(milho_img[2])
                    croplist.pop(alvo_planter)
                    x = qt_canteiro
            print('Colheita completa!')
            print(f'Foram colhidas {x} plantas!')
                

                
        jogo_inicio()
        jogo_meio()
        cronometro(5, None)
        brotamento()
        cronometro(5, None)
        planta()
        colher()
            
jogar = input('Gostaria de jogar? s/n: ')
while jogar == 's':
    menu_a()
    jogo_a()
    jogar = input('Gostaria de jogar? s/n: ')


# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode([500, 500])
# base_font = pygame.font.Font(None, 32)
# user_text = ''

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             user_text += event.unicode
    
#     screen.fill((0, 0, 0))
#     text_surface = base_font.render(user_text, True, (255, 255, 255))
#     screen.blit(text_surface, (0, 0))
    
#     pygame.display.flip()
#     clock.tick(60)
            
                
                
                
#https://youtu.be/Rvcyf4HsWiw 
                
                
                
                
            