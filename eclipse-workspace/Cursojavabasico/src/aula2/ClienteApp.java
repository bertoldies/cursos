package aula2;

import aula1.pessoa;

public class ClienteApp {
	
	public static void main(String[] args) {
		
		ClientePF clientepf1 = new ClientePF("5555", "Ana","22222222");
		ClientePJ clientepj1 = new ClientePJ("52222", "Pedro","22222555555222");
		
		
	
		 
		System.out.println("Dados cliente pf "+ clientepj1.getNome() +"\n"+ clientepj1.getEndereco() + "\n "+ clientepj1.getCnpj()); 
						
		System.out.println("Dados cliente pf "+ clientepf1.getNome() +"\n "+ clientepf1.getEndereco() + "\n "+ clientepf1.getCpf());
		
		System.out.println(clientepf1.toString());
		System.out.println(clientepj1.toString());
	}

}
