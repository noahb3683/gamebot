import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class WranglerCensus {
    static char[] column = {'A','B','C','D','E','F','G','H'};
    static boolean[][] SquareStates = {
            {true, false, true, false, true, false, true, false},
            {false, true, false, true, false, true, false, true},
            {false, false, false, false, false, false, false, false},
            {false, false, false, false, false, false, false, false},
            {false, false, false, false, false, false, false, false},
            {false, false, false, false, false, false, false, false},
            {true, false, true, false, true, false, true, false},
            {false, true, false, true, false, true, false, true}
    };
    public static void main(String[] args) {
        for(int c=0; c<8; c++) {
            for(int r=0; r<8; r++) {
                System.out.println("Checking signal on square  " + column[c]+ (r + 1) + " -- Result: " + SquareStates[c][r]);
            }
        }
        final Map<Character, Integer> map;
        final String str = "hello world";

        map = new HashMap<>();
        // or map = new HashMap<Character, Integer> if you are using something before Java 7.
        map.put('a', 0);
        map.put('b', 1);
        map.put('c', 2);
        map.put('d', 3);
        map.put('e', 4);
        map.put('f', 5);
        map.put('g', 6);
        map.put('h', 7);
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int i = scan.nextInt();
        int k = map.get(s);
        System.out.println(SquareStates[k][i]);

    }

}
