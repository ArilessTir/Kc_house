import pandas as pd

def get_dataset(id = "11GPbB_mjwVt0EdYKGGB9jjZ8aledjugC"):
    url = f'https://drive.google.com/uc?export=download&id={id}'
    return pd.read_csv(url)

def get_Xy(dataset, target):
    X = dataset.drop([target],axis=1)
    y = dataset[target]
    return X,y


def abc ():
    return "ari"