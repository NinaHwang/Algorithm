package Time;

public class Solution {
    static long time(int n) {
        int answer = 0;
        for (int i=0; i<60; i++){
            String str_i = String.valueOf(i);
            for (int j=0; j<60; j++) {
                String str_j = String.valueOf(j);
                for (int k=0; k<n+1; k++){
                    String str_k = String.valueOf(k);
                    String total = str_k + str_j + str_i;
                    if (total.indexOf("3") != -1) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}
