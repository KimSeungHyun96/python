
public class SaveBox2 {
	
	int coins = 0; 
	
	public void deposit(int coin) { 
		System.out.println(" 딸그랑 "+ " " + coin + "원 ");
		coins = coins + coin;
	}
	public void result() {
		System.out.println("잔액 : " + coins);
	}
	public void message(int coin, String userInputString) {
		System.out.println("딸그랑 " + coin + " 금액이 " + userInputString + "으로 입금되었습니다.");
		coins = coins + coin;
	}
}
