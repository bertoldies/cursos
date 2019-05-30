package aula1;

public class pessoaApp {
	
	public static void main(String[] args) {
		
		pessoa pessoa1 = new pessoa(1, "Ana");
		pessoa pessoa2 = new pessoa(1, "Sandro");
		
		System.out.println("o nome do objeto pessoa1 e "+ pessoa1.getNome());
		
		pessoa1.setNome("Eduardo");
		
		System.out.println("o nome do objeto pessoa1 e "+ pessoa1.getNome());
	}

}
