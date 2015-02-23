# Morse Code Library #

This is a simple Python-based Morse code library. It can be used
to convert text into dits and dahs as text and/or as sounds 
through the soundcard. 

## Requirements ##

* numpy
* pygame


### Example of converting text ###
```python

from morsecodelib import text
text.text_to_code('testing text to code converSION!')
```

This prints: 
`- . ... - .. -. --.  - . -..- -  - ---  -.-. --- -.. .  -.-. ... .. --- -. -.-.--`

### Example of playing sound ###

```python
from morsecodelib import sound
morse_sound = sound.MorseSoundPlayer()
morse_sound.text_to_sound('HI THERE THIS IS A TEST')
```

    