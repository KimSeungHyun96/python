import java.util.Random;
import java.util.Scanner;

public class Random_02 {
	public static void main(String[] args) {
		System.out.println("숫자를 입력해주세요 : ");
		
		Scanner s1 = new Scanner(System.in);
		int userNumber = s1.nextInt();
		
		Random r1 = new Random();
		int randNumber = r1.nextInt(20) + 1;
		
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
		System.out.println("" + userNumber + " / " + randNumber + " = " + resultNum2);
		
		resultNum = userNumber % randNumber;
		System.out.println("" + userNumber + " % " + randNumber + " = " + resultNum);
	}
}