import mido
import wave
import contextlib


def get_drum_timestamps(midifile):
    mid = mido.MidiFile(f'assets/songs/mid/{midifile}.mid')
    durations = []
    absolute_time = 0

    for msg in mid:
        absolute_time += msg.time

        if msg.type == 'note_on' and msg.velocity > 40:
            if durations and durations[-1] != absolute_time or not durations:
                durations.append(absolute_time)

    durations.pop(0)

    return durations

def get_wav_duration(wavfile):
    with contextlib.closing(wave.open(wavfile, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate * f.getnchannels())
    return duration
