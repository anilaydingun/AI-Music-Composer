import pretty_midi as pm
import glob




class Instrument:

  class Chord:
    def __init__(self, notes, pitches, velocity, length, offset):
      self.notes = notes
      self.pitches = pitches
      self.velocity = velocity
      self.length = length
      self.offset = offset



  def __init__(self, dataset="midi_songs", program=0):
    self.dataset = dataset
    self.name = pm.program_to_instrument_name(program)
    self.program = program
      
    self.notes = list()
    self.notes_count = 0
    self.chords = list()
    self.chords_count = 0

    self.pitches = list()
    self.unique_pitches = list()
    self.dict_pitches_ints = dict()
    self.dict_ints_pitches = dict()
    self.len_unique_pitches = 0
    self.len_pitches = 0

    self.velocities = list()
    self.unique_velocities = list()
    self.dict_velocities_ints = dict()
    self.dict_ints_velocities = dict()
    self.len_unique_velocities = 0
    self.len_velocities = 0

    self.lengths = list()
    self.unique_lengths = list()
    self.dict_lengths_ints = dict()
    self.dict_ints_lengths = dict()
    self.len_unique_lengths = 0
    self.len_lengths = 0

    self.offsets = list()
    self.unique_offsets = list()
    self.dict_offsets_ints = dict()
    self.dict_ints_offsets = dict()
    self.len_unique_offsets = 0
    self.len_offsets = 0

    self.read_dataset()
    self.set_chords()
    self.set_midi()
  



  def read_dataset(self):
    midi_count = len(glob.glob(self.dataset + "/*.mid"))
    for file_name in range(midi_count):
      midi_data = pm.PrettyMIDI(self.dataset + "/" + str(file_name) + ".mid")
      midi_data.remove_invalid_notes()
      
      wait = 0.0
      if len(self.notes) > 0:
        wait = self.notes[len(self.notes) - 1].end + 2.0

      for instrument in midi_data.instruments:
        if instrument.program == self.program:
          for note in instrument.notes:
            note.start += wait
            note.end += wait
            self.notes.append(note)

    self.notes_count = len(self.notes)



  def set_chords(self):
    notes_of_chord = list()
    index = 0

    while index < self.notes_count:
      if len(notes_of_chord) == 0:
        notes_of_chord.append(self.notes[index])
      elif notes_of_chord[0].start == self.notes[index].start and notes_of_chord[0].end == self.notes[index].end and notes_of_chord[0].velocity == self.notes[index].velocity:
        notes_of_chord.append(self.notes[index])
      else:
        while not self.is_chord(notes_of_chord):
          notes_of_chord.pop()
          index = index - 1

        ## Set chords octaves to a value to reduce unique pitch count ##
        if len(notes_of_chord) > 1:
          for note in notes_of_chord:
            note.pitch = self.set_octave_to(note.pitch)

        notes_of_chord = self.search_chord(notes_of_chord)

        pitches = list(note.pitch for note in notes_of_chord)
        velocity = notes_of_chord[0].velocity
        length = self.floor_the_value(notes_of_chord[0].end - notes_of_chord[0].start)
        offset = self.floor_the_value(self.notes[index].start - notes_of_chord[0].end)

        self.chords.append(self.Chord(list(note for note in notes_of_chord), pitches, velocity, length, offset))

        notes_of_chord = list()
        index = index - 1

      ## To add last chord ## 
      if index + 1 == len(self.notes):
        is_not_last = False
        while not self.is_chord(notes_of_chord):
          is_not_last = True
          notes_of_chord.pop()
          index = index - 1

        ## Set chords octaves to a value to reduce unique pitch count ##
        if len(notes_of_chord) > 1:
          for note in notes_of_chord:
            note.pitch = self.set_octave_to(note.pitch)

        notes_of_chord = self.search_chord(notes_of_chord)

        pitches = list(note.pitch for note in notes_of_chord)
        velocity = notes_of_chord[0].velocity
        length = self.floor_the_value(notes_of_chord[0].end - notes_of_chord[0].start)
        offset = 0.0

        self.chords.append(self.Chord(list(note for note in notes_of_chord), pitches, velocity, length, offset))

        if is_not_last:
          notes_of_chord = list()
          index = index - 1
       ## To add last chord ## 

      index = index + 1

    self.chords_count = len(self.chords)



  def floor_the_value(self, value_of_note):
    first_part = str(value_of_note).split('.')[0]
    second_part = (str(value_of_note).split('.')[1] + "0")[0:1]
    value_of_note = first_part + "." + second_part
    if value_of_note == "-0.0":
      return 0.0
    return float(value_of_note)



  def is_chord(self, note_list):
    if len(note_list) == 1:
      return True

    if self.is_same_note_in_chord(note_list):
      return False

    return True



  def is_same_note_in_chord(self, note_list):
    pitches = list(self.set_octave_to(note.pitch) for note in note_list)
    if len(pitches) != len(sorted(set(pitches))):
      return True
    else:
      return False

  

  def search_chord(self, new_note_list):
    for chord in self.chords:
      note_list = chord.notes
      if self.is_chord_equal(note_list, new_note_list):
        return list(pm.Note(velocity=new_note_list[0].velocity, pitch=note.pitch, start=new_note_list[0].start, end=new_note_list[0].end) for note in note_list)
        

    return list(note for note in new_note_list)




  def is_chord_equal(self, note_list_1, note_list_2):
    if(len(note_list_1) != len(note_list_2)):
      return False
    
    for note1 in note_list_1:
      control = False

      for note2 in note_list_2:
        if note1.pitch == note2.pitch:
          control = True

      if not control:
        return False

    return True





  def set_octave_to(self, pitch, octave=4):
    old_pitch = pm.note_number_to_name(pitch)
    new_pitch = pm.note_name_to_number(old_pitch[:len(old_pitch) - 1] + str(octave))
    return new_pitch



  def set_midi(self):

    for chord in self.chords:
      
      pitch = "-".join(str(pitch) for pitch in chord.pitches)
      velocity = str(chord.velocity)
      length = str(chord.length)
      offset = str(chord.offset)

      self.pitches.append(pitch)
      self.velocities.append(velocity)
      self.lengths.append(length)
      self.offsets.append(offset)

    ## Set unique lists ##
    self.unique_pitches = sorted(set(self.pitches))
    self.unique_velocities = sorted(set(self.velocities))
    self.unique_lengths = sorted(set(self.lengths))
    self.unique_offsets = sorted(set(self.offsets))

    ## Set feature to int dictionaries ##
    self.dict_pitches_ints = dict((pitch, number) for number, pitch in enumerate(self.unique_pitches))
    self.dict_velocities_ints = dict((velocity, number) for number, velocity in enumerate(self.unique_velocities))
    self.dict_lengths_ints = dict((length, number) for number, length in enumerate(self.unique_lengths))
    self.dict_offsets_ints = dict((offset, number) for number, offset in enumerate(self.unique_offsets))

    ## Set int to feature dictionaries ##
    self.dict_ints_pitches = dict((value, key) for key, value in self.dict_pitches_ints.items())
    self.dict_ints_velocities = dict((value, key) for key, value in self.dict_velocities_ints.items())
    self.dict_ints_lengths = dict((value, key) for key, value in self.dict_lengths_ints.items())
    self.dict_ints_offsets = dict((value, key) for key, value in self.dict_offsets_ints.items())
    
    ## Set length of lists ##
    self.len_unique_pitches = len(self.unique_pitches)
    self.len_unique_velocities = len(self.unique_velocities)
    self.len_unique_lengths = len(self.unique_lengths)
    self.len_unique_offsets = len(self.unique_offsets)
    self.len_pitches = len(self.pitches)
    self.len_velocities = len(self.velocities)
    self.len_lengths = len(self.lengths)
    self.len_offsets = len(self.offsets)