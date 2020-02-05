import os
import glob
import v_instrument

class V_Dataset:

  def __init__(self, data_folder="../data/data"):
    self.instruments = list()

    self.set_dataset(data_folder)


  def set_dataset(self, data_folder):
    for instrument_folder in glob.glob(data_folder + "/*"):
      instrument_exists = True
      if not os.path.exists(instrument_folder + "/instrument_name") or not os.path.isfile(instrument_folder + "/instrument_name"):
        instrument_exists = False

      if instrument_exists:
        self.instruments.append(v_instrument.V_Instrument(instrument_folder))