class Stack:    # creating a Stack

    def __init__(self, cap = 100):
        self.capacity = cap
        self.arr = [0] * (self.capacity)
        self._top = -1
        self.sz = 0

    def push(self, value):
        if (self._top == self.capacity - 1):
            print("Overflow")
            return

        self._top += 1
        self.arr[self._top] = value
        self.sz += 1

    def pop(self):
        if (self._top == -1):
            print("Underflow")
            return 

        self._top -= 1
        self.sz -= 1
        return self.arr[self._top + 1]

    def top(self):
        return self.arr[self._top]

    def size(self):
        return self.sz 

    def empty(self):
        return self.sz == 0

    def full(self):
        return self.sz == capacity

    def display(self):
        for i in range(self._top, -1, -1):

            print(self.arr[i], end = " ")
        print()


def precedence(p):       # creating precedence of the operators

    if (p == "^"):
        return 3
    if (p == "*" or p == "/"):
        return 2
    if (p == "+" or p == "-"):
        return 1 
    return 0 


def Infix_to_Postfix(s):   # conversion from infix to postfix

    stack = Stack()
    result = ""

    for i in range(0, len(s)):
        if (s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/" or s[i] == "^"):

            while (not stack.empty() and precedence(s[i]) <= precedence(stack.top())):
                result += stack.top()
                stack.pop()
            stack.push(s[i])

        elif (s[i] == "("):
            stack.push(s[i])

        elif (s[i] == ")"):
            while (not stack.empty() and stack.top() != "("):
                result += stack.top()
                stack.pop()
            stack.pop()

        else:
            result += s[i]

    while (not stack.empty()):
        result += stack.top()
        stack.pop()

    return result

s = input()

print(Infix_to_Postfix(s))
