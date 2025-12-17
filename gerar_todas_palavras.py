#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar todas as palavras possíveis do gerador.

Gera todas as combinações possíveis de palavras proparoxítonas
e salva em arquivo TXT com uma palavra por linha.
"""
import random
from gerador import GeradorEgera


def main() -> None:
    """Função principal do script."""
    gerador = GeradorEgera()
    
    print("Gerando todas as palavras possíveis...")
    
    # Gera todas as palavras possíveis usando o método da classe
    palavras_unicas = gerador.gerar_todas_palavras_possiveis()
    
    # Embaralha em ordem aleatória
    random.shuffle(palavras_unicas)
    
    # Salva em arquivo TXT com uma palavra por linha
    arquivo_txt = 'palavras_completas.txt'
    with open(arquivo_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(palavras_unicas))
    
    maximo_teorico = gerador.calcular_maximo_palavras()
    
    print(f"✓ Total de palavras geradas: {len(palavras_unicas):,}")
    print(f"✓ Máximo teórico: {maximo_teorico:,}")
    print(f"✓ Duplicatas removidas: {maximo_teorico - len(palavras_unicas):,}")
    print(f"✓ Arquivo TXT salvo: {arquivo_txt} (uma palavra por linha, em ordem aleatória)")


if __name__ == "__main__":
    main()

