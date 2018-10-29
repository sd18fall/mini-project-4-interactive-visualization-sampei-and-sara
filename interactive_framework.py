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


def bpm_to_frame(bpm):
    bps = 60 / bpm
    frames = bps * 24
    return frames

def key_q(key, frames):
    for frame in range(1,frames):
        to_display = pygame.image.load('/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/ComputationalArt-sampeiomichi/movie1_'+str(frame)+'.png')
        gameDisplay.blit(to_display, (0,0))
        pygame.time.delay(24)
        pygame.display.update()

def key_w(key, frames):
    for frame in range(1,frames):
        to_display = pygame.image.load('/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/ComputationalArt-sampeiomichi/movie2_'+str(frame)+'.png')
        gameDisplay.blit(to_display, (0,0))
        pygame.time.delay(24)
        pygame.display.update()

def key_e(key, frames):
    for frame in range(1,frames):
        to_display = pygame.image.load('/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/ComputationalArt-sampeiomichi/movie3_'+str(frame)+'.png')
        gameDisplay.blit(to_display, (0,0))
        pygame.time.delay(24)
        pygame.display.update()

if __name__ == "__main__": # Controller

    frames = int(bpm_to_frame(60))

    pygame.init()
    display_width = 350
    display_height = 350

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    end = False
    while not end:
        key = 'x'
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
        if key == ord('q'):
            print('q')
        if key == ord('h'):
            print('h')

                # while key == ord('w'):
                #     print('Colors Inverted!')
                #     key_w(key, frames)
                # while key == ord('e'):
                #     print('Image Greyscaled!')
                #     key_e(key, frames)
