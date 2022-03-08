import numpy 
from array import *
def Transpose(M):
    arr = numpy.array(M)
    num_list = arr.transpose().tolist()
    return(num_list)
    