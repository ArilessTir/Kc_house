import  preprocessor
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge



model = Pipeline(steps=[ 
    ('preprocessor', preprocessor.transformer),
    ('model', Ridge(random_state=42, alpha=0.05))
])

