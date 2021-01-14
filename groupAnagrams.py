# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def groupAnagrams(strs):
    picked = set()
    separated = []
    for i in range(len(strs)):
        if i in picked:
            continue
        found = [strs[i]]
        for j in range(i+1, len(strs)):
            if j in picked:
                continue
            if sorted(strs[i]) == sorted(strs[j]):
                found.append(strs[j])
                # print("added " + strs[j])
                picked.add(j);
        separated.append(found)
    
    return separated




strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))