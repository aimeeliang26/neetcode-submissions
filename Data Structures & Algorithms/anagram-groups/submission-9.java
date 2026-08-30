class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Anagram - same characters, can be diff order 
        // permutation
        // but it must be meaningful words 
        // it is a list of string list ....
        // if(strs.isEmpty()) return strs;

        // a hashmap to store 
        // []
        Map<String, List<String>> groups = new HashMap<>(); //Hashmap
        for(String every_str : strs){
            int[] count = new int[26];
            for( char c : every_str.toCharArray()){
                count[c - 'a']++; // char
            }
            String key = Arrays.toString(count); // toString for int to String

            groups.putIfAbsent(key, new ArrayList<>()); //putIfAbsent
            groups.get(key).add(every_str);

        }
        return new ArrayList<>(groups.values()); // values() gives Collection, not List; new ArrayList<>() is also a stable snapshot

    }
}
