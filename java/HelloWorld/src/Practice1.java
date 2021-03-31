import java.util.Arrays;

public class Practice1 {
	public static void main(String[] args) {
		
		int list[] = {7,21,8,43,3,5} ;
		for (int i = 0; i < list.length; i++) {
			for (int j = i + 1; j < list.length; j++) {
				if (list[i] > list[j]) {	
					int li = list[i];	
					list[i] = list[j];
					list[j] = li;
				}
			}
		}
		System.out.println(Arrays.toString(list));
	}
}