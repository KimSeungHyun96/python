
public class ExecClass {
	public static void main(String[] args) {
		Student s1 = new Student();
		//s1.setName("홍길동");
		s1.name = "홍길동";
		//s1.setKorScore(100);
		s1.korScore = 100;
		s1.setEngScore(100);
		s1.setMathScore(100);
		System.out.println(s1.name + " : " + s1.korScore);
		
		Student s2 = new Student();
		s2.setName("둘리");
		s2.setKorScore(50);
		s2.setEngScore(10);
		s2.setMathScore(90);
		System.out.println(s2.name + " : " + s2.korScore);
		
//		int s1_korScore = 100;
//		int s1_engScore = 100;
		//s2_korScore = 30;
	}
}
