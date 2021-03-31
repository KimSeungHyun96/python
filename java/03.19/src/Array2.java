import java.util.Arrays;

public class Array2 {
	public static void main(String[] args) {
		
	//  call by value	(값만 가져옴 a, b는 서로 다른 창고)
		
		int a = 3;
		int b = a;
		
		System.out.println(b);
		
		b = 10;
		System.out.println(a);
		
	//  call by reference  (창고에 대한 주소값만 가져옴)
		
		int arr1[] = {1, 2, 3, 4, 5};
		int arr2[] = arr1; // arr1을 참조 / 사용X 다른효과생김
		System.out.println(arr1); // 주소값만 나옴 [I@4361bd48
		
		System.out.println(arr2[2]);
		arr2[2] = 10;
		
		System.out.println(arr1[2]);
		int b1 = arr1[4];
		b1 = 10;
		System.out.println(b1);
		
	//  *** 배열을 복사하고 싶을 때 ***(외워야 할 것)
		
		int arr3[] = {1, 2, 3, 4, 5};
		int arr4[] = new int[arr3.length];
		System.arraycopy(arr3, 0, arr4, 0, arr3.length);
		// arraycopy 복사하고 싶은 순서 0 : 붙여넣기
		arr3[1] = 10;
		arr4[1] = 20;
		
		System.out.println(Arrays.toString(arr3));
		System.out.println(Arrays.toString(arr4));
	}
}
	