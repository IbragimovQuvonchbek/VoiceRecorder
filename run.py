import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# Sampling frequency (samples per second)
freq = 44100

# Recording duration (seconds)
duration = 5

# Specify the input device index for the microphone
device_index = 14  # Change this to the index of your preferred input device


def record_audio(filename, duration, freq, device_index):
    '''
    Records audio from the specified microphone device and saves it to a WAV file.

    Args:
        filename (str): The name of the file to save the recording.
        duration (int): The duration of the recording in seconds.
        freq (int): The sampling frequency in Hz.
        device_index (int): The index of the audio input device.
    '''
    print("Recording...")

    # Start recording
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2, dtype='float32', device=device_index)

    # Wait until the recording is finished
    sd.wait()

    # Normalize the audio data to the range of 16-bit PCM
    recording_int16 = np.int16(recording * 32767)

    # Save the recording to a WAV file
    write(filename, freq, recording_int16)
    print(f"Recording saved to {filename}")


# Example usage
if __name__ == "__main__":
    record_audio("recording.wav", duration, freq, device_index)
