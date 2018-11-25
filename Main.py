from src.dataset.Data_manager import Data_manager
from src.plot.Som_Plotter import Som_Plotter
from src.som.SOM import SOM

data_manager = Data_manager('data/Credit_Card_Applications.csv')
x = data_manager.get_scaled_x()

som = SOM(data_manager).train_som(x=x, x_units=10, y_units=10, input_length=15, number_iterations=100)

Som_Plotter(som, data_manager).plot_som()

frauds = data_manager.get_raw_frauds(som.get_scaled_frauds())

print(frauds)