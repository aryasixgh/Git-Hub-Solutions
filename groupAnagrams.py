class Solution:
    def groupAnagrams(self, strs: list[str]):

        sorted_dict = []
        # ans_lists = []
        # final_list =[]
        # for i in range(len(strs)):
        #     sorted_str = sorted(strs[i])
        #     sorted_dict.append(["".join(sorted_str),i])
        #     for j in range(i, len(strs)):
        #         if sorted_dict[i][0] == sorted_dict[j][0]:
        #             ans_lists.append(sorted_dict[i][1])
        #     final_list.append([])
        # print(sorted_dict[2][0])

        print(set(strs))
        for i in range(len(set(strs))):
            for j in range(i,len(strs)-i):
                if "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
                    print("".join(sorted(strs[i])), " <- index no = ", j, end=" ")
                    
            print()

        return sorted_dict

def main():
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    main()