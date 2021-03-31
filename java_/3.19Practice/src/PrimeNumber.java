
public class PrimeNumber {
	public static void main(String[] args) {
		
	for (int j = 0; j < 100; j++) {
		int num = j + 1;
		if (num < 2) {
			continue;
		}
		
		// 전체를 for부문에 추가
		boolean isPrime = true;
		for (int i = 0; i < num; i++) {
			if (i < 2) {
				continue;
			}
			if (num % i == 0) {
				isPrime = false;
				break;
			}
			
		}
		if (isPrime) {
			System.out.println("" + num + "  is Prime");
//		} else { 
//			System.out.println("" + num + "  is not Prime");
//			
		}
	}
}
}