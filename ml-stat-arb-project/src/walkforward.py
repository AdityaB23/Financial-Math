
import pandas as pd

def walk_forward(X, y, model_func, train_size=1000):

    preds = []
    dates = []

    for i in range(train_size, len(X)-1):
        X_train = X.iloc[i-train_size:i]
        y_train = y.iloc[i-train_size:i]

        model = model_func(X_train, y_train)

        pred = model.predict(X.iloc[i:i+1])[0]

        preds.append(pred)
        dates.append(X.index[i])

    return pd.Series(preds, index=dates)
