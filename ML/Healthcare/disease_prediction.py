import numpy as np
import pandas as pd
from scipy.stats import mode
import matplotlib.pyplot as plt  
import seaborn as sns
import sklearn.preprocessing import LabelEncoder
import sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.svm import svc
from sklearn.naive_bayes import GaussianNB
frok sklearn.tree import DecisionTreeClassifier
from sklearn