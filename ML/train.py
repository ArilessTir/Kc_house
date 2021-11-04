from math import pi
import pipeline
from sklearn.model_selection import train_test_split
from functions.get_data import get_dataset, get_Xy
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

data = get_dataset()

X,y = get_Xy(data, 'price')


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)


if __name__ == '__main__':

    print('training....')

    model = pipeline.model.fit(X_train,y_train)
    y_pred = pipeline.model.predict(X_test)

    ###### Metrics

    print(np.sqrt(mean_squared_error(y_test, y_pred)))
    print(r2_score(y_test, y_pred))
    