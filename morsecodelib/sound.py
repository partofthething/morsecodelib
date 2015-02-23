"""
Make sounds from Morse code data
"""

import time

import pygame
import numpy

from morsecodelib import config
from morsecodelib import text


class MorseSoundPlayer(object):
    """
    Takes text and renders it as sound on the sound card
    """
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, buffer=4096)
        pygame.init()
        self.tone = generate_tone()

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

def generate_tone(shape='sine', freq=440.0, vol=1.0):
    """
    create a pygame.mixer.Sound object of a sine wave
    
    Based on: http://www.pygame.org/project-pitch+perfect-1689-2947.html
    
    Parameters
    ----------
    freq : float
        frequency in Hz
    vol : float
        relative volume of returned sound; will be clipped into
        range 0.0 to 1.0
    """

    # Get playback values that mixer was initialized with.
    (pb_freq, pb_bits, pb_chns) = pygame.mixer.get_init()

    # Clip range of volume.
    vol = numpy.clip(vol, 0.0, 1.0)

    # multiplier and length pan out the size of the sample to help
    # keep the mixer busy between calls to channel.queue()
    multiplier = int(freq / 24.0)
    length = max(1, int(float(pb_freq) / freq * multiplier))
    
    # Create a one-dimensional array with linear values.
    lin = numpy.linspace(0.0, multiplier, num=length, endpoint=False)
    ary = numpy.sin(lin * 2.0 * numpy.pi)

    # If mixer is in stereo mode, double up the array information for
    # each channel.
    if pb_chns == 2:
        ary = numpy.repeat(ary[..., numpy.newaxis], 2, axis=1)

    if pb_bits == 8:
        # Adjust for volume and 8-bit range.
        snd_ary = ary * vol * 127.0
        return pygame.sndarray.make_sound(snd_ary.astype(numpy.uint8) + 128)
    elif pb_bits == -16:
        # Adjust for 16-bit range.
        snd_ary = ary * vol * float((1 << 15) - 1)
        return pygame.sndarray.make_sound(snd_ary.astype(numpy.int16))
    else:
        raise RuntimeError("pygame.mixer playback bit-size unsupported."
                            "Should be either 8 or -16.")

if __name__=='__main__':   
    morse_sound = MorseSoundPlayer()
    #morse_sound.text_to_sound('HI THERE THIS IS A TEST')
    morse_sound.text_to_sound('MMK MKM MMMKK')