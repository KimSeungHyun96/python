import java.util.Random;
import java.util.Scanner;

public class ExecClass {
	public static void main(String[] args) {
		System.out.println("숫자를 입력해주세요.");
		
		Scanner s1 = new Scanner(System.in);
		int userNumber = s1.nextInt();
		
		Random r1 = new Random();
		int randNumber = r1.nextInt(100) + 1;
		
		System.out.println("사용자가 입력한 숫자 : " + randNumber + ", 랜덤 생선된 숫자 : " + randNumber);
// 3 + 4   <-  7
// "" + 3 + 4  <- 34
		int resultNum = userNumber + randNumber;
		System.out.println("" + userNumber + " + " + randNumber + " = " + resultNum);
		
		resultNum = userNumber - randNumber;
		System.out.println("" + userNumber + " - " + randNumber + " = " + resultNum);
		
		resultNum = userNumber * randNumber;
		System.out.println("" + userNumber + " * " + randNumber + " = " + resultNum);
		
		double resultNum2 = userNumber / (double)randNumber;
		resultNum2 = Math.round(resultNum2); // 반올림(round) 
		// resultNum2 = Math.round(resultNum2 + 100) / (double)100; 0.00자리까지
		System.out.println("" + userNumber + " / " + randNumber + " = " + resultNum2);
		
		resultNum = userNumber % randNumber;
		System.out.println("" + userNumber + " % " + randNumber + " = " + resultNum);
		
		userNumber++;
		userNumber--;
		resultNum = 1 + 3 * (4 - 2) /4;
	}
}
