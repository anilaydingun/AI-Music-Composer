import os
import generate.g_instrument

class G_Data:

  def __init__(self, instrument_folder="../data/data", weight_folder="../train/weights"):
    self.instruments = dict()
    
    self.create_instruments(instrument_folder, weight_folder)




  def create_instruments(self, instrument_folder, weight_folder):

    for i in range(128):

      v_instrument_folder = instrument_folder + "/v_instrument" + str(i)
      is_instrument_trained = os.path.exists(weight_folder + "/" + str(i) + "/pitch")
      if is_instrument_trained and os.path.exists(v_instrument_folder) and os.path.isdir(v_instrument_folder) and os.path.exists(v_instrument_folder + "/instrument_program") and os.path.isfile(v_instrument_folder + "/instrument_program"):
        self.instruments[i] = generate.g_instrument.G_Instrument(v_instrument_folder, weight_folder)