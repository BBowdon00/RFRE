# Project 1: Saving Ukraine
By Benjamin Bowdon, Emily Mathew, Evan Chung, and Caleb Gardner
Using HRF09 and a tan tank

# Section 1: Hacking into the Tank’s Mainframe to Fry the Engine

## Part A: Recording the signal.

The signal was recorded using osmocom_fft

![osmocom_fft](https://github.com/ASRL/RFRE-F19-Foxtrot/blob/P1/RFRE%20Osmocom.png?raw=true)

## Part B: The signal was analyzed using Inspectrum

![inspectrum](https://github.com/ASRL/RFRE-F19-Foxtrot/blob/P1/RFRE%20Inspectrum.png?raw=true)
Amplitude Shift Keying
27.15 MHz
48.96 ms
At .55 (microseconds?) signal gets weird

## Part C: The signal was cleaned and deconstructed using URH (Universal Radio Hacker)
![URH_Replay](https://github.com/ASRL/RFRE-F19-Foxtrot/blob/P1/RFRE%20URH%20Replay.png?raw=true)
0xf54d54ccd33333353555550


## Part D: The signal was replayed using GnuRadio
![GNU_Replay](https://github.com/ASRL/RFRE-F19-Foxtrot/blob/P1/RFRE%20GNURadio%20Replay.png?raw=true)


# Section 2: Preventing Russian Military from Controlling Tank
## Part A: Active Targeted Jamming (as opposed to Passive White Noise Jamming)
For this project, we chose to do active targeted jamming instead of passive white noise jamming. This method has a much larger effective range than the white noise jamming. 

## Part B: Signal Selection using URH
![URH_Jamming](https://github.com/ASRL/RFRE-F19-Foxtrot/blob/P1/RFRE%20URH%20Jamming.png?raw=true)

## Part C: Signal Replay using GnuRadio
![GNU_Jamming](https://github.com/ASRL/RFRE-F19-Foxtrot/blob/P1/RFRE%20GNURadio%20Jamming.png?raw=true)



(Both jamming and signal replay were demoed to Nick)
