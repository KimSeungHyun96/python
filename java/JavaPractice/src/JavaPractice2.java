import java.util.Arrays;
import java.util.Scanner;

public class JavaPractice2 {
	public static void main(String[] args) {
		
// 사용자로부터 값 5개를 입력 받아 배열로 만들고 합 구하기.
Scanner s = new Scanner(System.in);

System.out.println("정수 5개를 입력하겠습니다.");

int[] arr2 = new int[5];	// 공간을 미리 만들어줘야한다.
int arrSum = 0;


for (int i = 0; i < arr2.length; i++) {
	int num = i+1;
	System.out.println((num) + "번째 숫자를 입력해주세요.");
	arr2[i] = s.nextInt();
	arrSum = arrSum + arr2[i];
}
System.out.println(""); // 문자열로 만들기
	System.out.println("입력한 숫자는 다음과 같습니다.");
	System.out.println(Arrays.toString(arr2));
	System.out.println("입력 받은 값 5개의 합은 " + arrSum + "입니다.");
	}
}
