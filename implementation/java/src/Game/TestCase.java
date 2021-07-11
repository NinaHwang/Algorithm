package Game;


public class TestCase {
    public static void main(String[] args) {
        int[] range = {4,4};
        int[] position = {1,1,0};
        int[][] map = {{1,1,1,1},{1,0,0,1},{1,1,0,1},{1,1,1,1}};

        int case1 = Solution.game(range, position, map);

        System.out.println(case1);
    }
}
