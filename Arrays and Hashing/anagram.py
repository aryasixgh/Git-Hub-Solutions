class Solution(object):
    def isAnagram(self, s, t):
        dict_s = {}
        dict_t = {}
        if len(s)!=len(t):
            return False
        #initialization
        for i in s:
            dict_s[i] = 0
        for i in t:
            dict_t[i] = 0
        #Incrementing letter counts
        for i in s:
            dict_s[i]+=1
        for i in t:
            dict_t[i]+=1
        
        print(dict_s)
        print(dict_t)

        #comparing the two dictonariez
        for i in s:
            if dict_s[i] != dict_t[i]:
                return False

        return True
def main():
    s = "aacc"
    t = "ccac" 
    print(Solution().isAnagram(s, t))
if __name__ == "__main__":
    main()