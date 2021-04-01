import java.util.Scanner;
public class triangleMethod {

	public int height = 0;
	public int base = 0;


	
	// 입력값 메소드
	public void inValue () {
		Scanner scanner = new Scanner(System.in);
		System.out.println("삼각형의 높이를 입력하세요: ");
		String height = scanner.nextLine();
		this.height = Integer.parseInt(height);
		
		System.out.println("삼각형 밑변을 입력하세요: ");
		String base = scanner.nextLine();
		this.base = Integer.parseInt(base);
		
	}

	
	// 연산 및 결과값 메소드
	public void outValue () {
		double triangle = (double) height * base / 2; 
		System.out.println("삼각형의 넓이는: " + triangle);
		
	}
	}

