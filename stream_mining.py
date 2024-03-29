# -*- coding: utf-8 -*-
"""stream_mining.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHKbJ3KLUITTHJRxegzbTvA_-6M7eO5v
"""

!pip install -U scikit-multiflow

from skmultiflow.data import AGRAWALGenerator
from skmultiflow.trees import HoeffdingTree
from skmultiflow.evaluation import EvaluatePrequential
import numpy as np

# 1. Create a stream
stream = AGRAWALGenerator()
stream.prepare_for_use()

# 2. Instantiate the HoeffdingTree classifier
ht = HoeffdingTree()

# # 3. Setup the evaluator
# evaluator = EvaluatePrequential(show_plot=False,
#                                 pretrain_size=500,
#                                 max_samples=500)

# # 4. Run evaluation
# evaluator.evaluate(stream=stream, model=ht)

def base_classifier(e, U, I, L, D, wd, ws):
  return print("I am here")

# all initialization
p = 0
I = 50
B = []
k = 0
i = 0
e = 0.20
wd = 0.5
ws = 0.5
D = 3
L = 2
Total_stream = 500
buffer_class0 = []
buffer_class1 = []
dynamic_classifier = []

def stream_fun(I):
  mystream = stream.next_sample(I)
  buffer_fun(mystream) 

def buffer_fun(mystream):
  for i in range(10):
    if mystream[1][i] == 0:
      buffer_class0.append(mystream)
    else:
      buffer_class1.append(mystream)
  print(len(buffer_class0))
  print(len(buffer_class1))

def train_on_instance(mystream):
  ht.partial_fit(mystream)

def dynamic_classifier(i, x):
  dynamic_classifier[i] = ht.predict(x)
  return dynamic_classifier
  

def reinforcement_weight_adjust(x, L, D, wd, ws, DCIR0, DCIR1):
  if(DCIR0 < 1/L):
    for i in range(D):
      dynamic_classifier(i, x)

def base_classifier(e, buffer_class0, buffer_class1, I, L, D, wd, ws):
    xi = stream_fun(e*I-1)
    DCIR0 = dcir(0)
    DCIR1 = dcir(1)
    reinforcement_weight_adjust(xi, L, D, wd, ws, DCIR)
    h0 = hn(0)
    h1 = hn(1)
    c_new = ht.predict(xi)
    if h0 < (I*e)/L:
      value = (I*e)/L - hn(0)
      rn = buffer_class0.pop(value)

def weights(D):
  ws = 0.5
  wd = 0.5
  wD = []
  for i in range(D):
    wD.append(1/D)