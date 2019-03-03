import tensorflow.keras as keras
import pandas as pd
import os
from time import time

data_dir = 'train_data/text_files'
label_file = 'train_data/labels.csv'

label_cols = ['level', 'language', 'popularity', 'legit']
labels = pd.read_csv(label_file, na_values=0, sep=',', names=label_cols, skipinitialspace=True).values

max_words = 5000
tokenizer = keras.preprocessing.text.Tokenizer(num_words=max_words)

dir_list = os.listdir(data_dir)
dir_list.sort()
data = []
for file_name in dir_list:
    print("Reading " + str(file_name) + "...")
    file_name = os.path.join(data_dir, file_name)
    f = open(file_name, 'r', encoding='ISO-8859-1')
    data.append(f.read())
    f.close()
tokenizer.fit_on_texts(data)
data = tokenizer.texts_to_matrix(data, mode='tfidf')
print(data)

model = keras.Sequential()
model.add(keras.layers.Dense(64, activation='relu', input_shape=(max_words,)))
model.add(keras.layers.Dropout(rate=0.2))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dropout(rate=0.2))
model.add(keras.layers.Dense(4))

opt = keras.optimizers.SGD(lr=0.00001)
tensorboard = keras.callbacks.TensorBoard(log_dir='train_data/logs/{}'.format(time()))
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['acc'])
model.fit(x=data, y=labels, epochs=10000, batch_size=4, validation_split=0.1, callbacks=[tensorboard])