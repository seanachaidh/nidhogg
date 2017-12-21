from scipy.cluster import hierarchy
from matplotlib import pyplot as plt
import numpy as np
import pandas

# What should this tree be capeble of doing?
# 1. Be non-binary
#   That is: When datapoints are of equal distance, it should be both a child of its parent
#   Can be emulated: Scan the tree for brances with same length and copy the children under the same node

class Tree:
    
    def load_from_file(self,filename):
        dnamatrix = pandas.read_csv(filename,header=None)
        print(dnamatrix)
        self.data = np.append(self.data, dnamatrix, axis=0)
        
    def gen_tree(self):
        self.tree = hierarchy.linkage(self.data, 'ward')
        
    def plot_tree(self):
        plt.figure()
        plt.title('testtree')
        hierarchy.dendrogram(self.tree, truncate_mode='lastp', p=3)
        plt.show()
    
    def __init__(self):
        self.data = np.empty((0,20), float)
        self.tree = []
    def __str__(self):
        return str(self.data)
    
