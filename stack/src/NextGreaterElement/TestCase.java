package NextGreaterElement;

import java.util.Arrays;

public class TestCase {
    public static void main(String[] args) {
        long[] test1 = {1,3,2,4};
        long[] test2 = {6,8,9,1,3};
        long[] test3 = {7,8,1,4};

        long[] answer1 = Solution.nextLargerElement(test1, test1.length);
        long[] answer2 = Solution.nextLargerElement(test2, test2.length);
        long[] answer3 = Solution.nextLargerElement(test3, test3.length);

        System.out.println(Arrays.toString(answer1));
        System.out.println(Arrays.toString(answer2));
        System.out.println(Arrays.toString(answer3));
    }
}
