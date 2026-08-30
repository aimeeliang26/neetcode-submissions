class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Anagram - same characters, can be diff order 
        // permutation
        // but it must be meaningful words 
        // it is a list of string list ....
        // if(strs.isEmpty()) return strs;
        Map<String, List<String>> groups = new HashMap<>();
        // if(strs.length <= 1){
        //     return new ArrayList<>(strs);
        // }
        for(String s : strs){
            int[] count = new int[26]; //store counts of each char
            for(char c : s.toCharArray()){
                count[c -'a']++;
            }  
    
         // Convert counts to a string key
            String key = Arrays.toString(count); // simple & readable

            // Use get/put instead of computeIfAbsent
            List<String> bucket = groups.get(key);
            if (bucket == null) {
                bucket = new ArrayList<>();
                groups.put(key, bucket);
            }
            bucket.add(s);
        }
        return new ArrayList<>(groups.values());   

    }
}
