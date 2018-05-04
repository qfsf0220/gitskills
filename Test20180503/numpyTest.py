import numpy as np
import numpy


def main():
    list1= [[1,3,5],[2,4,6]]
    print(list1)
#1
    npl1 = numpy.array(list1)
    print(npl1.shape)
    print(npl1.dtype)
    print(npl1.size)
    #2
    print(numpy.zeros([2, 4]))
    print(np.ones([1, 3]))
    print(np.random.rand(3,3))
    print(np.random.randint(1,4,20))



if __name__ == '__main__':
    main()
