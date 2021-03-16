import java.util.Random;

public class ExecClass2 {
	public static void main(String[] args) {
		Random r1 = new Random();
		int randNum = r1.nextInt(5) + 1;
		
		if (randNum == 1) {
			System.out.println("★☆☆☆☆");
		} else if (randNum == 2) {
			System.out.println("★★☆☆☆");
		} else if (randNum == 3) {
			System.out.println("★★★☆☆");
		} else if (randNum == 4) {
			System.out.println("★★★★☆");
		} else if (randNum == 5) {
			System.out.println("★★★★★");
		}
		
		switch(randNum) {  // 안에들어간 변수가 1~5인 경우 출력
		case 1:
			System.out.println("★☆☆☆☆");
			break;
		case 2:
			System.out.println("★★☆☆☆");
			break;
		case 3:
			System.out.println("★★★☆☆");
			break;
		case 4:
			System.out.println("★★★★☆");
			break;
		case 5:
			System.out.println("★★★★★");
			break;
			
		}
	}
}
