class Solution():
    def minMaxDifference(self, num):
        # numSet = set(str(num))
        # minDigit = min(numSet)
        # maxDigit = max(numSet)
        # numList = list(str(num))
        # smallest = 0
        # biggest = 0
        # for i in range(len(numList)):
        #     if numList[i] == minDigit:
        #         biggest += 9
        #         biggest *= 10
        #     else:
        #         biggest += int(numList[i])
        #         biggest *= 10
        # biggest /= 10        
        # for i in range(len(numList)):
        #     if numList[i] == maxDigit:
        #         smallest += 0
        #         smallest *= 10   
        #     else: 
        #         smallest +=int(numList[i])
        #         smallest *=10
        # smallest /=10
        # return biggest-smallest
        biggest = 0
        smallest = 0
        numList=list(str(num))
        print("Number List = ", numList[0])
        dictBig = {}
        dictSmall = {}
        for i in range(len(numList)):
            if(int(numList[i])<9 and len(dictBig)==0):
                dictBig = {numList[i]: "9"} #map the earliest smallest number that is obviously not 9 
                print("Dict Big=",dictBig)
            if(int(numList[i])>0 and len(dictSmall)==0):
                dictSmall = {numList[i]: "0"}
                print("Smallest Dictonary =",dictSmall)
        for i in str(num):
            if i in dictBig:
                biggest += int(dictBig[i])
            else:
                biggest += int(i)
            biggest *= 10
        
        for i in str(num):
            if i in dictSmall:
                smallest += int(dictSmall[i])
            else:
                smallest += int(i)
            smallest *= 10
        print("Smallest =",smallest/10)
        print("Biggest = ", biggest/10)
        return int((biggest/10)-(smallest/10))
def main():
    num = 456
    print((str(num)))
    print(Solution().minMaxDifference(num))

if __name__ == "__main__":
    main()