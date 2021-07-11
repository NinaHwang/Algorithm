package Knight;

import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    static int knight(String position){
        String columns = "abcdefgh";
        int[] case1 = {2,1};
        int[] case2 = {2,-1};
        int[] case3 = {-2,1};
        int[] case4 = {-2,-1};
        int[] case5 = {1,2};
        int[] case6 = {1,-2};
        int[] case7 = {-1,2};
        int[] case8 = {-1,-2};
        int[][] cases = {case1, case2, case3, case4, case5, case6, case7, case8};

        int column = columns.indexOf(position.charAt(0));
        int row = Integer.parseInt(String.valueOf(position.charAt(1))) - 1;

        int answer = 0;
        for (int[] each_case: cases) {
            int c = column + each_case[0];
            int r = row + each_case[1];
            System.out.println(c + ' ' + r);
            if (c >= 0 && c < 9 && r >= 0 && r < 9) {
                answer ++;
            }
        }
        return answer;
    }
}
