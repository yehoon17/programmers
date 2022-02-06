class Solution {
    public int divisor(int n){
        int cnt = 1;
        int temp = 1;
        int d = 2;
        while(n > 1){
            if(n % d == 0){
                n = n / d;
                temp += 1;                    
            }
            else{
                cnt *= temp;
                temp = 1;
                d += 1;
            }
        }
        
        return cnt * temp;
    }
    
    
    public int solution(int left, int right) {
        int answer = 0;
        for(int i=left; i<=right; i++){
            int cnt = divisor(i);
            if(cnt % 2 == 0){
                answer += i;
            }
            else{
                answer -= i;
            }
        }
        return answer;
    }
}
