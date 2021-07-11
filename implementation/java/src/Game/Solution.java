package Game;

import java.util.Arrays;

public class Solution {
    static int[] turn(int[][] map, int[] current_position) {
        int row = current_position[0];
        int column = current_position[1];
        int direction = current_position[2];

        int cnt = 1;

        int _column = column;
        int _row = row;

        while (map[_row][_column] == 1){
            if (cnt > 3) {
                int[] returning = {-1, -1, -1};
                return returning;
            }
            if (direction % 4 == 0) {
                _column = column - 1;
                _row = row;
            } else if (direction % 4 == 1) {
                _column = column;
                _row = row - 1;
            } else if (direction % 4 == 2) {
                _column = column + 1;
                _row = row;
            } else {
                _column = column;
                _row = row + 1;
            }
            direction += 3;
            cnt++;
        }
        int[] returning = {_row, _column, direction};
        return returning;

    }

    static int game(int[] range, int[] position, int[][] map) {
        int answer = 0;
        while (position[0] != -1) {
            position = turn(map, position);
            if (position[0] == -1) {
                break;
            }
            map[position[0]][position[1]] = 1;
            answer++;
        }
        return answer;
    }
}
