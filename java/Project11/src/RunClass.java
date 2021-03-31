
public class RunClass {
	public static void main(String[] args) {
		int a = 4;
		boolean r1 = 4 == 4;
		System.out.println(r1);
		
		r1 = a > 0;
		System.out.println(r1);

		r1 = a <= 10;
		System.out.println(r1);
		
		r1 = a != 2; // <>
		System.out.println(r1);
		
		r1 = a > 10 && a == 20; // false && false    AND 연산자 (모두 조건만족)
		System.out.println(r1);
		
		r1 = a < 10 && a % 4 == 0; // true && true
		System.out.println(r1);
		
		r1 = a == 10 || a < 10; // false || true     OR 연산자 (둘중 하나 만족)
		System.out.println(r1);
		
		r1 = true && true;
		System.out.println(r1);
		
		r1 = true || false;
		System.out.println(r1);
		
		r1 = !false; // !(a < 10) 반전 (같지 않으면/ a가 10보다 크거나 같으면)
		System.out.println(r1);
	}
}
