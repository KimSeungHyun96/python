import java.util.Random;
import java.util.Scanner;

public class practice2 {
	public static void main(String[] args) {
		System.out.print("가위바위보 중 하나를 입력하세요");
		System.out.print(" 1 : 가위");
		System.out.print(" 2 : 바위");
		System.out.print(" 3 : 보");
		
		Scanner s = new Scanner(System.in);
		int User = s.nextInt();
		System.out.print("사용자 : ");
		
		if (User == 1) {
			System.out.println("가위");
		} else if (User == 2) {
			System.out.println("바위");
		} else if (User == 3) {
			System.out.println("보");
		}
		
	    Random r = new Random();
		int Com = r.nextInt(3) + 1; 
		System.out.print("컴퓨터 : ");
		
		if (Com == 1) {
			System.out.println("가위");
		} else if (Com == 2) {
			System.out.println("바위");
		} else if (Com == 3) {
			System.out.println("보");
		}

		if (User == Com) {
			System.out.println("비겼습니다.");			
		} else if (User == 1 && Com == 2) {
			System.out.println("Com 승리");
		} else if (User == 1 && Com == 3) {
			System.out.println("User 승리");
		} else if (User == 2 && Com == 3) {
			System.out.println("Com 승리");
		} else if (User == 2 && Com == 1) {
			System.out.println("User 승리");
		} else if (User == 3 && Com == 1) {
			System.out.println("Com 승리");
		} else if (User == 3 && Com == 2) {
			System.out.println("User 승리");
		}
	}
}