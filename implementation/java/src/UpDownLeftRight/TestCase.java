package UpDownLeftRight;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class TestCase {
    public static void main(String[] args) {
        char[] directions = {'R','R','R','U','D','D'};

        ArrayList<Integer> case1 = Solution.upDownLeftRight(5, directions);

        System.out.println(case1.toString());
    }
}
