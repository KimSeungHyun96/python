import java.util.Random;
import java.util.Scanner;

public class Hello {
	public static void main(String[] args) {
		
		int Num = 0;
		
		Scanner s = new Scanner(System.in);
		System.out.print("사용자 숫자 : ");
		Num = s.nextInt();
		
		int randNum = 0; 
		
		Random r = new Random();
		randNum = r.nextInt(20)+1;
		System.out.println("랜덤 숫자 : " + randNum);
		
		int plus = Num + randNum; 
		int minus = Num - randNum;
		int multi = Num * randNum;
		double division = (double)Num / randNum;
		int mod = Num % randNum;
		
		System.out.println("덧셈 결과 :" + plus);
		System.out.println("뺄셈 결과 :" + minus);
		System.out.println("곱셈 결과 :" + multi);
		System.out.println("나누기 결과 :" + division);
		System.out.println("나머지 결과 :" + mod);
	}
}
