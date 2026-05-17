import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)
    trace = 0
    n,_ = A.shape

    for i in range(0,n):
        trace+=A[i,i]

    return trace