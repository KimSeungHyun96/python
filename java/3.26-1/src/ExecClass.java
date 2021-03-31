
public class ExecClass {
	public static void main(String[] args) {
		Kaup kaup = new Kaup();
		
		double weight = kaup.userInputWeight();
		double height = kaup.userInputHeight();
		kaup.calcKaup(weight, height);
	}
}
