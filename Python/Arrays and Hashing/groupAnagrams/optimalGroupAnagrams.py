class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}  # Regular dictionary

        for word in strs:
            key = "".join(sorted(word))  # Sorted characters are the hashable group key

            if key not in anagrams:
                anagrams[key] = []  # Manually initialize the list

            anagrams[key].append(word)

        return list(anagrams.values())
    
def main():
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    main()