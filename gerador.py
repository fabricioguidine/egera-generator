#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de palavras proparoxítonas de três sílabas
para criar apelidos em potencial para "égera"
"""

import random
import re
from typing import List


class GeradorEgera:
    """
    Gerador de palavras proparoxítonas de 3 sílabas.
    
    Combina sílabas tônicas, médias e finais para criar palavras
    proparoxítonas que podem ser usadas como apelidos.
    """
    
    # Constantes para validação
    NUM_SILABAS_ESPERADO = 3
    VOGAIS_ACENTUADAS = 'áéíóú'
    VOGAIS_BASICAS = 'aeiou'
    
    def __init__(self):
        # Sílabas iniciais (tônicas) - primeira sílaba
        # Todas devem ter vogal para formar sílaba válida em português
        self.silabas_tonicas = [
            'pró', 'fí', 'sô', 'bál', 'rés', 'nhú', 'jú', 'tê', 'drú',
            'cá', 'dé', 'fó', 'gá', 'hí', 'lí', 'má', 'ná', 'pá', 'rá',
            'sá', 'tá', 'vá', 'zá', 'chá', 'flá', 'glá', 'plá', 'trá',
            'brá', 'crá', 'drá', 'frá', 'grá', 'prá', 'scrá', 'sprá', 'strá'
        ]
        
        # Sílabas médias - segunda sílaba
        self.silabas_medias = [
            'tu', 'bra', 'ma', 'ho', 'sno', 'ma', 'ça', 'ni', 'ma',
            'la', 'ta', 'na', 'ra', 'sa', 'ca', 'da', 'fa', 'ga',
            'ha', 'ja', 'ka', 'pa', 'va', 'xa', 'za', 'cha', 'lha',
            'nha', 'rha', 'tha', 'bla', 'cla', 'fla', 'gla', 'pla'
        ]
        
        # Sílabas finais - terceira sílaba
        self.silabas_finais = [
            'la', 'ta', 'ne', 'de', 'te', 'na', 'ca', 'pe',
            'ra', 'sa', 'da', 'fa', 'ga', 'ma', 'pa', 'va',
            'za', 'cha', 'lha', 'nha', 'rha', 'tha', 'ca', 'ga'
        ]
    
    def adicionar_acento(self, silaba: str) -> str:
        """
        Adiciona acento agudo na primeira vogal da sílaba tônica.
        
        Args:
            silaba: Sílaba que pode ou não ter acento
            
        Returns:
            Sílaba com acento agudo na primeira vogal
        """
        vogais_acentuadas = {
            'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú'
        }
        
        # Se já tem acento, retorna como está
        if any(c in silaba for c in self.VOGAIS_ACENTUADAS):
            return silaba
        
        # Encontra a primeira vogal e acentua
        for i, char in enumerate(silaba):
            if char.lower() in vogais_acentuadas:
                vogal_acentuada = vogais_acentuadas[char.lower()]
                if char.isupper():
                    vogal_acentuada = vogal_acentuada.upper()
                return silaba[:i] + vogal_acentuada + silaba[i+1:]
        
        return silaba
    
    def gerar_palavra(self) -> str:
        """
        Gera uma palavra proparoxítona de 3 sílabas aleatoriamente.
        
        Returns:
            Palavra proparoxítona de 3 sílabas com acento na primeira sílaba
        """
        # Seleciona sílabas aleatoriamente
        silaba1 = random.choice(self.silabas_tonicas)
        silaba2 = random.choice(self.silabas_medias)
        silaba3 = random.choice(self.silabas_finais)
        
        # Garante que a primeira sílaba tenha acento
        silaba1 = self.adicionar_acento(silaba1)
        
        # Combina as sílabas
        return silaba1 + silaba2 + silaba3
    
    def gerar_multiplas(self, quantidade: int = 10) -> List[str]:
        """
        Gera múltiplas palavras proparoxítonas.
        
        Args:
            quantidade: Número de palavras a gerar (padrão: 10)
            
        Returns:
            Lista de palavras proparoxítonas geradas
        """
        return [self.gerar_palavra() for _ in range(quantidade)]
    
    def calcular_maximo_palavras(self) -> int:
        """
        Calcula a quantidade máxima teórica de palavras que podem ser geradas.
        
        Returns:
            Número máximo teórico de combinações possíveis
        """
        return len(self.silabas_tonicas) * len(self.silabas_medias) * len(self.silabas_finais)
    
    def gerar_todas_palavras_possiveis(self) -> List[str]:
        """
        Gera todas as palavras possíveis sem duplicatas.
        
        Returns:
            Lista com todas as palavras únicas possíveis
        """
        palavras = []
        
        # Gera todas as combinações possíveis
        for silaba1 in self.silabas_tonicas:
            for silaba2 in self.silabas_medias:
                for silaba3 in self.silabas_finais:
                    # Garante que a primeira sílaba tenha acento
                    silaba1_acentuada = self.adicionar_acento(silaba1)
                    palavra = silaba1_acentuada + silaba2 + silaba3
                    palavras.append(palavra)
        
        # Remove duplicatas e retorna
        return list(set(palavras))
    
    def validar_proparoxitona(self, palavra: str) -> bool:
        """
        Valida se a palavra tem 3 sílabas e é proparoxítona.
        
        Args:
            palavra: Palavra a ser validada
            
        Returns:
            True se a palavra é proparoxítona de 3 sílabas, False caso contrário
        """
        palavra_lower = palavra.lower()
        
        # Conta sílabas aproximadas (vogais)
        vogais = re.findall(rf'[{self.VOGAIS_BASICAS}{self.VOGAIS_ACENTUADAS}]', palavra_lower)
        num_silabas = len(vogais)
        
        # Verifica se tem acento na primeira sílaba
        primeira_silaba = re.match(
            rf'^[^{self.VOGAIS_BASICAS}{self.VOGAIS_ACENTUADAS}]*[{self.VOGAIS_BASICAS}{self.VOGAIS_ACENTUADAS}]',
            palavra_lower
        )
        tem_acento_na_primeira = (
            primeira_silaba is not None and
            any(c in primeira_silaba.group() for c in self.VOGAIS_ACENTUADAS)
        )
        
        return num_silabas == self.NUM_SILABAS_ESPERADO and tem_acento_na_primeira


def main() -> None:
    """
    Função principal do programa.
    
    Interage com o usuário para gerar palavras proparoxítonas.
    """
    gerador = GeradorEgera()
    
    print("Gerador de Apelidos Proparoxítonos para Égera")
    print()
    
    # Calcula e exibe a quantidade máxima de palavras possíveis
    maximo = gerador.calcular_maximo_palavras()
    print(f"Quantidade máxima de palavras que podem ser geradas: {maximo:,}")
    print()
    
    # Pergunta quantas palavras o usuário quer criar
    quantidade_input = input("Quantas palavras você quer criar? ").strip()
    
    try:
        quantidade = int(quantidade_input)
        if quantidade <= 0:
            print("Por favor, digite um número positivo.")
            return
        if quantidade > maximo:
            print(f"Erro: Você solicitou {quantidade:,} palavras, mas o máximo possível é {maximo:,}.")
            print(f"Por favor, digite um número entre 1 e {maximo:,}.")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        return
    
    # Gera as palavras
    palavras = gerador.gerar_multiplas(quantidade)
    
    # Exibe as palavras geradas
    print()
    print("Palavras geradas:")
    for palavra in palavras:
        print(palavra)


if __name__ == "__main__":
    main()

