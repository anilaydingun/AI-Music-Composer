import pickle
import os
import random
import shutil
import pretty_midi
import glob
import numpy as np

import generate.g_data
import generate.p_instrument
import generate.g_instrument


class Instrument_Settings:
    def __init__(self, program=0, note_count=100, velocity=False, length=False, offset=False, default_velocity=40, default_length=0.5, default_offset=0):
      self.program = program
      self.note_count = note_count
      self.velocity = velocity
      self.length = length
      self.offset = offset
      self.song_type = None

      self.default_velocity = default_velocity
      self.default_length = default_length
      self.default_offset = default_offset

      self.set_song_type()

    def set_song_type(self):
        self.song_type = str(self.program)

        if self.velocity:
          self.song_type = self.song_type + "T"
        else:
          self.song_type = self.song_type + "F"
        if self.length:
          self.song_type = self.song_type + "T"
        else:
          self.song_type = self.song_type + "F"
        if self.offset:
          self.song_type = self.song_type + "T"
        else: 
          self.song_type = self.song_type + "F"


class Generate:
  def __init__(self, song_folder="../generate/songs"):
    self.g_data = generate.g_data.G_Data(instrument_folder="../data/data", weight_folder="../train/weights")
    self.song_folder = song_folder

    if not os.path.exists(song_folder):
      os.mkdir(song_folder)



  def generate_p_song(self, argv):

    specific_song_folder = self.song_folder + "/"
    for i in range(128):
      for setting in argv:
        if setting.program == i:
          specific_song_folder = specific_song_folder + setting.song_type

    if not os.path.exists(specific_song_folder):
      os.mkdir(specific_song_folder)


    p_song_folder = self.get_song_name(specific_song_folder)


    for setting in argv:

      g_instrument = self.g_data.instruments[setting.program]

      p_instrument_folder = p_song_folder + "/p_instrument" + str(g_instrument.program)
      os.mkdir(p_instrument_folder)

      predicted_pitches = self.predict(g_instrument.model_pitch, g_instrument.pitch_input, g_instrument.dict_ints_pitches, g_instrument.len_unique_pitches, setting.note_count)
      predicted_velocities = list()
      predicted_lengths = list()
      predicted_offsets = list()



      if setting.velocity and g_instrument.model_velocity != None:
        predicted_velocities = self.predict(g_instrument.model_velocity, g_instrument.velocity_input, g_instrument.dict_ints_velocities, g_instrument.len_unique_velocities, setting.note_count)
      else:
        predicted_velocities = [setting.default_velocity] * setting.note_count

      if setting.length and g_instrument.model_length != None:
        predicted_lengths = self.predict(g_instrument.model_length, g_instrument.length_input, g_instrument.dict_ints_lengths, g_instrument.len_unique_lengths, setting.note_count)
      else:
        predicted_lengths = [setting.default_length] * setting.note_count

      if setting.offset and g_instrument.model_offset != None:
        predicted_offsets = self.predict(g_instrument.model_offset, g_instrument.offset_input, g_instrument.dict_ints_offsets, g_instrument.len_unique_offsets, setting.note_count)
      else:
        predicted_offsets = [setting.default_offset] * setting.note_count


      with open(p_instrument_folder + "/program", "wb") as fp:
        pickle.dump(g_instrument.program, fp)
      with open(p_instrument_folder + "/pitches", "wb") as fp:
        pickle.dump(predicted_pitches, fp)
      with open(p_instrument_folder + "/velocities", "wb") as fp:
        pickle.dump(predicted_velocities, fp)
      with open(p_instrument_folder + "/lengths", "wb") as fp:
        pickle.dump(predicted_lengths, fp)
      with open(p_instrument_folder + "/offsets", "wb") as fp:
        pickle.dump(predicted_offsets, fp)

      

  def get_song_name(self, song_folder):

    songs = glob.glob(song_folder + "/*")
    for i in range(len(songs)):
      if not os.path.exists(song_folder + "/" + str(i) + "_song"):
        os.mkdir(song_folder + "/" + str(i) + "_song")
        return song_folder + "/" + str(i) + "_song"

    os.mkdir(song_folder + "/" + str(len(songs)) + "_song")
    return song_folder + "/" + str(len(songs)) + "_song"



  def generate(self, argv):
    specific_song_folder = self.song_folder + "/"
    for i in range(128):
      for setting in argv:
        if setting.program == i:
          specific_song_folder = specific_song_folder + setting.song_type

    songs = glob.glob(specific_song_folder + "/*")
    song_count = len(songs)
    if song_count < 1:
      self.generate_p_song(argv)
      songs = glob.glob(specific_song_folder + "/*")
      song_count = len(songs)

    song_folder = songs[random.randint(0, (song_count - 1))]
    
    p_instruments = list()
    for instrument_folder in glob.glob(song_folder + "/*"):
      p_instruments.append(generate.p_instrument.P_Instrument(instrument_folder))

    new_midi_song = self.create_midi(p_instruments)
    self.remove_song(song_folder)
    return new_midi_song



  def remove_song(self, song_folder):
    shutil.rmtree(song_folder)


  def create_midi(self, p_instruments):
    if not os.path.exists(self.song_folder + "/temp"):
      os.mkdir(self.song_folder + "/temp")

    new_midi = pretty_midi.PrettyMIDI()
    for instrument in p_instruments:
      
      new_midi_instrument = pretty_midi.Instrument(program=instrument.program)
      start = 0.2
      for i in range(len(instrument.pitches)):
        for pitch in instrument.pitches[i].split("-"):
          note = pretty_midi.Note(velocity=int(instrument.velocities[i]), pitch=int(pitch), start=start, end=start + float(instrument.lengths[i]))
          new_midi_instrument.notes.append(note)
        start = start + float(instrument.lengths[i]) + float(instrument.offsets[i])


      new_midi.instruments.append(new_midi_instrument)
    
    temp_name =  self.song_folder + "/temp/" + str(random.randint(0,1000000000)) + ".mid"
    while os.path.exists(temp_name):
      temp_name =  self.song_folder + "/temp/" + str(random.randint(0,1000000000)) + ".mid"

    new_midi.write(temp_name)
    return temp_name







  @staticmethod
  def predict(model, input, int_to_unique, len_unique, note_count):

    start_index = np.random.randint(0, len(input)-1)
    initial_input = input[start_index]
    predicted = list()

    for i in range(note_count):
      prediction_input = np.reshape(initial_input, (1, len(initial_input), 1))
      prediction_input = prediction_input / float(len_unique)




      # library correction
      import keras.backend.tensorflow_backend as tb
      tb._SYMBOLIC_SCOPE.value = True


      prediction = model.predict(prediction_input, verbose=0)

      index = np.argmax(prediction)
      predicted.append(int_to_unique[index])

      initial_input.append(index)
      initial_input = initial_input[1:len(initial_input)]

    return predicted


os.chdir("generate")
generate1 = Generate("../static/songs")