import java.util.Scanner;

public class ExecClass {
	public static void main(String[] args) {
		System.out.println("화면에 숫자를 입력해주세요!");
		
		// 숫자입력
		int userInputNumber = 0;
		
		Scanner s = new Scanner(System.in);
		userInputNumber = s.nextInt();
	
		
		System.out.println("당신이 입력한 숫자는" + userInputNumber);
	}
}
