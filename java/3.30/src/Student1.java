
public class Student1 {
	public String name;
	public int korScore = 0;
	public int engScore = 0;
	public int mathScore = 0;

	public void printInfo() {
		System.out.println(this.name + " : " 
	      + "국어 " + this.korScore + ", "
	      + "영어 " + this.engScore + ", "
	      + "수학 " + this.mathScore
	    );
	}
}
