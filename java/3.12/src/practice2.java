import java.util.Random;
import java.util.Scanner;

public class practice2 {
	public static void main(String[] args) {
		System.out.print("가위바위보");
		System.out.print(" 1 : 가위");
		System.out.print(" 2 : 바위");
		System.out.print(" 3 : 보");
		
		Scanner s = new Scanner(System.in);
		int User = s.nextInt();
		System.out.print("1~3 숫자를 입력하세요 : ");
		
		if (User == 1) {
			System.out.println("媛��쐞");
		} else if (User == 2) {
			System.out.println("諛붿쐞");
		} else if (User == 3) {
			System.out.println("蹂�");
		}
		
	    Random r = new Random();
		int Com = r.nextInt(3) + 1; 
		System.out.print("而댄벂�꽣 : ");
		
		if (Com == 1) {
			System.out.println("媛��쐞");
		} else if (Com == 2) {
			System.out.println("諛붿쐞");
		} else if (Com == 3) {
			System.out.println("蹂�");
		}

		if (User == Com) {
			System.out.println("鍮꾧꼈�뒿�땲�떎.");			
		} else if (User == 1 && Com == 2) {
			System.out.println("Com �듅由�");
		} else if (User == 1 && Com == 3) {
			System.out.println("User �듅由�");
		} else if (User == 2 && Com == 3) {
			System.out.println("Com �듅由�");
		} else if (User == 2 && Com == 1) {
			System.out.println("User �듅由�");
		} else if (User == 3 && Com == 1) {
			System.out.println("Com �듅由�");
		} else if (User == 3 && Com == 2) {
			System.out.println("User �듅由�");
		}
	}
}