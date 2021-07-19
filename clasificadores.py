import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn import linear_model
def getClasificador():
    data = pd.read_csv("./util/aluguel.csv")
    mapping = LabelEncoder()
    data["cidade_Map"] = mapping.fit_transform(data["cidade"])
    remover = ['cidade',"aluguel",'total']
    x = data.drop(remover,axis=1)
    x = x.values
    y = data['total']
    y = y.values
    clf = linear_model.LinearRegression()
    return clf.fit(x,y)

def getPreticao(dados):
    return getClasificador().predict([dados])[0]

