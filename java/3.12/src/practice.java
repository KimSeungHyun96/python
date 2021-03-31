import java.util.Random;

public class practice {
	public static void main(String[] args) {
		Random r2 = new Random();
		int randNum = r2.nextInt(101);
		
	/*	int grade = 65;
		Random r1 = new Random();
		int randNum = r1.nextInt(); */
		
		if(randNum >= 90) {
			System.out.println("당신의 학점은 A");
		} else if(randNum >= 80) {
			System.out.println("당신의 학점은 B");
		} else if(randNum >= 70) {
			System.out.println("당신의 학점은 C");
		} else if(randNum >= 60) {
			System.out.println("당신의 학점은 D");
		} else if(randNum >= 50) {
			System.out.println("당신의 학점은 E");
		}	
	/*	switch(randNum) {  // 안에들어간 변수가 1~5인 경우 출력
		case 1:
			System.out.println("당신의 학점은 A");
			break;
		case 2:
			System.out.println("당신의 학점은 B");
			break;
		case 3:
			System.out.println("당신의 학점은 C");
			break;
		case 4:
			System.out.println("당신의 학점은 D");
			break;
		case 5:
			System.out.println("당신의 학점은 E");
			break;
		} */
	}
}
