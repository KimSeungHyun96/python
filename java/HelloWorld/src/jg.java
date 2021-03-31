
public class jg {
	public static void main(String[] args) {
		
		System.out.println(myRecursive(1));
		
	}
	
	// f(n) = n + f(n+1)
	// n >= 100; then exit
	
	public static int myRecursive(int n) {
		if(n >= 100) return 100;
		return n + myRecursive(n+1);
	}
//		return 1 + f(2)
//					return 2 + f(3)
//								return 3 + f(4)
//											return 4 + (5)
//														return5;
}


//public static void main(String[] args) {
//	// TODO Auto-generated method stub
//	
//		System.out.println(myRecursive(1));
//	
//	}
//	
//	 f(n) = n + f(n+1) 
//	 n >= 100; then exit
//	
//	public static int myRecursive(int n) {
//		if(n >= 5) return 5;
//		
//		return n + myRecursive(n+1);
//	}
//	 return 1 + f(2)
//	            return 2 + f(3)
//							 return 3 + f(4)
//										return 4 + f(5)
//	 											return 5;