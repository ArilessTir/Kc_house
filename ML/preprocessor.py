from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import os
import sys
current_path = os.getcwd()
sys.path.append(current_path.replace('/ML',''))
import Config

continue_pip = Pipeline(steps=[ 
    ('scaler',MinMaxScaler()),
    ('poly', PolynomialFeatures(degree=4))
])


transformer = ColumnTransformer(
    transformers=[
        ('drop no sens features','drop', Config.REMOVE),
        ('drop geo','drop', Config.GEO),
        ('drop date','drop', Config.DATE_TRANSFORMATION),
        ('Scale continu',continue_pip, Config.CONTINUE),
        ('passthrough discrete','passthrough', Config.DISCRETE),
        ('passthrough binary','passthrough', Config.BINARY),
        ('passthrough year','passthrough', Config.YEAR)
    ]
)