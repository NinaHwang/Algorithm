package RotateString;

import java.util.ArrayList;

public class Solution {
    static ArrayList<Character> rotateString(int n, int q, String s, int q1[], int q2[]) {
        ArrayList<Character> answer = new ArrayList<Character>();

        int idx = 0;
        int rotate = 0;

        for (int i=0; i<q1.length; i++) {
            if (q1[i] == 1) {
                idx = n-((q2[i]+rotate) % n);
                rotate = (q2[i]+rotate) % n;
            } else {
                if (q2[i] + idx >= n) {
                    answer.add(s.charAt(q2[i]+idx-n));
                } else {
                    answer.add(s.charAt(q2[i]+idx));
                }
            }
        }
        return answer;
    }
}

// https://practice.geeksforgeeks.org/problems/lazy-pasha1646/1/?category[]=implementation&category[]=implementation&problemStatus=solved&problemType=functional&page=1&sortBy=submissions&query=category[]implementationproblemStatussolvedproblemTypefunctionalpage1sortBysubmissionscategory[]implementation
// Execution Time:3.02