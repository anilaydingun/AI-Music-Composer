import os
import pickle
import numpy as np
import glob

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation
from keras.layers import BatchNormalization as BatchNorm
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint



class G_Instrument:

  def __init__(self, v_instrument_folder, weight_folder="../train/weights"):
    self.program = 0
    self.name = str()

    self.pitches = list()
    self.unique_pitches = list()
    self.dict_pitches_ints = dict()
    self.dict_ints_pitches = dict()
    self.len_unique_pitches = 0
    self.len_pitches = 0
    self.pitch_input = None
    self.n_pitch_input = None
    self.model_pitch = None
    self.pitch_sequence_length = None

    self.velocities = list()
    self.unique_velocities = list()
    self.dict_velocities_ints = dict()
    self.dict_ints_velocities = dict()
    self.len_unique_velocities = 0
    self.len_velocities = 0
    self.velocity_input = None
    self.n_velocity_input = None
    self.model_velocity = None
    self.velocity_sequence_length = None

    self.lengths = list()
    self.unique_lengths = list()
    self.dict_lengths_ints = dict()
    self.dict_ints_lengths = dict()
    self.len_unique_lengths = 0
    self.len_lengths = 0
    self.length_input = None
    self.n_length_input = None
    self.model_length = None
    self.length_sequence_length = None

    self.offsets = list()
    self.unique_offsets = list()
    self.dict_offsets_ints = dict()
    self.dict_ints_offsets = dict()
    self.len_unique_offsets = 0
    self.len_offsets = 0
    self.offset_input = None
    self.n_offset_input = None
    self.model_offset = None
    self.offset_sequence_length = None

    self.set_instrument(v_instrument_folder)
    self.set_model(weight_folder, v_instrument_folder)


  def set_instrument(self, folder):
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



  def set_model(self, folder, instrument_folder):

    weights = glob.glob(folder + "/" + str(self.program) + "/pitch/*.hdf5")
    if os.path.exists(folder + "/" + str(self.program) + "/pitch") and len(weights) > 0:
      with open(instrument_folder + "/pitch_sequence_length", "rb") as fp:
        self.pitch_sequence_length = pickle.load(fp)
      self.pitch_input, self.n_pitch_input = self.create_network_input(self.pitches, self.dict_pitches_ints, self.len_unique_pitches, sequence_length=self.pitch_sequence_length)
      weight_path = weights[0]
      self.model_pitch = self.create_network(self.n_pitch_input, self.len_unique_pitches, weight_path)

    weights = glob.glob(folder + "/" + str(self.program) + "/velocity/*.hdf5")
    if os.path.exists(folder + "/" + str(self.program) + "/velocity") and len(weights) > 0:
      with open(instrument_folder + "/velocity_sequence_length", "rb") as fp:
        self.velocity_sequence_length = pickle.load(fp)
      self.velocity_input, self.n_velocity_input = self.create_network_input(self.velocities, self.dict_velocities_ints, self.len_unique_velocities, sequence_length=self.velocity_sequence_length)
      weight_path = weights[0]
      self.model_velocity = self.create_network(self.n_velocity_input, self.len_unique_velocities, weight_path)

    weights = glob.glob(folder + "/" + str(self.program) + "/length/*.hdf5")
    if os.path.exists(folder + "/" + str(self.program) + "/length") and len(weights) > 0:
      with open(instrument_folder + "/length_sequence_length", "rb") as fp:
        self.length_sequence_length = pickle.load(fp)
      self.length_input, self.n_length_input = self.create_network_input(self.lengths, self.dict_lengths_ints, self.len_unique_lengths, sequence_length=self.length_sequence_length)
      weight_path = weights[0]
      self.model_length = self.create_network(self.n_length_input, self.len_unique_lengths, weight_path)


    weights = glob.glob(folder + "/" + str(self.program) + "/offset/*.hdf5")
    if os.path.exists(folder + "/" + str(self.program) + "/offset") and len(weights) > 0:
      with open(instrument_folder + "/offset_sequence_length", "rb") as fp:
        self.offset_sequence_length = pickle.load(fp)
      self.offset_input, self.n_offset_input = self.create_network_input(self.offsets, self.dict_offsets_ints, self.len_unique_offsets, sequence_length=self.offset_sequence_length)
      weight_path = weights[0]
      self.model_offset = self.create_network(self.n_offset_input, self.len_unique_offsets, weight_path)


  def create_network(self, network_input, n_vocab, weight_path):
    model = Sequential()
    model.add(LSTM(
      512,
      input_shape=(network_input.shape[1], network_input.shape[2]),
      recurrent_dropout=0.3,
      return_sequences=True
    ))
    model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3, ))
    model.add(LSTM(512))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(n_vocab))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')


    model.load_weights(weight_path)
    return model


  def create_network_input(self, features, dict_features_ints, len_unique_features, sequence_length=100):
    input_sequence = list()
    for i in range(0, len(features) - sequence_length):
      ins = features[i:i + sequence_length]
      input_sequence.append(list(dict_features_ints[feature] for feature in ins))

    n_input_sequence = np.reshape(input_sequence, (len(input_sequence), sequence_length, 1))
    n_input_sequence = n_input_sequence / float(len_unique_features)

    return input_sequence, n_input_sequence