import numpy as np
import os
import glob
import pickle
import sys

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation
from keras.layers import BatchNormalization as BatchNorm
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint

import v_dataset


class Train:

  def __init__(self, instrument, feature, sequence_length=100, epoch=200, batch_size=128, load_effective=False):
    self.instrument = instrument
    self.feature = feature
    self.sequence_length = sequence_length
    self.epoch = epoch
    self.batch_size = batch_size

    self.features = list()
    self.unique_features = list()
    self.dict_features_ints = dict()
    self.dict_ints_features = dict()
    self.len_features = 0
    self.len_unique_features = 0

    self.input_sequence = None
    self.output_sequence = None
    self.model = None

    self.pretrain()
    self.io_sequence()
    self.create_folders()
    self.create_model(load_effective)
    self.train()




  def pretrain(self):
    if(self.feature == "pitch"):
      self.features = self.instrument.pitches
      self.unique_features = self.instrument.unique_pitches
      self.dict_features_ints = self.instrument.dict_pitches_ints
      self.dict_ints_features = self.instrument.dict_ints_pitches
      self.len_features = self.instrument.len_pitches
      self.len_unique_features = self.instrument.len_unique_pitches
    elif(self.feature == "velocity"):
      self.features = self.instrument.velocities
      self.unique_features = self.instrument.unique_velocities
      self.dict_features_ints = self.instrument.dict_velocities_ints
      self.dict_ints_features = self.instrument.dict_ints_velocities
      self.len_features = self.instrument.len_velocities
      self.len_unique_features = self.instrument.len_unique_velocities
    elif(self.feature == "length"):
      self.features = self.instrument.lengths
      self.unique_features = self.instrument.unique_lengths
      self.dict_features_ints = self.instrument.dict_lengths_ints
      self.dict_ints_features = self.instrument.dict_ints_lengths
      self.len_features = self.instrument.len_lengths
      self.len_unique_features = self.instrument.len_unique_lengths
    elif(self.feature == "offset"):
      self.features = self.instrument.offsets
      self.unique_features = self.instrument.unique_offsets
      self.dict_features_ints = self.instrument.dict_offsets_ints
      self.dict_ints_features = self.instrument.dict_ints_offsets
      self.len_features = self.instrument.len_offsets
      self.len_unique_features = self.instrument.len_unique_offsets
    

  def io_sequence(self):
    input_sequence = list()
    output_sequence = list()

    ## Create input sequences and the corresponding outputs ##
    for i in range(0, len(self.features) - self.sequence_length):
      ins = self.features[i:i + self.sequence_length]
      out = self.features[i + self.sequence_length]
      
      input_sequence.append(list(self.dict_features_ints[feature] for feature in ins))
      output_sequence.append(self.dict_features_ints[out])

    input_sequence = np.reshape(input_sequence, (len(input_sequence), self.sequence_length, 1))

    ## Normalize the input vector. ##
    ## One-hot vectors of output vectors. ##
    self.input_sequence = input_sequence / float(self.len_unique_features)   
    self.output_sequence = np_utils.to_categorical(output_sequence)



  def create_folders(self):
    folder_name = "weights"
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)
    elif not os.path.isdir(folder_name):
      os.mkdir(folder_name)

    folder_name = folder_name + "/" + str(self.instrument.program)
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)
    elif not os.path.isdir(folder_name):
      os.mkdir(folder_name)

    folder_name = folder_name + "/" + self.feature
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)
    elif not os.path.isdir(folder_name):
      os.mkdir(folder_name)



  def create_model(self, load_effective):
    model = Sequential()
    model.add(LSTM(512, input_shape=(self.input_sequence.shape[1], self.input_sequence.shape[2]), recurrent_dropout=0.3, return_sequences=True))
    model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))
    model.add(LSTM(512))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(self.len_unique_features)) 
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    weights = glob.glob("weights/" + str(self.instrument.program) + "/" + str(self.feature) + "/*")
    if load_effective and len(weights) > 0 and os.path.exists(weights[len(weights) - 1]):
      model.load_weights(weights[0])

    self.model = model


  def train(self):
    filepath = "weights/" + str(self.instrument.program) + "/"  + self.feature + "/weights-{loss:.4f}-{epoch:02d}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=0, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    self.model.fit(self.input_sequence, self.output_sequence, epochs=self.epoch, batch_size=self.batch_size, callbacks=callbacks_list)


def pretrain(arg_instrument, arg_feature, load_effective=False, sequence_length=100, batch_size=128, v_instrument_folder="../data/data"):
  virtual_dataset = v_dataset.V_Dataset()
  feature_list = list()
  feature_list.append("pitch")
  feature_list.append("velocity")
  feature_list.append("length")
  feature_list.append("offset")

  for instrument in virtual_dataset.instruments:
    if instrument.program == int(arg_instrument):
      for feature in feature_list:
        if feature == str(arg_feature):
          if os.path.exists(v_instrument_folder + "/v_instrument" + str(instrument.program) + "/" + str(feature)  + "_sequence_length"):
            with open(v_instrument_folder + "/v_instrument" + str(instrument.program) + "/" + str(feature)  + "_sequence_length", "rb") as fp:
              sequence_length = pickle.load(fp)
          else:
            with open(v_instrument_folder + "/v_instrument" + str(instrument.program) + "/" + str(feature)  + "_sequence_length", "wb") as fp:
              pickle.dump(sequence_length, fp)
          Train(instrument=instrument, feature=feature, load_effective=load_effective, sequence_length=sequence_length, batch_size=batch_size)



if __name__ == "__main__":
  pretrain(sys.argv[1], sys.argv[2], sequence_length=int(sys.argv[4]))
