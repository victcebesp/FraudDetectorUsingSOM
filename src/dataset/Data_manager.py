import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class Data_manager():

    def __init__(self, path):
        self.path = path
        self.split_x_and_y()

    def split_x_and_y(self):
        dataset = pd.read_csv(self.path)
        self.x = self.scale(dataset.iloc[:, :-1].values)
        self.y = dataset.iloc[:, -1].values

    def get_scaled_x(self):
        return self.x

    def get_y(self):
        return self.y

    def scale(self, x):
        self.min_max_scaler = MinMaxScaler(feature_range=(0, 1))
        return self.min_max_scaler.fit_transform(x)

    def get_raw_frauds(self, scaled_frauds):
        return self.min_max_scaler.inverse_transform(scaled_frauds)
