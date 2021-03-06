import pipeline
from sklearn.model_selection import train_test_split, learning_curve
from functions.get_data import get_dataset, get_Xy
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pickle
import matplotlib.pyplot as plt 
from plot_learning_curve import plot_learning_curve
import os

def run_training():
    data = get_dataset()

    X,y = get_Xy(data, 'price')


    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

    print('training....')

    ###### Fiting

    model = pipeline.model.fit(X_train,y_train)
    y_pred = model.predict(X_test)

    ###### Metrics

    f = open('metrics.txt','w')
    f.write('### Metrics ###')
    f.write(f'RMSE:{np.sqrt(mean_squared_error(y_test, y_pred))}\n')
    f.write(f'R²:{r2_score(y_test, y_pred)*100}')
    f.close()
    
    ##### Learning curve

    plot_learning_curve(model,X,y)

    filename = 'model_registry/model.sav'
    pickle.dump(model, open(filename, 'wb'))

if __name__ == '__main__':
    run_training()