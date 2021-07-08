//https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/?category[]=Stack&category[]=Stack&difficulty[]=1&page=1&query=category[]Stackdifficulty[]1page1category[]Stack#

package NextGreaterElement;

import java.util.Arrays;
import java.util.Stack;

public class Solution {
    static long[] nextLargerElement(long arr[], int n) {
        long[] answer = new long[n];
        Arrays.fill(answer, -1);
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.lastElement()] < arr[i]) {
                answer[stack.lastElement()] = arr[i];
                stack.pop();
            }
            stack.push(i);
        }
        return answer;
    }
}

// Execution Time:2.54