//
//  저금통 프로그램을 만드시오. 
//	조건1. 입금하는 방식은 돈만 넣는 방법, 돈과 메시지를 넣는 방법의 2가지이다. (o)
//	조건2. 돈만 넣었을 경우 ‘딸그랑’이라는 메시지와 입금 액수 출력 ()
//  조건3. 메시지와 같이 넣으면 메시지와 입금 액수 출력 ()
//  조건4. ‘crash’를 입력하면 총 액수 출력과 함께 프로그램 종료 (o)

import java.util.Scanner;

public class ExecClass1 {
	public static void main(String[] args) {
		SaveBox2 box = new SaveBox2();
		
		for (int i = 0; i < 9999999; i++) {
		System.out.println("원하시는 메뉴를 선택해주세요.");
		System.out.println("1 : 돈 입금");
		System.out.println("2 : 돈 입금 + 메세지 입력");
		System.out.println("종료를 원하시면 crash를 입력하세요.");
		
		Scanner s = new Scanner(System.in);
		String userInputString = s.nextLine(); 
		
		if (userInputString.equals("crash")) {
			box.result();
			break;
		} 
		int converNumber = Integer.parseInt(userInputString);
		if (converNumber == 1) {
			Scanner s1 = new Scanner(System.in);
			System.out.println("입금액 : ");
			int coin = s1.nextInt();
			box.deposit(coin);	
		}	else if(converNumber == 2) {
			Scanner s1 = new Scanner(System.in);
			System.out.println("입금자 : ");
			String userInputString1 = s1.nextLine();
			System.out.println("입금액 : ");
			int coin = s1.nextInt();
			box.message(coin, userInputString1);
		}
	}
}
}