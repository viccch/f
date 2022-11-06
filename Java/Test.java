
/*
 * JDK 10 or above required
 */

import java.util.Scanner;

public class Test {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int in1 = sc.nextInt();
        double dou1 = sc.nextDouble();
        boolean bool1 = sc.nextBoolean();
        String str1 = sc.next();
        sc.nextLine();// 清除上次输入仍遗留在缓冲中的行结束符。
        // 即清除了输入的回车。如果去掉，在敲入回车后，str3捕捉到了空行，程序结束。
        String str3 = sc.nextLine();
        System.out.println(in1 + " " + dou1 + " " + bool1 + " " + str1);
        System.out.println(str3);
        sc.close();
        /*
         * 123 45.67 true scannerTest
         * str3 test
         */
    }

}