# -*- coding: utf-8 -*-
"""
Atividade de Recuperação - Agenda 10 - DSI
Estudante: Paulo
Objetivo: Automatizar o cálculo de notas, identificação de aprovação e geração de relatórios.
"""

def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.
    Trata o erro de lista vazia para evitar divisão por zero.
    """
    if not notas:
        return 0.0
    return round(sum(notas) / len(notas), 2)

def verificar_aprovacao(media, frequencia):
    """
    Verifica a situação do aluno com base na média e na frequência.
    Critérios: Média mínima 6.0 e Frequência mínima 75%.
    Retorna uma string: "Aprovado" ou "Reprovado".
    """
    if media >= 6.0 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"

def gerar_relatorio_aluno(nome, disciplina, notas, frequencia):
    """
    Procedimento que atua como camada de visualização (I/O).
    Agrupa as funções de cálculo e exibe o desempenho formatado.
    """
    media = calcular_media(notas)
    situacao = verificar_aprovacao(media, frequencia)
    
    print("-" * 50)
    print(f"RELATÓRIO DE DESEMPENHO ESCOLAR")
    print("-" * 50)
    print(f"Aluno: {nome}")
    print(f"Disciplina: {disciplina}")
    print(f"Notas: {', '.join(map(str, notas))}")
    print(f"Média Final: {media}")
    print(f"Frequência: {frequencia}%")
    print(f"Situação: {situacao}")
    print("-" * 50)

# Exemplo de execução para testes
if __name__ == "__main__":
    # Teste com aluno aprovado
    gerar_relatorio_aluno("Carlos Silva", "Programação de Computadores", [8.5, 7.0, 6.0], 85)
    
    # Teste com aluno reprovado por nota
    gerar_relatorio_aluno("Ana Souza", "Banco de Dados", [5.0, 4.5, 6.0], 90)
