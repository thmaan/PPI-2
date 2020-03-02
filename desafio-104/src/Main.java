
public class Main {

	public static void main(String[] args) {
		// Desafio 104 1
			int x = 1;
			int y = 2;
			int temp;
			temp = x;
			x = y;
			y = temp;
		
			System.out.println("x: " + x +" y:" + y );
				
			// Desafio 104 2 - String
			String a = "Mama";
			String b = "Mia";
			a = a + b;  
		    b = a.substring(0, a.length() - b.length());  
		    a = a.substring(b.length()); 
		    System.out.println("a = " + a + " b = " + b);

		    // Desafio 104 2 - Numero
	        x = x + y;  
	        y = x - y;  
	        x = x - y; 
	        System.out.println("x: " + x + "y: " + y);
	}

}
