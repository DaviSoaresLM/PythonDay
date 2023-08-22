#Faça um programa em Python que abra a e reproduza o aúdio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('ashley.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()