//
//public class Exec0316_2 {
//	public static void main(String[] args) {
//		for (int i = 0; i < 9; i++) {
//			for (int j = 0; j < 9; j++) {
//				System.out.println("i : " + i + " j : " + j);
//			} 
//		}
		
		// i : 0  j : 0~9 / i : 1 j : 0~9
		
//		for (int i = 0; i < 9; i++) {
//			int number1 = i + 1;
//			System.out.println("\n" + number1 + "단");
//			for (int j = 0; j < 9; j++) {
//				int number2 = j + 1;
//				int resultNumber = number1 * number2;
//				System.out.println("" + number1 + " X " + number2 + " = " + resultNumber);
//			}                      // "" 문자열로 만들어줌
//		}
		
//		사용자로부터 숫자(정수)를 입력 받아서 그 숫자가 소수(prime number)인지 출력
//		1과 사용자 숫자까지 반복
//
//public class Exec0316_2 {
//	public static void main(String[] args) {
//		 int number = 0;
//
//         for(int i = 2; i <= 100; i++) {
//             for(int j = 2; j <= i; j++) {
//                  if(i%j == 0) {
//                	  number ++; }    
//             }
//             if(number == 1)
//             {
//                  System.out.print(i+" ");
//             }
//             number = 0;
//         }	
//	}
//}

import java.util.Scanner;

public class Exec0316_2 {
	public static void main(String[] args) {
		System.out.println("숫자(정수)를 입력해주세요.");
		
		Scanner s1 = new Scanner(System.in);
		int number = s1.nextInt();
		
		System.out.println("입력받은 숫자는 " + number + "입니다.");
		
		boolean isPrime = true;
		for (int i = 0; i < number; i++) {
			if (i < 2) {
				continue;
			}
			if (number % i == 0) {
				isPrime = false;
				break;
			}
		}
		if (isPrime) {
			System.out.println("소수입니다.");
		} else { 
			System.out.println("소수가 아닙니다.");
		}
	}
}

//		System.out.println("숫자(정수)를 입력해주세요.");
//		Scanner s1 = new Scanner(System.in);
//		int number = s1.nextInt();
//		
//		System.out.println("입력받은 숫자는 " + number + "입니다.");
//		
//		boolean isPrime = true;
//		for (int i =2; i < number; i++) {
//			if (i )
//		}
//		

		