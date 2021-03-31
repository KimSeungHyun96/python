import java.util.Arrays;
import java.util.Random;

public class Array3 {
	public static void main(String[] args) {
		double number[] = new double[10];
	//	double number[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
		
		Random r1 = new Random();
		for (int i = 0; i < number.length; i++) {
			number[i] = r1.nextInt();
		}
		
		System.out.println(Arrays.toString(number));
		
		Arrays.sort(number);
		System.out.println(Arrays.toString(number));
		
	}
}
