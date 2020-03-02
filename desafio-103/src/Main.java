
public class Main {

	public static void main(String[] args) {
		
		// Desafio 103
		String s = "qqqqqqssdfasf"; 
		String invertida = "";
		for (int i = s.length()-1; i >= 0; i--) {
			invertida += s.charAt(i); 
		} 
		System.out.println(invertida);	
 
	}	
}
