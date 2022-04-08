import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('moving.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()

