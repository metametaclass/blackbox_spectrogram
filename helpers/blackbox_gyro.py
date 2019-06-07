import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal,stats


def init_figure_settings():
    plt.rcParams["figure.figsize"] = [12, 5]
    plt.rcParams['font.size'] = 14
    plt.rcParams['image.cmap'] = 'plasma'
    plt.rcParams['axes.linewidth'] = 2
    # Set the default colour cycle (in case someone changes it...)
    from cycler import cycler
    cols = plt.get_cmap('tab10').colors
    plt.rcParams['axes.prop_cycle'] = cycler(color=cols)




def show_axes_v2(data,start,stop,samplerate,names,caption,nfft):
    fig = plt.figure()

    i=1
    for name in names:

        axis = data[name][start:stop]
        plot = fig.add_subplot(len(names),2,i)
        i += 1
        plot.set_title(caption+' '+name)
        plot.plot(axis)

        #fig = plt.figure()
        plot = fig.add_subplot(len(names),2,i)
        powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(axis, Fs=samplerate, NFFT=nfft)
        plt.colorbar(imageAxis)    
        i += 1
    plt.tight_layout()

def show_axes(data,start,stop,samplerate,name,caption,nfft):
    fig = plt.figure()

    axis0 = data[name+'[0]'][start:stop]
    plot0 = fig.add_subplot(3,1,1)
    plot0.set_title(caption+"[0]")
    plot0.plot(axis0)
    
    axis1 = data[name+'[1]'][start:stop]
    plot1 = fig.add_subplot(3,1,2)
    plot1.set_title(caption+"[1]")
    plot1.plot(axis1)
    
    axis2 = data[name+'[2]'][start:stop]
    plot2 = fig.add_subplot(3,1,3)
    plot2.set_title(caption+"[2]")
    plot2.plot(axis2)
    
    fig = plt.figure()
    plt.title(caption+'[0]')
    powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(axis0, Fs=samplerate, NFFT=nfft, noverlap=nfft/2)
    plt.colorbar(imageAxis)    
    
    fig = plt.figure()
    plt.title(caption+'[1]')
    powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(axis1, Fs=samplerate, NFFT=nfft, noverlap=nfft/2)
    plt.colorbar(imageAxis)    
    
    fig = plt.figure()
    plt.title(caption+'[2]')
    powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(axis2, Fs=samplerate, NFFT=nfft, noverlap=nfft/2)
    plt.colorbar(imageAxis)    


def calc_max_noise_regression(data,start,stop,samplerate,axis1,axis2,nfft, start_regression=None, stop_regression=None):
    fig = plt.figure()

    gyro_axis1 = data[axis1][start:stop]

    plt11 = fig.add_subplot(2,2,1)
    plt11.set_title("axis 1 data")
    plt11.plot(gyro_axis1)

    plt12 = fig.add_subplot(2,2,2)
    plt12.set_title("axis 1 spectrogram")
    powerSpectrum1, freqenciesFound1, time1, imageAxis1 = plt12.specgram(gyro_axis1, Fs=samplerate, 
                                                                         NFFT=nfft, window=signal.windows.blackmanharris(nfft))
    plt.colorbar(imageAxis1)    

    gyro_axis2 = data[axis2][start:stop]

    plt21 = fig.add_subplot(2,2,3)
    plt21.set_title("axis 2 data")
    plt21.plot(gyro_axis2)

    plt22 = fig.add_subplot(2,2,4)
    plt22.set_title("axis 2 spectrogram")
    powerSpectrum2, freqenciesFound2, time2, imageAxis2 = plt22.specgram(gyro_axis2, Fs=samplerate, 
                                                                         NFFT=nfft, window=signal.windows.blackmanharris(nfft))
    plt.colorbar(imageAxis2)    
    plt.tight_layout()

    maxFreq1 = powerSpectrum1.argmax(0)
    maxFreq2 = powerSpectrum2.argmax(0)
    freqs1 = freqenciesFound1[maxFreq1]
    freqs2 = freqenciesFound2[maxFreq2]
    fig = plt.figure()
    plt1 = fig.add_subplot(2,1,1)
    plt1.plot(freqs1)
    plt2 = fig.add_subplot(2,1,2)
    plt2.plot(freqs2)
    plt.tight_layout()

    if start_regression is None:
        start_regression = 0

    if stop_regression is None:
        stop_regression = len(freqs1)

    r = stats.linregress(freqs1[start_regression:stop_regression],freqs2[start_regression:stop_regression])
    print(r)
