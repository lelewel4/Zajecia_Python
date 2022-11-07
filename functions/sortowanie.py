def sortowanie(array:list[int]):                            #sortowanie tylko liczb
    if(len(array)==0):
        print("Pusta lista")
        return array
    else:
        len_array = len(array)
        for i in range(len_array - 1):
            for j in range(len_array - i - 1):
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array



