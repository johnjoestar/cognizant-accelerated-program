# Part 1: Building and Optimizing a CNN

# need to use python version below 3.13 to make tensorflow work
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

spam_data = pd.read_csv('C:/Users/user/Downloads/spam.csv')

spam_data['v1'] = spam_data['v1'].map({'spam': 1, 'ham': 0}) # changes feature to binary
texts = spam_data['v2'].values
labels = spam_data['v1'].values

# padding and tokenization
tokenizer = Tokenizer(num_words = 10000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_seuqences(texts)
padded_sequences = pad_sequences(sequences, maxlen=100, padding='post', truncating='post')

# train-test split
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

# Part 2: Debugging Model Failures 

# Part 3: Evaluating Model Effectiveness

# Part 4: Creative Application