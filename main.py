'''
This programme is a realtime DTMF Generator coded in Python. 
DTMF Dual-Tone Multi-Frequency, an auditory encoding system
for digits on a key pad. 

The DTMF system encodes an alphabet of 16 characters: 

Numbers: {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
Letters: {A, B, C, D}
Special: {#, *}

These are arranged in grid form:

+-----+------+------+------+------+
|     | 1209 | 1336 | 1447 | 1663 |
+-----+------+------+------+------+
| 697 |   1  |   2  |   3  |   A  |
+-----+------+------+------+------+
| 770 |   4  |   5  |   6  |   B  |
+-----+------+------+------+------+
| 852 |   7  |   8  |   9  |   C  |
+-----+------+------+------+------+
| 941 |   *  |   0  |   #  |   D  |
+-----+------+------+------+------+

The tone produced is simply an additive process of 2 sinusoids, at the frequencies dictated
by the grid position.

Harry Williams
University of Liverpool 
Computer Science MSc
May 2019 

'''

import numpy as np
import sounddevice as sd
import gui 

# Lookup Table

xFreqs = [1209.0, 1336.0, 1447.0, 1663.0]
yFreqs = [697.0, 770.0, 852.0, 941.0]

def playSynthSound(input1, input2,tone):
	
    # Sound Bits

	sps = 44100 # samples per second
	atten = 0.3 # attenuation amount
	duration_s = 0.25
	each_sample_number = np.arange(duration_s * sps) # array for each sample

	# Frequencies
	freq_hz = input1
	freq_hz_2 = input2

	# Calculate Waveform
	waveform  = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
	waveform2 = np.sin(2 * np.pi * each_sample_number * freq_hz_2 / sps)
    
    # Adder waveforms together & attenuate
	waveformComp = (waveform + waveform2) * atten

	# Update Visual Output
	freqText = gui.freqText
	freqText.clear()
	freqText.write("Freq I: {}Hz  Freq II: {}Hz".format(int(input1), int(input2)),  align = "center", font = ("Courier", 28, "normal"))

	selectedChar = gui.selectedChar
	selectedChar.clear()
	selectedChar.write("Tone: {}".format(tone),  align = "center", font = ("Courier", 28, "normal"))

    # Play the sound out the speakers
	sd.play(waveformComp, sps)




# Functions that determine sine input
def one():
	playSynthSound(697.0, 1209.0, 1)

def two():
	playSynthSound(697.0, 1336.0, 2)

def three():
	playSynthSound(697.0, 1447.0, 3)

def a():
	playSynthSound(697.0, 1633.0, 'A')

def four():
	playSynthSound(770.0, 1209.0, 4)

def five():
	playSynthSound(770.0, 1336.0, 5)

def six():
	playSynthSound(770.0, 1447.0, 6)

def b():
	playSynthSound(770.0, 1633.0, 'B')

def seven():
	playSynthSound(852.0, 1209.0, 7)

def eight():
	playSynthSound(852.0, 1336.0, 8)

def nine():
	playSynthSound(852.0, 1447.0, 9)

def c():
	playSynthSound(852.0, 1633.0, 'C')
	
def asterix():
	playSynthSound(941.0, 1209.0, '*')
	
def zero():
	playSynthSound(941.0, 1336.0, 0)

def hashtag():
	playSynthSound(941.0, 1447.0, '#')

def d():
	playSynthSound(941.0, 1633.0, 'D')

# Event Listeners

window = gui.window 
window.listen()
window.onkeypress(one, "1")
window.onkeypress(two, "2")
window.onkeypress(three, "3")
window.onkeypress(a, "a")
window.onkeypress(four, "4")
window.onkeypress(five, "5")
window.onkeypress(six, "6")
window.onkeypress(b,"b")
window.onkeypress(seven, "7")
window.onkeypress(eight, "8")
window.onkeypress(nine, "9")
window.onkeypress(c,"c")
window.onkeypress(asterix,"*")
window.onkeypress(zero,"0")
window.onkeypress(hashtag,"#")
window.onkeypress(d,"d")

# Program loop
while True:
	window.update()

