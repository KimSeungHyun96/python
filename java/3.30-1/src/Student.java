
public class Student {
	public String name;
	public int korScore = 0;
	public int engScore = 0;
	public int mathScore = 0;
	public int totalScore = 0;

	Student(String name, int korScore, int engScore, int mathScore) {
		this.name = name;
		this.korScore = korScore;
		this.engScore = engScore;
		this.mathScore = mathScore;
		this.totalScore = korScore + engScore + mathScore;
	}
	
	public void printInfo() {
		System.out.println(this.name + " : " 
	      + "국어 " + this.korScore + ", "
	      + "영어 " + this.engScore + ", "
	      + "수학 " + this.mathScore + ", "
	      + "총점 " + this.totalScore
	    );
	}
}
