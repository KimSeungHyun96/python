
import java.util.Scanner;

public class Pattern {
	public static void main(String[] args) {
		SaveBox2 saveBox2 = new SaveBox2();
		for (int i = 0; i < 9999999; i++) {
			System.out.println("원하시는 메뉴를 선택해주세요.");
			System.out.println("1 : 돈 입금");
			System.out.println("2 : 돈 입금 + 메세지 입력");
			System.out.println("종료를 원하시면 crash를 입력하세요.");
			
			Scanner s = new Scanner(System.in);
			String userInputString = s.nextLine();

			if (userInputString.equals("1")) {
				saveBox2.deposit();
			} else if (userInputString.equals("2")) {
				saveBox2.deposit2();
			} else if (userInputString.equals("crash")) {
				saveBox2.crash();
				break;
			}
		}
	}
}