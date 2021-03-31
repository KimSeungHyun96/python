import java.util.Scanner;

public class trapazoidMethod {

	public int height = 0;
	public int base = 0;
	public int topbase = 0;
	
	// 입력값 메소드
	public void inValue() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("사다리꼴의 높이를 입력하세요: ");
		String height = scanner.nextLine();
		this.height = Integer.parseInt(height);

		System.out.println("사다리꼴의 밑변을 입력하세요: ");
		String base = scanner.nextLine();
		this.base = Integer.parseInt(base);
		
		System.out.println("사다리꼴의 윗변을 입력하세요: ");
		String topbase = scanner.nextLine();
		this.topbase = Integer.parseInt(topbase);

	}

	
	// 연산 및 결과값 메소드
	public void outValue() {
		double trapaz = (double) (height * (base + topbase)) / 2;
		System.out.println("사다리꼴의 넓이는: " + trapaz);

	}
}
