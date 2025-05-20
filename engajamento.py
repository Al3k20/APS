def calcular_engajamento():
    print("Digite as métricas de sua publicação:")
    
    curtidas = int(input("Número de curtidas: "))
    comentarios = int(input("Número de comentários: "))
    compartilhamentos = int(input("Número de compartilhamentos: "))
    seguidores = int(input("Número de seguidores: "))
    alcance = int(input("Número de alcance: "))
    impressoes = int(input("Número de impressões: "))

    total_interacoes = curtidas + comentarios + compartilhamentos

    # Cálculo das métricas
    engajamento_seguidores = (total_interacoes / seguidores) * 100 if seguidores > 0 else 0
    engajamento_alcance = (total_interacoes / alcance) * 100 if alcance > 0 else 0
    engajamento_impressoes = (total_interacoes / impressoes) * 100 if impressoes > 0 else 0

    # Exibição dos resultados
    print("\nResultados:")
    print(f"Engajamento por seguidores: {engajamento_seguidores:.2f}%")
    print(f"Engajamento por alcance: {engajamento_alcance:.2f}%")
    print(f"Engajamento por impressões: {engajamento_impressoes:.2f}%")

# Executa o programa
calcular_engajamento()
