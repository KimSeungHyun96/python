import java.util.Scanner;

public class SaveBox2 {
	int coins = 0;
	public void deposit() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("입금하실 금액를 입력해주세요.");
		String userInputString = scanner.nextLine();
//		try { 예외처리
		int coin = Integer.parseInt(userInputString);
			System.out.println("딸그랑");
			coins = coins + coin;
//			} catch (Exception e) {
//	}
	}
	public void deposit2() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("메세지를 입력해주세요.");
		String message = scanner.nextLine();
		
		System.out.println("입금하실 금액를 입력해주세요.");
		String userInputString = scanner.nextLine();		
		int coin = Integer.parseInt(userInputString);
		coins = coins + coin;
		
		System.out.println("" + coin + " (" + message + ")");
	}
	public void crash() {
		System.out.println("전체 금액 : " + coins);
	}
}
