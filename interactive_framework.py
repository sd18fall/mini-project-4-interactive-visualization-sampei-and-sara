from __future__ import print_function
import shutil
import ntpath
import wave
import os
import glob
import eyed3
import numpy
from pydub import AudioSegment
import pygame
import matplotlib.pyplot as plt
from pyAudioAnalysis import audioFeatureExtraction
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioAnalysis

def process_key(key):
    """ Controller function - identifies key input
    """
    if key == ord('q'):
        print('Regular')
        key_q()
    if key == ord('w'):
        print('Colors Inverted!')
        key_w()
    if key == ord('e'):
        print('Image Greyscaled!')
        key_e()

def key_q():
    for frame in range(1,239):
        to_display = pygame.image.load('/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/ComputationalArt-sampeiomichi/movie1_'+str(frame)+'.png')
        gameDisplay.blit(to_display, (0,0))
        pygame.time.delay(24)
        pygame.display.update()

def key_w():
    for frame in range(1,239):
        to_display = pygame.image.load('/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/ComputationalArt-sampeiomichi/movie2_'+str(frame)+'.png')
        gameDisplay.blit(to_display, (0,0))
        pygame.time.delay(24)
        pygame.display.update()

def key_e():
    for frame in range(1,239):
        to_display = pygame.image.load('/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/ComputationalArt-sampeiomichi/movie3_'+str(frame)+'.png')
        gameDisplay.blit(to_display, (0,0))
        pygame.time.delay(24)
        pygame.display.update()

if __name__ == "__main__": #Controller

    pygame.init()
    display_width = 350
    display_height = 350

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('z'):
                    end = True
                else:
                    process_key(event.key)
