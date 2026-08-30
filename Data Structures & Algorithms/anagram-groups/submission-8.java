class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Anagram - same characters, can be diff order 
        // permutation
        // but it must be meaningful words 
        // it is a list of string list ....
        // if(strs.isEmpty()) return strs;

        // a hashmap to store 
        // []
        Map<String, List<String>> groups = new HashMap<>();
        for(String every_str : strs){
            int[] count = new int[26];
            for( char c : every_str.toCharArray()){
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);

            groups.putIfAbsent(key, new ArrayList<>());
            groups.get(key).add(every_str);

        }
        return new ArrayList<>(groups.values());

    }
}
