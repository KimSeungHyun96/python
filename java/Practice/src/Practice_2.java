import java.util.Random;
import java.util.Scanner;

public class Practice_2 {
	public static void main(String[] args) {
	  System.out.println("가위바위보 중 하나를 입력하세요.");
	  System.out.println(" 1 : 가위");
	  System.out.println(" 2 : 바위");
	  System.out.println(" 3 : 보");
	  
	  Scanner s = new Scanner(System.in);
	  int user = s.nextInt();
	  
	  if (user == 0) {
		  System.out.println("사용자는 가위를 냈습니다."); 
	  	} else if (user == 1) {
	  		System.out.println("사용자는 바위를 냈습니다.");
	  	} else if (user == 2) {
	  		System.out.println("사용자는 보를 냈습니다.");
	  	}
  	
	  Random r = new Random();
	  int com = r.nextInt(3) + 1;
	  
	  if (com == 0) {
		  System.out.println("컴퓨터는 가위를 냈습니다.");
	  } else if (com == 1) {
  		  System.out.println("컴퓨터는 바위를 냈습니다.");
	  } else if (com == 2) {
		  System.out.println("컴퓨터는 보를 냈습니다.");
	  }
	  
	  if (user == com) {
			System.out.println("비겼습니다.");			
		} else if (user == 1 && com == 2) {
			System.out.println("컴퓨터 승리");
		} else if (user == 1 && com == 3) {
			System.out.println("사용자 승리");
		} else if (user == 2 && com == 3) {
			System.out.println("컴퓨터 승리");
		} else if (user == 2 && com == 1) {
			System.out.println("사용자 승리");
		} else if (user == 3 && com == 1) {
			System.out.println("컴퓨터 승리");
		} else if (user == 3 && com == 2) {
			System.out.println("사용자 승리");
		}
	}
}
