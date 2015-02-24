"""
Configuration options for morsecodelib

Will change to some config-file reader later, maybe. 
"""


SAMPLE_RATE = 22050
FREQUENCY = 600

WORDS_PER_MINUTE = 15
DIT_DURATION = 20 * 0.060 / WORDS_PER_MINUTE # PARIS @ 20WPM = 60ms/dit
DAH_DURATION = DIT_DURATION * 3.0