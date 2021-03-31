
public class JavaPractice1 {
	public static void main(String[] args) {
		int totalSum = 0;
		int oddSum = 0;
		int evenSum = 0;
		
		for(int i = 0; i < 100; i++) {
			totalSum = totalSum + (i + 1);
		}
		
		System.out.println("1부터 100까지의 숫자의 합은 " + totalSum + " 입니다.\n");
		
		
		for(int i = 0; i < 100; i++) {
			if ((i + 1) % 2 != 0) {
				oddSum = oddSum + (i + 1);
			}
		}
		
		System.out.println("1부터 100까지의 홀수의 합은 " + oddSum + " 입니다.\n");
		
		for(int i = 0; i < 100; i++) {
			if ((i + 1) % 2 == 0) {
				evenSum = evenSum + (i + 1);
			}
		}
		
		System.out.println("1부터 100까지의 짝수의 합은 " + evenSum + " 입니다.\n");
	}
}

//int total = 0;
//int evenTotal = 0;
//int oddTotal = 0;
//for (int i = 0; i < 100; i++) {
//	int number = i + 1;
//	
//	total = total + number; 
//	
//	if (number % 2 == 0) {
//		evenTotal = evenTotal + number;
//	} else {
//		oddTotal = oddTotal + number;
//	}
//}
//System.out.println(total);
//System.out.println(evenTotal);
//System.out.println(oddTotal);