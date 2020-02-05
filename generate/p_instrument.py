import pickle

class P_Instrument:

  def __init__(self, instrument_folder):
    self.program = 0
    self.pitches = list()
    self.velocities = list()
    self.lengths = list()
    self.offsets = list()

    self.set_instrument(instrument_folder)

  def set_instrument(self, instrument_folder):

    with open(instrument_folder + "/program", "rb") as fp:
      self.program = pickle.load(fp)
    with open(instrument_folder + "/pitches", "rb") as fp:
      self.pitches = pickle.load(fp)
    with open(instrument_folder + "/velocities", "rb") as fp:
      self.velocities = pickle.load(fp)
    with open(instrument_folder + "/lengths", "rb") as fp:
      self.lengths = pickle.load(fp)
    with open(instrument_folder + "/offsets", "rb") as fp:
      self.offsets = pickle.load(fp)