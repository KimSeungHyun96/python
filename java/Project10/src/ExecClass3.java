
public class ExecClass3 {
	public static void main(String[] args) {
		int a =10;
		double b = a;
		int c = (int)b;
		
		int num1 = 10;
		int num2 = 2;
		double result = (double)num1 / num2;
		
		short s1 = 10;
		int s2 = s1;
		short s3 = (short)s2;
		
	    int plus = 10 + a;
	    int minus = 100 - c;
	    int multi = 3 * 2;
	    double divide = (double)10 / 3;
	    int number3 = 10 % 3;
	    
	    // 산술연산자
	    a++; // a = a + 1
	    c--; // c = c - 1
	    //++a; > int num3 = 3 * ++a / 3; 섞어쓰지말고 위의 2개 사용
	    //a =+ 3; 사용X /  a = a + 3;
	}
}
