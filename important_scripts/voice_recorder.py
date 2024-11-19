# voice recorder in python using the sounddevice library
# pip install sounddevice
# pip install scipy

import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate

# Ask to enter the duration of the recording
seconds = int(input("Enter the duration of the recording in seconds: "))
print("Recording...\n")

# Corrected: Replace 'sounddevice' with 'sd' since you imported it as 'sd'
record_voice = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Use 'sd.wait()' instead of 'sounddevice.wait()'

# Save the recording as a WAV file
write('MyRecording.wav', fs, record_voice)

print("Recording is done. Please check the file 'MyRecording.wav' in the current directory.")
