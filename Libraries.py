import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
import os
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.layers import Conv2D, Dense, BatchNormalization, Activation, Dropout, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam #, RMSprop, SGD
from keras.callbacks import ModelCheckpoint,EarlyStopping
import datetime
from keras import regularizers
from keras.models import load_model
import matplotlib.pyplot as plt
from keras.utils.vis_utils import plot_model
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox
import sys
from functools import partial
from PIL import Image, ImageTk