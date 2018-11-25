from pylab import bone, pcolor, colorbar, plot, show

class Som_Plotter():

    def __init__(self, som, data_manager):
        self.som = som
        self.data_manager = data_manager

    def plot_som(self):
        bone()
        pcolor(self.som.distance_map().T)
        colorbar()
        markers = ['o', 's']
        colors = ['r', 'g']
        x = self.data_manager.get_scaled_x()
        y = self.data_manager.get_y()
        for i, each in enumerate(x):
            w = self.som.winner(each)
            plot(w[0] + 0.5,
                 w[1] + 0.5,
                 markers[y[i]],
                 markeredgecolor=colors[y[i]],
                 markerfacecolor='None',
                 markersize=10,
                 markeredgewidth=2)
        show()
