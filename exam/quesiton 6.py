def deleteElement(array,index):
    if index<0 or index>= len(array):
        print("invalid index")
        return array
    
    array.pop(index)
    return array

list=[3, 7,1, 9, 4]
print(deleteElement(list, 7))
