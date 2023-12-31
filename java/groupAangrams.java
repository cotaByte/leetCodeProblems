import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Arrays;

/*
 * 49. Group Anagrams --- Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
 * 
 */
public class groupAangrams {

    public static List<List<String>> groupAnagrams(String[] strs) {
        // create a hashMap to storage by a key all the diferent anagrams founded
        Map<String, List<String>> hashMap = new HashMap<>();
        for (String word : strs) {
            char[] letters = word.toCharArray();
            // sort the letters to check if the anagram exists
            Arrays.sort(letters);
            String sortedAnagram = new String(letters);

            if (!hashMap.containsKey(sortedAnagram)) {
                // if not exists, create the entry
                hashMap.put(sortedAnagram, new ArrayList<>());
            }

            // if already exists, just put the word on the key
            hashMap.get(sortedAnagram).add(word);

        }
        return new ArrayList<>(hashMap.values());

    }

    public static void main(String[] args) {
        String[] strs = { "eat", "tea", "tan", "ate", "nat", "bat" };
        List<List<String>> gruposAnagramas = groupAnagrams(strs);
        for (List<String> grupo : gruposAnagramas) {
            System.out.println(grupo);
        }
    }

}
