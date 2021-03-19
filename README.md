# Morsey  

Python Algorithm to convert strings to Morse Code. Can generate a string representation and a wav file. 

The StringToSound function in main.py serves as the main entrypoint. It generates a np.array of type float containing the original sentence converted to Morse waveform.

## Usage  

The Morse.py file contains the following functions:   
- SentenceToMorse
- WordToMorse  
- CharacterToMorse  

These functions are pretty straightforward and only take a string as input. 

The SoundGenerator.py file contains the SoundGenerator class which is responsible for generating the individual audio samples, playing an array and saving it to disk.  
The SoundGenerator object allows the user to specify a sound frequency (the height of the sound generated), the time in milliseconds for a dot (or dit, which is one unit of time) and the sample rate.  

A SoundGenerator instance must be passed to the StringToSound function in main.py. There is a default SOUND_GENERATOR with parameters frequency 440, dot duration 50 and sample rate 4000 available and passed by default to StringToSound.  


## Examples  

Run example.py or listen to the generated wav files in the media folder.  


## Credits  

Timing information was taken from the morsecodeclass.net  
https://www.morsecodeclassnet.com/lesson3/#:~:text=Each%20dit%2C%20the%20short%20sound,the%20spacing%20within%20each%20character.  

morse-code.json file comes a gist by mohayonao  
https://gist.github.com/mohayonao/094c71af14fe4791c5dd  

