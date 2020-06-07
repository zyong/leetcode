

def test(method):
    # ret = obj.qsort([9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0,0])
    input = [9,1,4,2,1,3,45,5,6,7,89,2,3,4,5,63,2,1,3,4,21,21,12]
    print("test method {}".format(method))
    print("test input data {}".format(input))
    ret = method(input)
    if len(input) == len(ret):
        print("length of input and output is equal")
    else:
        print("output length is not equal")

    flag = True
    for j in range(len(ret)):
        if j + 1 < len(ret) and ret[j] > ret[j+1]:
            flag = False
            break

    if not flag:
        print("sort failed,output {}".format(ret))
    else:
        print("sort success,output {}".format(ret))