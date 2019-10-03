# Project 2: North Korean Takeover
by Benjamin Bowdon, Emily Matthew, Caleb Gardner, Evan Chung

# Section 1: Finding the elusive, top secret North Korean radio station

## Part A: Using QSpectrumAnalyzer
The first task of this project was to find the radio station on the spectrum. According to some top secret intel, the station frequency hopped every few minutes so we needed a good way to find the signal each time. QSpectrumAnalyzer was set up for frequency sweeping with 1 GHz bandwith. The first time we saw the signal was at 1.26 GHz. We quickly opened GQRX to play the radio station.

(Insert Picture of QSpec)

## Part B: Using GQRX
Once we found the signal with QSpectrum Analyzer, we looked at that frequency in GQRX. Using wideband frequency modulation, we played the radio station and heard the North Korean national anthem, played along with a display of Kim Jong Un's face. In the middle of the broadcast, morse code plays audibly.

(Insert GQRX Pic)

# Section 2: High-Tech Intricate Digital Signal Analysis using High-End Interpretation Software

## Part A: Decoding Complex Morse Code
We separated morse code from the rest of the signal and decoded it by tweaking a few settings in Audacity. We made the dots and dashes very visible and used an online decoder to decode the secret message as: "Did the plan work?".
## Part B: Analyzing Entire Electromagnetic Spectrum to Identify Hidden Signal Tags
We analyzed the whole signal in Audacity by plotting the spectrum as a Power vs. Frequency graph. We noticed the signal had an unnaturally low dip around 250 Hz and deduced it must be a purposeful attribute/flag of the station. We need to replicate this dip in the message that we replay.

(Insert Picture Here)
# Section 2: Taking over the protected, safeguarded radio station using elite h@x4r techniques

## Part A: Choosing a Filter
In order to make our .wav file fit in with the station, we needed to apply a filter to it. The filter we selected was the Band Reject filter (a filter that "rejects" samples in a certain frequency range or "band with"). 
## Part B: Choosing a Message
Minecraft xD
## Part C: Playing Modified Message
We used the GRC file to play the message

(Insert pic of GRC file)
