#This is my record of learning numpy

import numpy as np

#np.ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None): low-level method for instantiating an array.
#shape is the only parameter that must have, should be a tuple containing the shape of the array we are going to construct
#dtype specifies the data type
#order specifies Row-major (C-style) or column-major (Fortran-style) order.
#buffer is an object for storeing data to load into the ndarray we are going to construct. If this parameter is specified, all parameters are interpreted. If not, only the three above are interpreted.
#example:
np.ndarray((2,2), buffer=np.array([[1,2], [3,4], [5,6]]))
np.ndarray((2,2), buffer=np.array([[1,2], [3,4], [5,6]]), offset=np.int_().itemsize, dtype=int)
