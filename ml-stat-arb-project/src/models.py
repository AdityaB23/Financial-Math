
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor

def train_model(X,y,model_type="ridge"):
    if model_type=="ridge":
        model = Ridge(alpha=1.0)
    else:
        model = RandomForestRegressor(n_estimators=100, max_depth=5)

    model.fit(X,y)
    return model
