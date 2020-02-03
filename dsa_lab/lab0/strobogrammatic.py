def sfind(number,length):
    if number==0: return [""]
    if number == 1:
        return ["1","0","8"]
    
    middles = sfind(number-2,length)
    result = []

    for middle in middles:
        if number!=length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("6" + middle + "9")
        result.append("9" + middle + "6")
    return result


def strobogrammatic(number):
    strobo = sfind(number)
    return strobo




def main():
    number = int(input('Enter the number of digits:'))
    strobo = strobogrammatic(number)
    print(strobo)

if __name__ == "__main__":
    main()