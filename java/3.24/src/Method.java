//import java.util.Random;
//
//public class Method {
//	public static void testMethod() {
//		Random r1 = new Random();
//		
//		int number1 = r1.nextInt(100);
//		int number2 = r1.nextInt(100);
//		
//		int resultNumber = number1 + number2;
//		System.out.println("" + number1 + " + " + number2 + " = " + resultNumber);
//	}
//	
//	public static void testMethod2() {
//		Random r2 = new Random();
//		
//		int number1 = r2.nextInt(100);
//		int number2 = r2.nextInt(100);
//		
//		int resultNumber = number1 - number2;
//		System.out.println("" + number1 + " - " + number2 + " = " + resultNumber);
//	}
//	
//	public static void main(String[] args) {
//		testMethod();
//		testMethod2();
//		}
//	}

//import java.util.Random;
//
//public class Method {
//	// static 삭제
//	public void testMethod() {
//		Random r1 = new Random();
//		
//		int number1 = r1.nextInt(100);
//		int number2 = r1.nextInt(100);
//		
//		int resultNumber = number1 + number2;
//		System.out.println("" + number1 + " + " + number2 + " = " + resultNumber);
//	}
//	public static void main(String[] args) {
//		Method a = new Method();
//		a.testMethod();
//		}
//	}

// 인자 파라미터 사용
//import java.util.Random;
//
//public class Method {
//	public static void testMethod(int n1, int n2) {
//		int resultNumber = n1 + n2;
//		System.out.println("" + n1 + " + " + n2 + " = " + resultNumber);
//	}
//	
//	public static void testMethod2(int number1, int number2) {
//		int resultNumber = number1 - number2;
//		System.out.println("" + number1 + " - " + number2 + " = " + resultNumber);
//	}
//	
//	public static void main(String[] args) {
//		Random r1 = new Random();
//		
//		int number1 = r1.nextInt(100);
//		int number2 = r1.nextInt(100);
//		
//		testMethod(number1, number2);
//		testMethod2(number1, number2);
//		}
//	}

import java.util.Random;

public class Method {
	public static int testMethod(int n1, int n2) {
		int resultNumber = n1 + n2;
		System.out.println("" + n1 + " + " + n2 + " = " + resultNumber);
		return resultNumber;
	}
	
	public static void testMethod2(int number1, int number2) {
		int resultNumber = number1 - number2;
		System.out.println("" + number1 + " - " + number2 + " = " + resultNumber);
	}
	
	public static void main(String[] args) {
		Random r1 = new Random();
		
		int number1 = r1.nextInt(100);
		int number2 = r1.nextInt(100);
		
		int result = testMethod(number1, number2);
		testMethod2(number1, number2);
		}
	}