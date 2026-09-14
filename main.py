#Etapa 1: Cadastro da Startup e Projetos (Dicionários e Listas)
startup = {
	"nome": "CyberPulse Tech",
	"segmento": "Segurança da Informação",
	"ano_adesao": "2026",
}

solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

print("Nome da startup:", startup["nome"])
print("Segmento:", startup["segmento"])
print("Primeiro produto:", solucoes_ativas[0])

#Etapa 2: Mapeamento das Bancadas de Trabalho (Matriz 2D)
bancadas = [
	[1, 0],
	[0, 1],
]

print("Bancada N1:", bancadas[0][0])
print("Bancada N2:", bancadas[0][1])
print("Bancada S1:", bancadas[1][0])
print("Bancada S2:", bancadas[1][1])
print("Legenda: 1 = Ocupado e 0 = Livre")

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
	linha_cabecalho = arquivo.readline()
	linha_dado_1 = arquivo.readline()
	linha_dado_2 = arquivo.readline()
	linha_dado_3 = arquivo.readline()
	linha_dado_4 = arquivo.readline()

print(linha_cabecalho, end="")
print(linha_dado_1, end="")
print(linha_dado_2, end="")
print(linha_dado_3, end="")
print(linha_dado_4, end="")

