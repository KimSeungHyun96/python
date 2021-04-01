import java.util.Random;

public class ExecClass {
	public static void main(String[] args) {
		Random r1 = new Random();
		int randNum = r1.nextInt(); // 0 ~ 99
		randNum = randNum % 100;
		// 1 => 1, 2 => 2 ..... 99 => 99, 100 => 0, 101 => 1 / 순환값 제어
		
		System.out.println("랜덤하게 생성된 숫자 : " + randNum);
		
	/*	if (randNum % 2 == 0) {
			System.out.println("짝수");
		}
		if (randNum % 2 == 1) {
			System.out.println("홀수");
		} 
	*/		
		if (randNum % 2 == 0 && randNum > 0) {  // randNum을 2로 나눌때 나머지가 0이면서 0보다 클때)
			System.out.println("짝수");          
		}
		if (randNum % 2 == 1 && randNum > 0) {
			System.out.println("홀수");
		}
		if (randNum == 0) {
			System.out.println("0");
		}
		if (randNum < 0) {
			System.out.println("음수");
		}
	/*	if (randNum % 2 == 0 && randNum > 0) {
			System.out.println("짝수");  
		} else if (randNum > 0) {
			System.out.println("홀수");
		} else if (randNum < 0) {
			System.out.println("음수");
		} else {
			System.out.println("0");
		} */
	}
}
