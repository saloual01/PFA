from sklearn import preprocessing
import pandas as pd
housing = pd.read_csv("PFA/a.csv")
d = preprocessing.normalize(housing)
scaled_df = pd.DataFrame(d, columns=names)