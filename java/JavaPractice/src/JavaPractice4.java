import java.util.Arrays;
import java.util.Random;

//0~100까지 임의의 수를 30개 발생시켜서 배열에 넣은 후 정렬하시오.
//1) 정렬 전/후의 값을 화면에 출력조건
//2) 소트 알고리즘 중 사용한 알고리즘을 설명한 레포트 (형식 무관,내용만 제출)첨부비고.
//정렬 알고리즘 및 이중 루프문에 대한 공부는 따로 하셔야 합니다.(서로간의 정보 교환 가능)
//2중 for문을 사용하는 소트로 구성 - 검색 후 적용 (버블소트, 셀렉션소트ㅡ쉬움) / Array.sort 사용x

// bubble sort 사용
public class JavaPractice4 {
	public static void main(String[] args) {
	
		Random s = new Random();
		//  arr[]에 30개의 배열 생성
		int arr[] = new int[30];
		
		// for문을 통해 i를 초기화 arr.length의 반복조건으로 i를 1씩 추가
		for(int i = 0; i < arr.length; i++ ) {
			int num = s.nextInt(101);
			// num에 임시변수 생성
			arr[i] = num;
	         for(int j=0; j<i; j++) {
	        	 if (arr[i]==arr[j]) {
	        		 i--;
	        	 }
	         }
		}	
		System.out.println("정렬 전 : " + Arrays.toString(arr));

		// 오름차순 정렬 (이중 for문)
		
		// 앞의 for문 i와 뒤의 for문 j를 만들어 비교
		for (int i = 0; i < arr.length; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				// [i]가 [j]보다 크다면 실행한다는 조건
				if (arr[i] > arr[j]) {	
					// 큰 값인 arr[i]를 arr1에 임시변수 생성
					int arr1 = arr[i];	
					// 작은 값인 arr[j]를 arr[i]에 덮어씌움
					arr[i] = arr[j];
					// 변수로 지정한 arr1을 arr[j]에 넣음 
					arr[j] = arr1;
				}
			}
		}
		System.out.println("정렬 후 : " + Arrays.toString(arr));
	}
}