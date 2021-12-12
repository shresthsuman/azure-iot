import numpy as np
from numpy import random
from numpy.core.fromnumeric import size

class Linear_Sensor:
    """
    Linear Sensor 
    """
    def __init__(self, slope=1, intercept=0):
        self.slope = slope
        self.intercept = intercept

    def gen_data(self):
        x = np.random.uniform(1, 1000)
        noise_x = np.random.normal(0, 1.)
        noise_y = np.random.normal(0, 1.)
        _x = x + x * noise_x

        return x, self.slope * _x + self.intercept + noise_y




if __name__ == "__main__":
    ls = Linear_Sensor()
    x, y = [], []
    for i in range(1000):
        sen_dat = ls.gen_data()
        x.append(sen_dat[0])
        y.append(sen_dat[1])


    import plotly.express as px
    fig = px.scatter(x=x, y=y)
    fig.show()