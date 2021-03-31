import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class aa1 {
	public static void main(String[] args) {

		Random r = new Random();
		int arr[] = new int[30];
		
		for(int i = 0; i < arr.length; i++ ) {
			int num = r.nextInt(101);
			arr[i] = num;
	         for(int j=0; j<i; j++) {
	        	 if (arr[i]==arr[j]) {
	        		 i--;
	        	 }
	         }
		}	
		System.out.println("정렬 전 : " + Arrays.toString(arr));

		for (int i = 0; i < arr.length; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[i] > arr[j]) {	
					int arr1 = arr[i];	
					arr[i] = arr[j]; 
					arr[j] = arr1;
				}
			}
		}
		System.out.println("정렬 후 : " + Arrays.toString(arr));
	}
}