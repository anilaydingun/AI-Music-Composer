# AI-Music-Composer
## What is an AI Music Composer ?  
It is a BBM419 Design Project we prepared by using various Machine Learning and NLP algorithms, and in the end artificial intelligence automatically produces music.
## Dataset
Dataset consists of final fantasy music and midi files based on the piano as an instrument. To visit the dataset https://github.com/Skuldur/Classical-Piano-Composer
## Requirements
- **Python 3.x** development kit. </br>
- **Pycharm** and **Google Colab** development environment.
- Installing the following packages:
    - **pretty_midi:** contains utility function/classes for handling MIDI data. </br>
    - **Keras:** is a high-level neural networks API, written in Python.</br>
    - **Tensorflow:** is an end-to-end open source platform for machine learning. </br>
    - **Flask:** is a lightweight WSGI web application framework. </br>
    - In addition, **numpy, os, glob, pickle, shutil, random** libraries were used.
## Training
To train the network you run **train.py**.
```
python train.py
```
The network will use every midi file in **data/midi_songs** to train the network. The midi files should contain a same type instruments to train.</br>
Weights are saved in folders according to the instrument types in the **train/weights** folder. Instrument types consist of numbers such as 0,1,2,16.
## Generate
Once you have trained the network you can generate midi file using **generate.py**.

```
python generate.py
```
The generated music creates a midi file with random numbers inside the **generate/songs/temp** folder.
## Run Interface
Run the **app.py** python script.
