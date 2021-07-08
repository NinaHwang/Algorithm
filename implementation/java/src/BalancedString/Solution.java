package BalancedString;

public class Solution {
    public static String balancedString(int n) {
        String str = "abcdefghijklmnopqrstuvwxyz";
        String answer = "";
        int cnt = 0;
        int a = n;

        while (n > 26) {
            cnt++;
            n -= 26;
        }

        for (int i=0; i < cnt; i++) {
            answer += str;
        }

        String begin = "";
        String end = "";

        if (n % 2 == 0) {
            begin = str.substring(0, n/2);
            end = str.substring(26-n/2);
            answer += begin;
            answer += end;
            return answer;
        }

        String aToString = Integer.toString(a);
        int sumOfDigits = 0;
        for (int i=0; i<aToString.length(); i++) {
            sumOfDigits += Integer.parseInt(aToString.substring(i,i+1));
        }
        if (sumOfDigits % 2 == 0) {
            begin = str.substring(0, (n+1)/2);
            if (n != 1) {
                end = str.substring(26-((n-1)/2));
            }
        } else {
            if (n != 1) {
                begin = str.substring(0, (n - 1) / 2);
            }
            end = str.substring(26 - ((n + 1) / 2));
        }
        return answer + begin + end;
    }
}
