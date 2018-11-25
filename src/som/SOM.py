from src.som.minisom import MiniSom
import numpy as np

class SOM():

    def __init__(self, data_manager):
        self.data_manager = data_manager

    def train_som(self, x, x_units, y_units, input_length, number_iterations):
        self.som = MiniSom(x=x_units, y=y_units, input_len=input_length)
        self.som.random_weights_init(x)
        self.som.train_random(data=x, num_iteration=number_iterations)
        return self.som

    def get_scaled_frauds(self):
        mappings = self.som.win_map(self.data_manager.get_scaled_x())
        return np.concatenate((mappings[(8, 1)], mappings[(6, 8)]), axis=0)