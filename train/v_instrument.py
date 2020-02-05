import pickle

class V_Instrument:

  def __init__(self, folder):
    self.program = 0
    self.name = str()

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

    self.set_instrument(folder)

  def set_instrument(self,folder):

    folder_name = folder + "/"

    with open(folder_name + "instrument_program", "rb") as fp:
      self.program = pickle.load(fp)
    with open(folder_name + "instrument_name", "rb") as fp:
      self.name = pickle.load(fp)

    with open(folder_name + "pitches", "rb") as fp:
      self.pitches = pickle.load(fp)
    with open(folder_name + "unique_pitches", "rb") as fp:
      self.unique_pitches = pickle.load(fp)
    with open(folder_name + "dict_pitches_ints", "rb") as fp:
      self.dict_pitches_ints = pickle.load(fp)
    with open(folder_name + "dict_ints_pitches", "rb") as fp:
      self.dict_ints_pitches = pickle.load(fp)
    with open(folder_name + "len_unique_pitches", "rb") as fp:
      self.len_unique_pitches = pickle.load(fp)
    with open(folder_name + "len_pitches", "rb") as fp:
      self.len_pitches = pickle.load(fp)

    with open(folder_name + "velocities", "rb") as fp:
      self.velocities = pickle.load(fp)
    with open(folder_name + "unique_velocities", "rb") as fp:
      self.unique_velocities = pickle.load(fp)
    with open(folder_name + "dict_velocities_ints", "rb") as fp:
      self.dict_velocities_ints = pickle.load(fp)
    with open(folder_name + "dict_ints_velocities", "rb") as fp:
      self.dict_ints_velocities = pickle.load(fp)
    with open(folder_name + "len_unique_velocities", "rb") as fp:
      self.len_unique_velocities = pickle.load(fp)
    with open(folder_name + "len_velocities", "rb") as fp:
      self.len_velocities = pickle.load(fp)

    with open(folder_name + "lengths", "rb") as fp:
      self.lengths = pickle.load(fp)
    with open(folder_name + "unique_lengths", "rb") as fp:
      self.unique_lengths = pickle.load(fp)
    with open(folder_name + "dict_lengths_ints", "rb") as fp:
      self.dict_lengths_ints = pickle.load(fp)
    with open(folder_name + "dict_ints_lengths", "rb") as fp:
      self.dict_ints_lengths = pickle.load(fp)
    with open(folder_name + "len_unique_lengths", "rb") as fp:
      self.len_unique_lengths = pickle.load(fp)
    with open(folder_name + "len_lengths", "rb") as fp:
      self.len_lengths = pickle.load(fp)

    with open(folder_name + "offsets", "rb") as fp:
      self.offsets = pickle.load(fp)
    with open(folder_name + "unique_offsets", "rb") as fp:
      self.unique_offsets = pickle.load(fp)
    with open(folder_name + "dict_offsets_ints", "rb") as fp:
      self.dict_offsets_ints = pickle.load(fp)
    with open(folder_name + "dict_ints_offsets", "rb") as fp:
      self.dict_ints_offsets = pickle.load(fp)
    with open(folder_name + "len_unique_offsets", "rb") as fp:
      self.len_unique_offsets = pickle.load(fp)
    with open(folder_name + "len_offsets", "rb") as fp:
      self.len_offsets = pickle.load(fp)