class MinStack:
    def __init__(self):
        print("Constructor Called")
        self.stackObject = []
        return None

    def push(self, val: int) -> None:
        self.stackObject.append(val)
        return None

    def pop(self) -> None:
        self.stackObject.pop()
        return None    

    def top(self) -> int:
        return self.stackObject[len(self.stackObject)-1]

    def getMin(self) -> int:
        return min(self.stackObject)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
def main():
    obj = MinStack()
    print(obj.push(10))
    obj.push(2)
    obj.push(34)
    print("Min" , obj.getMin())
    print("Top ",obj.top())
    obj.pop()

    print(obj.stackObject)

if __name__ == '__main__':
    main()