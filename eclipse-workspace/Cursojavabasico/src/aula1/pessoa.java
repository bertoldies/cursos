package aula1;

public class pessoa {
	private String nome;
	private int codigo;
	
	public pessoa (int codigo, String nome) {
		this.codigo=codigo;
		this.nome=nome;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome=nome;
	}
	
	public int getCodigo() {
		return codigo;
	}
	
	public void setCodigo(int codigo) {
		this.codigo=codigo;
	}

}
