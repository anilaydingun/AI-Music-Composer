import dataset as ds
import serialize as sr

dataset = ds.Dataset(dataset="midi_songs")
for instrument in dataset.instruments:
  sr.Serialize(instrument=instrument, data_folder="data")