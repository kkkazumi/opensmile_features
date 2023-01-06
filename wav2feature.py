from scipy.io import arff
import numpy as np
import pandas as pd

import subprocess

def arff2feature(arff_filename):
    #filename = "a.arff"
    subprocess.run(["./remove.sh",arff_filename])
    dataset= arff.loadarff(arff_filename)
    ds = pd.DataFrame(dataset[0])
    print(ds)

filename = "b.arff"
arff2feature(filename)
