import java.util.Random;
import java.util.Scanner;

public class GawiBawiBo {
	public static void main(String[] args) {
		System.out.println("가위바위보 중 하나를 입력해주세요");
		System.out.println(" 1 : 가위");
		System.out.println(" 2 : 바위");
		System.out.println(" 3 : 보");
	
		Scanner s = new Scanner(System.in);
		int User = s.nextInt();
	
		/*	if (userNum < || userNum > 3); {
		System.out.println("1~3의 숫자를 입력하세요.");
		} */
		
		if (User == 1) {
			System.out.println("사용자는 가위를 냈습니다.");
		} else if (User == 2) {
			System.out.println("사용자는 바위를 냈습니다.");
		} else if (User == 3) {
			System.out.println("사용자는 보를 냈습니다.");
		}
		
		 Random r = new Random();
		int Com = r.nextInt(3) + 1; 
		
		if (Com == 1) {
			System.out.println("컴퓨터는 가위를 냈습니다.");
		} else if (Com == 2) {
			System.out.println("컴퓨터는 바위를 냈습니다.");
		} else if (Com == 3) {
			System.out.println("컴퓨터는 보를 냈습니다.");
		}
		
		if (User == Com) {
			System.out.println("비겼습니다.");			
		} else if (User == 1 && Com == 2) {
			System.out.println("컴퓨터 승리");
		} else if (User == 1 && Com == 3) {
			System.out.println("사용자 승리");
		} else if (User == 2 && Com == 3) {
			System.out.println("컴퓨터 승리");
		} else if (User == 2 && Com == 1) {
			System.out.println("사용자 승리");
		} else if (User == 3 && Com == 1) {
			System.out.println("컴퓨터 승리");
		} else if (User == 3 && Com == 2) {
			System.out.println("사용자 승리");
		}
	}
}
