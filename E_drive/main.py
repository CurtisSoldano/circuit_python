#import the needed libraries

import time
import random
import audioio
import digitalio
import board
import neopixel

#initialize Circuit Playground on board Neopixels,number of LED's, brightness

CPX_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.90)

# Audio invocation required for CircuitPlayground Express
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)
a = audioio.AudioOut(board.A0)
#assign audio samples and assign to an object
data = open("thunder1.wav", "rb")
wav1 = audioio.WaveFile(data)
data1 = open("thunder2.wav", "rb")
wav2 = audioio.WaveFile(data1)
data2 = open("thunder3.wav", "rb")
wav3 = audioio.WaveFile(data2)
data3 = open("thunder4.wav", "rb")
wav4 = audioio.WaveFile(data3)
data4 = open("thunder5.wav", "rb")
wav5 = audioio.WaveFile(data4)
data5 = open("thunder7.wav", "rb")
wav6 = audioio.WaveFile(data5)

#lighting function with random delay timer
def lightning():

#set up random numbers
    time_delay = random.randint(1,6)
    time.sleep(time_delay)
    soundnumber = random.randint(1,6)
    lightsequence = random.randint(1,3)

    if lightsequence == 1:
        CPX_pixels.fill((255, 255, 255))
        time.sleep(random.randrange(1))
        CPX_pixels.fill((0, 0, 0))

    elif lightsequence == 2:
        CPX_pixels.fill((50, 50, 50))
        time.sleep(random.randrange(1))
        CPX_pixels.fill((0, 0, 0))
        CPX_pixels.fill((250,250,250))
        time.sleep(random.randrange(1))
        CPX_pixels.fill((0, 0, 0))
    elif lightsequence == 3:
        CPX_pixels.fill((250, 250, 250))
        time.sleep(random.randrange(1))
        CPX_pixels.fill((0, 0, 0))
        CPX_pixels.fill((50, 50, 50))
        time.sleep(random.randrange(1))
        CPX_pixels.fill((0, 0, 0))
        CPX_pixels.fill((250, 250, 250))
        time.sleep(random.randrange(1))
        CPX_pixels.fill((0, 0, 0))


#play random sound

    if soundnumber == 1:
        a.play(wav1)
    elif soundnumber == 2:
        a.play(wav2)
    elif soundnumber == 3:
        a.play(wav3)
    elif soundnumber == 4:
        a.play(wav4)
    elif soundnumber == 5:
        a.play(wav5)
    elif soundnumber == 6:
        a.play(wav6)
    while a.playing:
      pass


# main program loop
while True:
    lightning()

