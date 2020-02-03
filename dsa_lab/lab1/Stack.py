class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        self.stack.pop()

    def __str__(self):
        return str(self.stack)

    def peek(self):
        print(self.stack[len(self.stack) - 1])

    def isEmpty(self):
        if self.stack == []:
            print("Empty")
        else:
            print("Not Empty")



def main():
    s = Stack()
    s.push(2)
    s.push(5)
    s.push(8)
    s.push(9)
    print(s)
    s.pop()
    print(s)
    s.isEmpty()

if __name__ == "__main__":
    main()