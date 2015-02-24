"""
Make sounds from Morse code data
"""

import time
from array import array
import math 

import pygame
import numpy

from morsecodelib import config
from morsecodelib import text


class MorseSoundPlayer(object):
    """
    Takes text and renders it as sound on the sound card
    """
    def __init__(self):
        """
        Set up the mixer and tone. 
        
        Mixer buffer should be small to minimize latency. 
        """
        pygame.mixer.pre_init(config.SAMPLE_RATE, size = -16, channels = 1, buffer = 64)
        pygame.init()
        self.tone = ToneSound(frequency = config.FREQUENCY, volume = .5)

    def text_to_sound(self, message_text):
        """
        Play a text string as Morse code through speakers
        """
        message_morse = text.text_to_code(message_text)
        for word in message_morse.split('  '):
            self.play_word(word)

    def play_word(self, word):
        """
        Plays a Morse code word through the speakers
        This does all the official timing.
        """
        for letter in word.split(' '):
            for char in letter:
                if char == '.':
                    self.play_dit()
                elif char == '-':
                    self.play_dah()
                time.sleep(config.DIT_DURATION)
            time.sleep(config.DAH_DURATION)
        time.sleep(config.DIT_DURATION*7)
            
    def play_dit(self):
        """
        Play one dit
        """
        self._play_tone(config.DIT_DURATION)
    
    def play_dah(self):  
        """
        Play one dah
        """  
        self._play_tone(config.DAH_DURATION)
        
    def _play_tone(self, duration):
        self.tone.play(-1) # the -1 means to loop the sound
        time.sleep(duration)
        self.tone.stop()

class ToneSound(pygame.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self, shape = 'sine'):
        mixer_frequency, mixer_format, _channels = pygame.mixer.get_init()
        period = int(round(mixer_frequency / self.frequency))
        
        amplitude = 2 ** (abs(mixer_format) - 1) - 1
        if shape == 'sine':
            samples = self.sine_wave(amplitude, period)
        elif shape=='square':
            samples = self.square_wave(amplitude, period)
           
        return samples
    
    def _init_samples(self, period):
        return array("h", [0] * period)
    
    def sine_wave(self, amplitude, period):
        samples = self._init_samples(period)
        for time in xrange(period):
            samples[time] = int(amplitude * math.sin(2*math.pi*time/period))
        return samples
    
    def square_wave(self, amplitude, period):
        samples = self._init_samples(period)
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples
          


if __name__=='__main__':   
    morse_sound = MorseSoundPlayer()
    #morse_sound.text_to_sound('HI THERE THIS IS A TEST')
    morse_sound.text_to_sound('HELLO THERE THIS IS NICK')