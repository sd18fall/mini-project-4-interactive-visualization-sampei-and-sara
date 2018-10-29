"""We are creating an Interactive Music Visualizer users input an MP3 file into
the program which generates a movie with data extracted from the music file.
This program will run prior to playing the movie and music at the same time, and
will preprocess the audio data to generate the Computational Art equations that
will be visualized later on. Then, during the movie (the visualization of these
equations), the user is able to manipulate the movie behavior throughout the
song by interacting with several keys on the keyboard. These keystrokes will
essentially swap colors in the equations but will not involve regenerating
equations."""

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



__author__ = 'Sampei and Sara'
__version__ = '0.0.1'

def get_wav():
    """Controller function - asks for wav file from user and ensures that it is
    a wav file
    """
    got_wav = False
    while got_wav == False:
        wav_file = input('What audio file would you like to visualize?: ')
        if wav_file[-4:] == '.wav':
            return got_wav
        else:
            print('You must enter an WAV file.')

def process_key(key):
    """ Controller function - identifies key input
    """
    print(chr(key))

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

if __name__ == "__main__": #Controller

    WAV_FILE = '/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/pyAudioAnalysis/data/beat/small.wav'
    [Fs, x] = audioBasicIO.readAudioFile(WAV_FILE);
    F, f_names = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
    print(audioFeatureExtraction.beatExtraction(F, 1, PLOT=False))

    frames = 239

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
        if key == ord('z'):
            end = True
        if key == ord('q'):
            print('Regular')
            key_q(key, frames)
        if key == ord('w'):
            print('Colors Inverted!')
            key_w(key, frames)
        if key == ord('e'):
            print('Image Greyscaled!')
            key_e(key, frames)
