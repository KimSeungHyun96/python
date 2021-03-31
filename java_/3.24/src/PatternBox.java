import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Pattern;

public class PatternBox {
	int coins = 0;
	public void deposit() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("입금하실 금액를 입력해주세요.");
		String userInputString = scanner.nextLine();
		// 정규표현식
		if (Pattern.matches("^[0-9]{1,}$", userInputString)) {
			int coin = Integer.parseInt(userInputString);
			System.out.println("딸그랑");
			coins = coins + coin;
		} else {
			System.out.println("금액 입력이 잘못 되었습니다.");
		}
	}
	public void deposit2() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("금액, 메세지를 입력해주세요.");
		String message = scanner.nextLine();
		// 문자열 분리
		String[] splited = message.split(",");
		
		int coin = Integer.parseInt(splited[0]);
		coins = coins + coin;
		message = splited[1].trim();
		
		//System.out.println("입금하실 금액를 입력해주세요.");
		//String userInputString = scanner.nextLine();		
		//int coin = Integer.parseInt(userInputString);
		//coins = coins + coin;
		
		System.out.println("" + coin + " (" + message + ")");
	}
	public void crash() {
		System.out.println("전체 금액 : " + coins);
	}
}
