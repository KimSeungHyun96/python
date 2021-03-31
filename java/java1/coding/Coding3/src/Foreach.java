
public class Foreach {
	public static void main(String[] args) {
		
	/*	String[] members = { "최진혁", "최유빈", "한이람" };
		for (int i = 0; i < members.length; i++) {
			String member = members[i];
			System.out.println(member + "이 상담을 받았습니다");
		} */
		
	/*	String[] members = { "최진혁", "최유빈", "한이람" };
		for (String e : members) {
			System.out.println(e + "이 상담을 받았습니다");
		} */
		
	//	오류
		
	/*	String[] members = { "최진혁", "최유빈", "한이람" };
		System.out.println(members [3]);
		===================================================================
		Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 3
		at Foreach.main(Foreach.java:18)
		
		String[] members = new String[3];
		members [0] = "최진혁";
		members [1] = "최유빈";
		members [2] = "한이람";
		members [3] = "이고잉";
		===================================================================
		Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 3
		at Foreach.main(Foreach.java:26) */
	}
}
