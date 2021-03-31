import java.util.Arrays;

public class Array {
	public static void main(String[] args) {
		int a[] = {0, 0, 0, 0};
	//	int b[] = new int[5];
	
		a[0] = 10;
		a[0]++;
	
		a[1] = 3;
		a[1] = a[0] + a[1];
	
		a[3] = 50;
		
		for(int i = 0; i < a.length; i++) {
			System.out.println(a[i]);
		}
		System.out.println(Arrays.toString(a));
		
	//  , 사용시 여러개 선언가능
	//	int a = 0, b = 0, c = 0, d = 0;
	}
}
