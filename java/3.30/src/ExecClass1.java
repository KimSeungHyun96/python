
public class ExecClass1 {
	public static void main(String[] args) {
		Student1 s1 = new Student1();
		s1.name = "홍길동";
		s1.korScore = 100;
		s1.engScore = 100;
		s1.mathScore = 100;
		
		s1.printInfo();
		
		Student1 s2 = new Student1();
		s2.name = "둘리";
		s2.korScore = 50;
		s2.engScore = 10;
		s2.mathScore = 90;
		
		s2.printInfo();
	}
}
