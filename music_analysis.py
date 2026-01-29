import mido


def get_drum_timestamps(midifile_path):
    mid = mido.MidiFile(f'assets/songs/mid/{midifile_path[0]}.mid')
    drum_timestamps = []

    DRUM_CHANNEL = [9, 10]

    accumulated_ticks = 0
    tempo = 500000
    ticks_per_beat = mid.ticks_per_beat

    for msg in mid:
        accumulated_ticks += msg.time

        if msg.type == 'set_tempo':
            tempo = msg.tempo

        if msg.time and msg.type == 'note_on' and msg.channel in DRUM_CHANNEL:
            seconds = mido.tick2second(accumulated_ticks, ticks_per_beat, tempo)
            drum_timestamps.append(seconds * midifile_path[1])

    print(drum_timestamps)

    return sorted(drum_timestamps)
