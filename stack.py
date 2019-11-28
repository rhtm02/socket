class Stack:
    def __init__(self):
        self.A=[]

    def isEmpty(self):
        return self.A==[]

    def push(self,item):
        self.A.append(item)

    def pop(self):
        n=len(self.A)
        temp = ""
        if n!=0:
            temp= self.A[n-1]
            del self.A[n-1]
        return temp

    def clear(self):
        self.A=[]

    def peek(self):
        n=len(self.A)
        if n>0: return self.A[n-1]

    def stackPrint(self):
        n = len(self.A)
        if n>0:
            for i in range(0,n):
                print(self.A[n-1-i])

if "__main__"==__name__:
    print("STACK MODULE")