from cython.parallel import prange, parallel, threadid
from libc.stdio cimport printf

cdef int n = 10
cdef int i
cdef int sum = 0

cdef int j = -1

with nogil, parallel():

    j = threadid()

    for i in prange(n):
        sum += i
        printf("%d: %d\n", i, j)

print sum

