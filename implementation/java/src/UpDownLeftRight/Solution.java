package UpDownLeftRight;

import java.util.ArrayList;

public class Solution {
    static ArrayList<Integer> move(int x, int y, int n, char direction) {
        if (direction == 'R') {
            int _x = x + 1;
            if (_x <= n) {
                x = _x;
            }
        } else if (direction == 'L') {
            int _x = x - 1;
            if (_x > 0) {
                x = _x;
            }
        } else if (direction == 'U') {
            int _y = y - 1;
            if (_y > 0) {
                y = _y;
            }
        } else {
            int _y = y + 1;
            if (_y <= n) {
                y = _y;
            }
        }
        ArrayList<Integer> nextPosition = new ArrayList<Integer>();
        nextPosition.add(y);
        nextPosition.add(x);
        return nextPosition;
    }

    static ArrayList<Integer> upDownLeftRight(int n, char directions[]) {
        ArrayList<Integer> currentPosition = new ArrayList<Integer>();
        currentPosition.add(1);
        currentPosition.add(1);
        for (int i=0; i<=n; i++) {
            currentPosition = move(currentPosition.get(1), currentPosition.get(0), n, directions[i]);
        }
        return currentPosition;
    }
}
