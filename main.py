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

