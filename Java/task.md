# Java 作业

## 第二章
1、	用移位运算实现求2的x次方。
```java
    static int pow2(int i) {
        return 1<<i;
    }
```
2、	用按位与运算，取模运算、判断一个数是否为奇数。
```java
    static boolean is_odd(int x) {
        return (x & 2) == 1;
    }
```
```java
    static boolean is_odd(int x) {
        return (x % 2) == 1;
    }
```
3、	判断一个数是否是2的n 次幂  
```java
    static boolean ispow2(int x) {
        return (x & (x - 1)) == 0;
    }
```
## 第三章
查原理，编程序
1、	计算多项式1！+2！+3！…+n!，当多项式之和超过10000时停止，并输出累加之和以及n的值。
```java
    static void fun() {
        int sum = 0;
        int n = 1;
        for (;; n++) {
            sum += factorial(n);
            if (sum > 10_000)
                break;
        }
        System.out.println("sum="+sum);
        System.out.println("n="+n);
    }

    static int factorial(int i) {
        return i == 0 ? 1 : i * factorial(i - 1);
    }
```
2、	从标准输入端输入一个字符，判断字符是数字、还是西文字母还是其他的字符。
```java
    static void fun() {
        try {
            char x = (char) System.in.read();
            System.out.print(x);
            if (x >= 'a' && x <= 'z' || x >= 'A' && x <= 'Z') {
                System.out.println("是西文字母");
            } else if (x >= '0' && x <= '9') {
                System.out.println("是数字");
            } else
                System.out.println("是其它字符");
        } catch (IOException ioException) {
            System.out.println(ioException);
        }
    }
```
3、	利用辗转相除法（欧几里得算法）求两个正整数的最大公约数
```java
    static int gcd(int a,int b){
        return b==0?a:gcd(b,a%b);
    }
```
4、	假设一个数在1000到1100之间，那除以3结果余2,；除以5结果余3,；除以7结果余2（中国剩余定理），求此数。
```java
    static int num() {
        int n = 1000;
        for (; n <= 1100; n++)
            if (n % 3 == 2 && n % 5 == 3 && n % 7 == 2)
                break;
        return n;
    }
```
5、	小球从100米高度自由落下，每次触地后反弹到原来高度的一半，求第10次触地时经历的总路程以及第10次反弹高度。
```java
    static void fun() {
        int n = 1;// 反弹次数
        double u = 0.5;// 反弹率
        double h = 100;// 起始高度
        double total_distance = h;// 总路程
        for (int i = 1; i < n; i++) {
            h *=u;
            total_distance += 2 * h;
        }
        System.out.println("总路程："+total_distance);
        System.out.println("第"+n+"次反弹高度："+h / 2);
    }
```
6、	从键盘输入一个字符，用程序来判断这个字符是属于数字，西文字母还是其他字符。
```java
    static void fun() {
        try {
            char x = (char) System.in.read();
            System.out.print(x);
            if (x >= 'a' && x <= 'z' || x >= 'A' && x <= 'Z') {
                System.out.println("是西文字母");
            } else if (x >= '0' && x <= '9') {
                System.out.println("是数字");
            } else
                System.out.println("是其它字符");
        } catch (IOException ioException) {
            System.out.println(ioException);
        }
    }
```
