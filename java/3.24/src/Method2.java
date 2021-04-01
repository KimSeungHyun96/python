import java.util.Arrays;
import java.util.Random;

public class Method2 {
	public static void main(String[] args) {
		int[] score = new int[10];
		
		insertNumber(score); // score에 점수를 넣어줘
		System.out.println(Arrays.toString(score)); // 확인
		calcScore(score);// score의 총합을 구해줘
		
		
//		 재활용 가능	
//		int[] score2 = new int[20];
//		insertNumber(score2);
//		System.out.println(Arrays.toString(score2));
	}
	
	public static void insertNumber(int[] s) {
		Random r = new Random();
		for (int i = 0; i < s.length; i++)
			s[i] = r.nextInt(101);
		}
	
	public static void calcScore(int[] s) {
		int total = 0;
		for (int i = 0; i < s.length; i++) {
			total = total + s[i];
		}
		System.out.println("총합 : " + total);
	}
	}

//return 사용
//public static void insertNumber(int[] s) {
//	Random r = new Random();
//	for (int i = 0; i < s.length; i++)
//		s[i] = r.nextInt(101);
//	}
//	System.out.println(Arrays.toString(s));
//	return s;

// return 사용
//	int calcScore(score);
//	System.out.println("총합 : " + total);
//
//public static int calcScore(int[] s) {
//	int total = 0;
//	for (int i = 0; i < s.length; i++) {
//		total = total + s[i];
//	}
////	System.out.println("총합 : " + total);
//	return total;