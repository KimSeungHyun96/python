import java.net.MulticastSocket;

public class RunClass {
	public static void main(String[] args) {
		int a; // 정수 
		a = 10;
		
		
		double c = 3.14; //실수 or 작은공간float
		char d = 'A'; // 문자(한글자), 작은따옴표 사용(오직 여기서만)
		boolean e = true; // 참/거짓 true/false
		//boolean e = 5 > 3;
		String f = "Hello"; // 문자열 큰따옴표사
		//String g = new String("Hello");
		
		
		int b = a + 3;
		double result = (double)a/ 3;
		//double result = (int)10.3/ 3;
		System.out.println(result);
		
		//System.out.println(d);
		//d = (char) (d + 1);
		//System.out.println(d);
		
		String printString = "안녕하세요.\n\"자바\"프로그래밍 수업입니다.";
		System.out.println(printString);
	}
}