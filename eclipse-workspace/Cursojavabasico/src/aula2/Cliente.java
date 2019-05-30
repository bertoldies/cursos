package aula2;

public class Cliente {
	private String nome;
	private String endereco;
	
	public Cliente (String nome, String endereco) {
		this.nome=nome;
		this.endereco=endereco;
		
	}
		public String getNome() {
			return nome;
		}
		
		public void setNome(String nome) {
			this.nome=nome;
		}
		
		public String getEndereco() {
			return endereco;
		}
		
		public void setCodigo(String endereco) {
			this.endereco=endereco;
		
	}
		public String toString() {
			return "nome:"+nome+"endereco"+endereco;
		}

}
