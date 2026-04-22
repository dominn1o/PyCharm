import numpy as np
import wave


def text_to_waveform(text, duration=0.3, sample_rate=44100):
    waveforms = []
    for char in text:
        freq = 200 + (ord(char) * 3)  # map character to frequency
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        tone = np.sin(freq * t * 2 * np.pi)
        waveforms.append(tone)
    return np.concatenate(waveforms)


def save_waveform_to_wav(filename, waveform, sample_rate=44100):
    # Normalize to 16-bit PCM
    audio = (waveform * 32767).astype(np.int16)

    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)  # mono
        wav_file.setsampwidth(2)  # 2 bytes per sample
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio.tobytes())


# Example usage
name = "digital_girlfriend_2002"
waveform = text_to_waveform(name)
save_waveform_to_wav("digigf.wav", waveform)

print("Saved as alex.wav")
