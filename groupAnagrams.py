class Solution:
    def groupAnagrams(self, strs: list[str]):

        sorted_list = []
        size_set = []
        for i in range(len(strs)):
            size_set.append("".join(sorted(strs[i])))
        new_set = set(size_set)
        print(new_set)
        for i in range(len(new_set)):
            new_list = []
            for j in range(0,len(strs)):
                word_j = strs[j]
                sorted_i = list(new_set)[i]
                sorted_j = "".join(sorted(word_j))
                if sorted_i == sorted_j and word_j not in sorted_list:
                    print("Word = ", word_j, " <- index no = ", j, end=" ")
                    new_list.append(word_j)
            sorted_list.append(new_list)
            print()
        return sorted_list

def main():
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    main()