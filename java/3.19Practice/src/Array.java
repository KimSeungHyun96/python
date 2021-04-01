import java.util.Random;
import java.util.Arrays;

public class Array {
	public static void main(String[] args) {
		
		Random s = new Random();
		int arr[] = new int[10];
		
		for(int i = 0; i < arr.length; i++ ) {
			System.out.println();
			int num = s.nextInt(30) + 1;
			arr[i] = num;
		}	
		System.out.println(Arrays.toString(arr));
		
		int total = 0;
		for(int i = 0; i < arr.length; i++ ) {
			total = total + arr[i];
		}
		System.out.println("총점 : " + total);
		
		double avg = (double)total / arr.length;
		avg = (double)Math.round(avg * 100) / 100;
		
		System.out.println("평균 : " + avg);
			
			
		}
	}

//int arr[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
//Random s = new Random();
//for(int i = 0; i < arr.length; i++ ) {
//	 num = s.nextInt(30) + 1;
//}
//System.out.println(Arrays.toString(arr));
