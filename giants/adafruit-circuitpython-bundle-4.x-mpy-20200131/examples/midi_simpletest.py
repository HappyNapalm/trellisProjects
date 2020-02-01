# simple_test
import time
import random
import usb_midi
import adafruit_midi
from adafruit_midi.control_change   import ControlChange
from adafruit_midi.note_off         import NoteOff
from adafruit_midi.note_on          import NoteOn
from adafruit_midi.pitch_bend       import PitchBend

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

print("Midi test")

# Convert channel numbers at the presentation layer to the ones musicians use
print("Default output channel:", midi.out_channel + 1)
print("Listening on input channel:",
      midi.in_channel + 1 if midi.in_channel is not None else None)

while True:
    midi.send(NoteOn(44, 120))  # G sharp 2nd octave
    time.sleep(0.25)
    a_pitch_bend = PitchBend(random.randint(0, 16383))
    midi.send(a_pitch_bend)
    time.sleep(0.25)
    # note how a list of messages can be used
    midi.send([NoteOff("G#2", 120),
               ControlChange(3, 44)])
    time.sleep(0.5)
