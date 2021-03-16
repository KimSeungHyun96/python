
public class Method2 {
	public static void numbering(int limit) { // limit라는 변수만 받음 
											  // parameter (매개변수)
	// 메소드 입력
		int i = 0; // 5
		while (i < limit) {
			System.out.println(i);
			i++;
		}
	}
	public static void main(String[] args) {
		numbering(5); // limit라는 변수안에 5가들어감 argument(인자)
	}
} 

/* =========================2번째 방법======================================
public class Method2 {
	public static void numbering() { // limit라는 변수만 받는다.
		int limit = 5;
		int i = 0; // 5
		while (i < limit) {
			System.out.println(i);
			i++;
		}
	}
	public static void main(String[] args) {
		numbering();
	}
}
==========================================================================
public class Method2 {
	public static void numbering(int init, int limit) {
		int i = init;
		while (i < limit) {
			System.out.println(i);
			i++;
		}
	}
	public static void main(String[] args) {
		numbering(3, 5);
	}
}
========================================================================*/

