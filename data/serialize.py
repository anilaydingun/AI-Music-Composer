import os
import pickle

class Serialize:

  def __init__(self, instrument, data_folder="data"):
    self.instrument = instrument
    self.data_folder = data_folder
    self.instrument_folder = str()
    
    self.create_folders()
    self.create_files()



  def create_folders(self):
    
    folder_name = self.data_folder
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)
    elif not os.path.isdir(folder_name):
      os.mkdir(folder_name)

    
    folder_name = self.data_folder + "/v_instrument" + str(self.instrument.program)
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)
    elif not os.path.isdir(folder_name):
      os.mkdir(folder_name)

    self.instrument_folder = folder_name



  def create_files(self):

    folder_name = self.instrument_folder + "/"
    
    with open(folder_name + "instrument_program", "wb") as fp:
      pickle.dump(self.instrument.program, fp)
    with open(folder_name + "instrument_name", "wb") as fp:
      pickle.dump(self.instrument.name, fp)

    with open(folder_name + "pitches", "wb") as fp:
      pickle.dump(self.instrument.pitches, fp)
    with open(folder_name + "unique_pitches", "wb") as fp:
      pickle.dump(self.instrument.unique_pitches, fp)
    with open(folder_name + "dict_pitches_ints", "wb") as fp:
      pickle.dump(self.instrument.dict_pitches_ints, fp)
    with open(folder_name + "dict_ints_pitches", "wb") as fp:
      pickle.dump(self.instrument.dict_ints_pitches, fp)
    with open(folder_name + "len_unique_pitches", "wb") as fp:
      pickle.dump(self.instrument.len_unique_pitches, fp)
    with open(folder_name + "len_pitches", "wb") as fp:
      pickle.dump(self.instrument.len_pitches, fp)

    with open(folder_name + "velocities", "wb") as fp:
      pickle.dump(self.instrument.velocities, fp)
    with open(folder_name + "unique_velocities", "wb") as fp:
      pickle.dump(self.instrument.unique_velocities, fp)
    with open(folder_name + "dict_velocities_ints", "wb") as fp:
      pickle.dump(self.instrument.dict_velocities_ints, fp)
    with open(folder_name + "dict_ints_velocities", "wb") as fp:
      pickle.dump(self.instrument.dict_ints_velocities, fp)
    with open(folder_name + "len_unique_velocities", "wb") as fp:
      pickle.dump(self.instrument.len_unique_velocities, fp)
    with open(folder_name + "len_velocities", "wb") as fp:
      pickle.dump(self.instrument.len_velocities, fp)

    with open(folder_name + "lengths", "wb") as fp:
      pickle.dump(self.instrument.lengths, fp)
    with open(folder_name + "unique_lengths", "wb") as fp:
      pickle.dump(self.instrument.unique_lengths, fp)
    with open(folder_name + "dict_lengths_ints", "wb") as fp:
      pickle.dump(self.instrument.dict_lengths_ints, fp)
    with open(folder_name + "dict_ints_lengths", "wb") as fp:
      pickle.dump(self.instrument.dict_ints_lengths, fp)
    with open(folder_name + "len_unique_lengths", "wb") as fp:
      pickle.dump(self.instrument.len_unique_lengths, fp)
    with open(folder_name + "len_lengths", "wb") as fp:
      pickle.dump(self.instrument.len_lengths, fp)

    with open(folder_name + "offsets", "wb") as fp:
      pickle.dump(self.instrument.offsets, fp)
    with open(folder_name + "unique_offsets", "wb") as fp:
      pickle.dump(self.instrument.unique_offsets, fp)
    with open(folder_name + "dict_offsets_ints", "wb") as fp:
      pickle.dump(self.instrument.dict_offsets_ints, fp)
    with open(folder_name + "dict_ints_offsets", "wb") as fp:
      pickle.dump(self.instrument.dict_ints_offsets, fp)
    with open(folder_name + "len_unique_offsets", "wb") as fp:
      pickle.dump(self.instrument.len_unique_offsets, fp)
    with open(folder_name + "len_offsets", "wb") as fp:
      pickle.dump(self.instrument.len_offsets, fp) 