
public class SaveBox1 {
	int coins = 0; // 돈이 쌓이는 곳
	public void deposit(int coin) {  // 돈을 넣는다
		coins = coins + coin;
	}
	public void withdraw() {  // 모든 돈을 찾는다 
		System.out.println("모든 돈 : " + coins);
	}
}
