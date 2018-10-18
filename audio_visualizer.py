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
import pygame
import os, glob, eyed3, ntpath, shutil, numpy
import wave
from pydub import AudioSegment
from pyAudioAnalysis import utilities

__author__ = 'Sampei and Sara '
__version__ = '0.0.1'

def get_wav():
    got_wav = False
    while got_wav == False:
        wav_file = input('What audio file would you like to visualize?: ')
        if wav_file[-4:] == '.wav':
            return got_wav
        else:
            print('You must enter an WAV file.')

def input_audio_file(path):
    '''Gets a path for an wav file and returns a numpy array that represents
    the audio file.'''
    extension = os.path.splitext(path)[1]
    try:
        if extension.lower() == '.wav':
            try:
                audiofile = AudioSegment.from_file(path)
            #except pydub.exceptions.CouldntDecodeError:
            except:
                print("Error: file not found or other I/O error. "
                      "(DECODING FAILED)")
                return (-1,-1)

            if audiofile.sample_width==2:
                data = numpy.fromstring(audiofile._data, numpy.int16)
            elif audiofile.sample_width==4:
                data = numpy.fromstring(audiofile._data, numpy.int32)
            else:
                return (-1, -1)
            Fs = audiofile.frame_rate
            x = []
            for chn in list(range(audiofile.channels)):
                x.append(data[chn::audiofile.channels])
            x = numpy.array(x).T
        else:
            print("Error in readAudioFile(): Unknown file type!")
            return (-1,-1)

    except IOError:
        print("Error: file not found or other I/O error.")
        return (-1,-1)

    if x.ndim==2:
        if x.shape[1]==1:
            x = x.flatten()

    return Fs, x

def beatExtraction(st_features, win_len, PLOT=False):
    """
    This function extracts an estimate of the beat rate for a musical signal.
    ARGUMENTS:
     - st_features:     a numpy array (n_feats x numOfShortTermWindows)
     - win_len:        window size in seconds
    RETURNS:
     - BPM:            estimates of beats per minute
     - Ratio:          a confidence measure
    """

    # Features that are related to the beat tracking task:
    toWatch = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    max_beat_time = int(round(2.0 / win_len))
    hist_all = numpy.zeros((max_beat_time,))
    for ii, i in enumerate(toWatch):                                        # for each feature
        DifThres = 2.0 * (numpy.abs(st_features[i, 0:-1] - st_features[i, 1::])).mean()    # dif threshold (3 x Mean of Difs)
        if DifThres<=0:
            DifThres = 0.0000000000000001
        [pos1, _] = utilities.peakdet(st_features[i, :], DifThres)           # detect local maxima
        posDifs = []                                                        # compute histograms of local maxima changes
        for j in range(len(pos1)-1):
            posDifs.append(pos1[j+1]-pos1[j])
        [hist_times, HistEdges] = numpy.histogram(posDifs, numpy.arange(0.5, max_beat_time + 1.5))
        hist_centers = (HistEdges[0:-1] + HistEdges[1::]) / 2.0
        hist_times = hist_times.astype(float) / st_features.shape[1]
        hist_all += hist_times
        if PLOT:
            plt.subplot(9, 2, ii + 1)
            plt.plot(st_features[i, :], 'k')
            for k in pos1:
                plt.plot(k, st_features[i, k], 'k*')
            f1 = plt.gca()
            f1.axes.get_xaxis().set_ticks([])
            f1.axes.get_yaxis().set_ticks([])

    if PLOT:
        plt.show(block=False)
        plt.figure()

    # Get beat as the argmax of the agregated histogram:
    I = numpy.argmax(hist_all)
    bpms = 60 / (hist_centers * win_len)
    BPM = bpms[I]
    # ... and the beat ratio:
    Ratio = hist_all[I] / hist_all.sum()

    if PLOT:
        # filter out >500 beats from plotting:
        hist_all = hist_all[bpms < 500]
        bpms = bpms[bpms < 500]

        plt.plot(bpms, hist_all, 'k')
        plt.xlabel('Beats per minute')
        plt.ylabel('Freq Count')
        plt.show(block=True)

    return BPM, Ratio

# gameDisplay = pygame.display.set_mode((1,1))
# clock = pygame.time.Clock()
# end = False
# while not end:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == ord('q'):
#                 end = True
#         print(event)
#     pygame.display.update()
#     clock.tick(30)

[fs, s] = input_audio_file('/home/sampeiomichi/mini-project-4-interactive-visualization-sampei-and-sara/pyAudioAnalysis/pyAudioAnalysis/data/beat/small.wav')
beatExtraction(fs,PLOT=True)
