
public class ShapeMain {
	public static void main(String[] args) {
		
		// 삼각형넓이 구하는 클래스 //임시진
		triangleMethod triangle = new triangleMethod();

		triangle.inValue();
		triangle.outValue();
		

		// 사각형넓이 구하는 클래스 //백두용
		squareMethod square = new squareMethod();

		square.inValue();
		square.outValue();

		// 사다리꼴넓이 구하는 클래스 //김승현
		trapazoidMethod trapazoid = new trapazoidMethod();

		trapazoid.inValue();
		trapazoid.outValue();

		// 평행사변형넓이 구하는 클래스 //최성운
		ParallelMethod parallel = new ParallelMethod();

		parallel.inValue();
		parallel.outValue();
		
	
	}

}
