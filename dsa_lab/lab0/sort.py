
def main():
    array = []
    noOfElements = input('Enter number of elements:')
    noOfElements = int(noOfElements)
    for i in range(0,noOfElements):
        element = int(input())
        array.append(element)
    print(array) 

    for i in range(1,noOfElements):
        j = i-1
        key = array[i]
        while(j>=0 and array[j]>=key):
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key

    print(array)

if __name__ == "__main__":
    main()