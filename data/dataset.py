import pretty_midi as pm
import instrument as inst
import glob

class Dataset:

  def __init__(self, dataset="midi_songs"):
    self.dataset = dataset
    self.instruments_names = list()
    self.instruments_programs = list()
    self.instruments = list()

    self.set_dataset()

  def set_dataset(self):
    midi_count = len(glob.glob(self.dataset + "/*.mid"))
    for file_name in range(midi_count):
      midi_data = pm.PrettyMIDI(self.dataset + "/" + str(file_name) + ".mid")
      midi_data.remove_invalid_notes()

      for instrument in midi_data.instruments:
        self.instruments_programs.append(instrument.program)

    self.instruments_programs = sorted(set(self.instruments_programs))
    self.instruments_names = list(pm.program_to_instrument_name(program) for program in self.instruments_programs)

    for program in self.instruments_programs:
      self.instruments.append(inst.Instrument(dataset=self.dataset, program=program))