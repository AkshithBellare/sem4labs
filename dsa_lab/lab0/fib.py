
def fibi(noOfTerms):
    noOfTerms = int(noOfTerms)
    first = 0
    second = 1
    print('Iterative way')
    while(noOfTerms>=1):
        print(first,end=' ')
        temp = first
        first = second
        second = second + temp
        noOfTerms -= 1


def fibr(noOfTerms):
   noOfTerms = int(noOfTerms)
   if(noOfTerms == 1):
       return 0
   elif(noOfTerms == 2):
        return 1
   elif (noOfTerms > 2):
        return fibr(noOfTerms-1) + fibr(noOfTerms -2)

def main():
    noOfTerms = input('Enter the number of terms:')
    #fibi(noOfTerms)
    noOfTerms = int(noOfTerms)
    #recurive version
    for i in range(1,noOfTerms+1):
        print(fibr(i),end=' ')
if __name__ == "__main__":
    main()