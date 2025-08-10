class Solution:
    def groupAnagrams(self, strs: list[str]):

        # rows = 3
        # cols = 4
        # # Initialize a 3x4 matrix with all zeros
        # sorted_list = [[0 for _ in range(cols)] for _ in range(rows)]
        # size_set = []
        # for i in range(len(strs)):
        #     size_set.append("".join(sorted(strs[i])))
        # new_set = set(size_set)
        # print(new_set)
        # for i in range(len(new_set)):
        #     new_list = []
        #     for j in range(0,len(strs)):
        #         word_j = strs[j]
        #         sorted_i = list(new_set)[i]
        #         sorted_j = "".join(sorted(word_j))
        #         if sorted_i == sorted_j and word_j not in sorted_list:
        #             print("Word = ", word_j, " <- index no = ", j, end=" ")
        #             new_list.append(word_j)
        #     sorted_list.append(new_list)
        #     print()
        
        #Dict where key=strs.sorted() value =1...strs.len



        size_set = []
        for i in range(len(strs)):
            size_set.append("".join(sorted(strs[i])))
        new_set = set(size_set)

        sorted_list = [[] for _ in range(len(new_set))]

        strsDict = {}
        j=0
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) not in strsDict:
                strsDict["".join(sorted(strs[i]))] = j
                j+=1
        print(strsDict)

        if(len(new_set) == 1):
            return strs

        for i in range(0, len(strs)):
            sorted_i = "".join(sorted(strs[i]))
            if sorted_i in strsDict:
                strsDictIndex = int(strsDict[sorted_i])
                sorted_list[strsDictIndex].append(strs[i])

        return sorted_list

def main():
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    main()