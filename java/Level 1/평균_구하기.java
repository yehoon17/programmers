class Solution {
    public double solution(int[] arr) {
        int sum = 0;
        for(int x: arr){
            sum += x;
        }
        return (double)sum / arr.length;
    }
}
