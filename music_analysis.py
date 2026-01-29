import mido

def get_drum_timestamps(midifile_path):
    mid = mido.MidiFile(midifile_path)
    drum_timestamps = []

    DRUM_CHANNEL = 9

    for msg in mid:
        if msg.type == 'note_on' and msg.channel == DRUM_CHANNEL:
            if msg.time:
                drum_timestamps.append(msg.time * 4)

    return drum_timestamps

print(sum(get_drum_timestamps('assets/songs/Never-Gonna-Give-You-Up-3.mid')))