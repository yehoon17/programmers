class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        int zero = 0;
        int match = 0;
        
        for(int i: lottos){
            if(i == 0){
                zero += 1;
            }
            else{
                for(int n: win_nums){
                    if(i == n){
                        match += 1;
                    }
                }
            }
        }
        
        int max_rank = Math.min(7 - zero - match, 6);
        int min_rank = Math.min(7 - match, 6);
        
        answer[0] = max_rank;
        answer[1] = min_rank;
        return answer;
    }
}
