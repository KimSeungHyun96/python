import java.util.Arrays;
import java.util.Scanner;

public class Array3 {
	public static void main(String[] args) {
	Scanner s = new Scanner(System.in);
	System.out.println("숫자를 9개 입력하겠습니다.\n");
	// 사용자에게 9개의 숫자를 입력 받아서 3x3 이중 배열에 넣은 후 각 행의 덧셈 합을 출력하시오.
	// 조건 1) 출력시 4x4의 형식으로 출력 (4행째는 덧셈 합)
    // 조건 2) 데이터는 정렬된 형식으로 출력
	
	// 비고. 이중배열 사용법 int[][] arr = new int[4][4]
	// 비고. 데이터를 정렬된 형식으로 출력하는 방법을 찾아보시오.
			
	int arr[][] = new int[3][3];

	for (int i = 0; i < arr.length; i++) {	
		for (int j = 0; j < arr.length; j++) {
			System.out.print((i * 3 + j + 1) + "번째 숫자를 입력해주세요.   ");
			arr[i][j] = s.nextInt();
		}
		Arrays.sort(arr[i]);
		System.out.println("");
		}
	
//	int arr[][] = new int[4][4]; 
	
	for (int i = 0; i < arr.length; i++) {
		for (int j = 0; j < arr[i].length; j++) {
			if (i < 3 && j < 3) {
				arr[i][j] = arr[i][j];					
			} else if (j == 3) {
				arr[i][j] = Arrays.stream(arr[i]).sum();
			} else {
				arr[i][j] = arr[0][j] + arr[1][j] + arr[2][j];
			} 
		}
	}
	
	for (int i = 0; i < arr.length; i++) {
		System.out.println(Arrays.toString(arr[i]));
	}

	}
}





