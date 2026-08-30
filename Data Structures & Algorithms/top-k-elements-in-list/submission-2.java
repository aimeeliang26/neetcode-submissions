class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // hashmap to store counts
        Map<Integer, Integer> count = new HashMap<>();
        // pq of size k to keep track of k most frequent 
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) ->(a[0]-b[0]) );
        // for loop to store those elements to new int[] to return

        for(int i = 0; i<nums.length; i++){
            // 
            count.put(nums[i], count.getOrDefault(nums[i], 0)+1);
        }

        // store it in pq 
        for(Map.Entry<Integer, Integer> entry : count.entrySet()){
            pq.offer(new int[]{entry.getValue(), entry.getKey()});
            if(pq.size()>k){
                pq.poll();
            }
        }
        int[] res = new int[k];
        for(int i = 0; i < k ; i ++){
            res[i] = pq.poll()[1];
        }
        return res;
    }
}
