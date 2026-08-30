class Solution {
    public boolean isValidSudoku(char[][] board) {
        // iterate through the boxes 
        // Which datastructure will be good for checking duplicates?
            // HashMap to check dup
        
        HashMap<Integer, Set<Character>> rowMap = new HashMap<>();
        HashMap<Integer, Set<Character>> colMap = new HashMap<>();
        HashMap<String, Set<Character>> sqrMap = new HashMap<>();
        //row - board[i]
        //col- board[i][j]
        //sqr - board[i/3]
        int bLen = board.length;
        // for rows checking dup
        for(int i = 0; i<bLen; i++){
            for(int j = 0; j<bLen; j++){
                if(board[i][j] == '.'){
                    continue;
                }
                String sqrKey = (i/3) + "," + (j/3); 
                if(rowMap.computeIfAbsent(i, k-> new HashSet<>()).contains(board[i][j])||
                colMap.computeIfAbsent(j, k-> new HashSet<>()).contains(board[i][j]) ||
                sqrMap.computeIfAbsent(sqrKey, k-> new HashSet<>()).contains(board[i][j]) ){
                    return false;
                }
            
                rowMap.get(i).add(board[i][j]);
                colMap.get(j).add(board[i][j]); 
                sqrMap.get(sqrKey).add(board[i][j]);
            }
        } 
        return true;      
    }
}
