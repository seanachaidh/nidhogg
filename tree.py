from scipy.cluster import hierarchy
import numpy as np
import pandas

class Tree:
    
    def load_from_file(self,filename):
        dnamatrix = pandas.read_csv(filename,header=None)
        print(dnamatrix)
        np.append(self.data, dnamatrix, axis=0)
    
    def __init__(self):
        self.data = np.array([])
        self.tree = []
    def __str__(self):
        pass
    
