import java.util.Scanner;

public class practice_01 {
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		System.out.println("3, 5");
		
		int a = s.nextInt();
		int b = s.nextInt();
		
		System.out.println(a+b);
		System.out.println(a-b); 
		System.out.println(a*b); 
		System.out.println(a/b); 
		System.out.println(a%b); 
		
	   /* int plus = 3 + 5;
	    int minus = 3 - 5;
	    int multi = 3 * 5;
	    double divide = (double)3 / 5;
	    int number3 = 3 % 5; */
	}
}