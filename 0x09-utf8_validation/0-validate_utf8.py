def validUTF8(data):
    bpc = 8
    mno = 4

    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (bpc - 1)
        if number == 0:  
            index += 1
            continue

        
        number_of_ones = 0
        while True:  
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (bpc - number_of_ones - 1)
            if number == 1:
                number_of_ones += 1
            else:
                break

            if number_of_ones > mno:
                return False 
        if number_of_ones == 1:
            return False  

        index += 1  

        
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False  

        for i in range(index, index + number_of_ones - 1):
            number = data[i]

            number >>= (bpc - 1)
            if number != 1:
                return False
            number >>= (bpc - 1)
            if number != 0:
                return False

            index += 1

    return True