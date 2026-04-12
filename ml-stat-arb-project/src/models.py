
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor

def train_ridge(X,y):
    model = Ridge(alpha=1.0)
    model.fit(X,y)
    return model

def train_rf(X,y):
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X,y)
    return model
