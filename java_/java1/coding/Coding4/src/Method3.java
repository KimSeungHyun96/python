
public class Method3 {
    public static String numbering(int init, int limit) {
       
    	// 메소드 출력
    	int i = init;
        // 만들어지는 숫자들을 output이라는 변수에 담기 위해서 변수에 빈 값을 주었다.
        String output = "";
        while (i < limit) {
            // 숫자를 화면에 출력하는 대신 변수 output에 담았다.
            output += i;
            i++;
        }
        // 중요!!! output에 담겨 있는 문자열을 메소드 외부로 반환하려면
        // 아래와 같이 return 키워드 뒤에 반환하려는 값을 배치하면 된다.
        return output; // Mehtod(메소드)를 종료시킴
    }
 
    public static void main(String[] args) { // main(메소드)의 return값은 존재X
        // 메소드 numbering이 리턴한 값이 변수 result에 담긴다.
        String result = numbering(1, 5); // 반드시 String이 되어야 함
        // 변수 result의 값을 화면에 출력한다.
        System.out.println(result);
    }
}