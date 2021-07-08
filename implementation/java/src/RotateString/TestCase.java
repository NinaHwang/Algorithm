package RotateString;

import java.util.ArrayList;

public class TestCase {
    public static void main(String[] args) {

        int q1[] = {1,2,2,1,2};
        int q2[] = {2,0,6,4,1};

        ArrayList<Character> case1 = Solution.rotateString(7, 5, "abcdefg", q1, q2);

        System.out.println(case1.toString());
    }
}
