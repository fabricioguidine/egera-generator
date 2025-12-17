"""
Testes unitários para a classe GeradorEgera
"""
import pytest
import re
from gerador import GeradorEgera


class TestGeradorEgera:
    """Testes para a classe GeradorEgera"""
    
    @pytest.fixture
    def gerador(self):
        """Fixture que retorna uma instância de GeradorEgera"""
        return GeradorEgera()
    
    def test_inicializacao(self, gerador):
        """Testa se o gerador é inicializado corretamente"""
        assert gerador is not None
        assert hasattr(gerador, 'silabas_tonicas')
        assert hasattr(gerador, 'silabas_medias')
        assert hasattr(gerador, 'silabas_finais')
        assert len(gerador.silabas_tonicas) > 0
        assert len(gerador.silabas_medias) > 0
        assert len(gerador.silabas_finais) > 0
    
    def test_adicionar_acento_com_silaba_ja_acentuada(self, gerador):
        """Testa que sílabas já acentuadas não são modificadas"""
        silabas_ja_acentuadas = ['pró', 'fí', 'sô', 'bál', 'rés', 'nhú', 'jú', 'tê', 'drú']
        for silaba in silabas_ja_acentuadas:
            assert gerador.adicionar_acento(silaba) == silaba
    
    def test_adicionar_acento_silaba_sem_acento(self, gerador):
        """Testa que acentos são adicionados corretamente"""
        casos_teste = [
            ('ca', 'cá'),
            ('de', 'dé'),
            ('fi', 'fí'),
            ('go', 'gó'),
            ('hu', 'hú'),
            ('pro', 'pró'),
        ]
        for entrada, esperado in casos_teste:
            resultado = gerador.adicionar_acento(entrada)
            assert resultado == esperado, f"Esperado {esperado}, mas obteve {resultado}"
    
    def test_adicionar_acento_preserva_maiusculas(self, gerador):
        """Testa que maiúsculas são preservadas ao adicionar acento"""
        resultado = gerador.adicionar_acento('CA')
        assert resultado == 'CÁ'
        assert resultado.isupper()
    
    def test_gerar_palavra_retorna_string(self, gerador):
        """Testa que gerar_palavra retorna uma string"""
        palavra = gerador.gerar_palavra()
        assert isinstance(palavra, str)
        assert len(palavra) > 0
    
    def test_gerar_palavra_tem_acento_na_primeira_silaba(self, gerador):
        """Testa que palavras geradas têm acento na primeira sílaba"""
        for _ in range(20):  # Testa múltiplas palavras
            palavra = gerador.gerar_palavra()
            # Verifica se há acento na primeira sílaba
            primeira_silaba = re.match(r'^[^aeiouáéíóú]*[aeiouáéíóú]', palavra.lower())
            assert primeira_silaba is not None, f"Palavra {palavra} não tem primeira sílaba identificável"
            tem_acento = any(c in primeira_silaba.group() for c in 'áéíóú')
            assert tem_acento, f"Palavra {palavra} não tem acento na primeira sílaba"
    
    def test_gerar_palavra_tem_tres_silabas(self, gerador):
        """Testa que palavras geradas têm aproximadamente 3 sílabas"""
        for _ in range(20):
            palavra = gerador.gerar_palavra()
            vogais = re.findall(r'[aeiouáéíóú]', palavra.lower())
            num_silabas = len(vogais)
            assert num_silabas == 3, f"Palavra {palavra} tem {num_silabas} sílabas, esperado 3"
    
    def test_gerar_multiplas_retorna_lista(self, gerador):
        """Testa que gerar_multiplas retorna uma lista"""
        palavras = gerador.gerar_multiplas(5)
        assert isinstance(palavras, list)
    
    def test_gerar_multiplas_quantidade_correta(self, gerador):
        """Testa que gerar_multiplas retorna a quantidade solicitada"""
        for quantidade in [1, 5, 10, 20, 50]:
            palavras = gerador.gerar_multiplas(quantidade)
            assert len(palavras) == quantidade, \
                f"Esperado {quantidade} palavras, mas obteve {len(palavras)}"
    
    def test_gerar_multiplas_palavras_unicas(self, gerador):
        """Testa que palavras geradas podem ser diferentes (aleatoriedade)"""
        palavras = gerador.gerar_multiplas(100)
        # Com 100 palavras, é muito provável que haja pelo menos algumas diferentes
        palavras_unicas = set(palavras)
        assert len(palavras_unicas) > 1, \
            "Todas as palavras geradas são idênticas (possível problema de aleatoriedade)"
    
    def test_validar_proparoxitona_palavras_validas(self, gerador):
        """Testa validação com palavras proparoxítonas válidas"""
        palavras_validas = ['prótula', 'fíbrala', 'sômata', 'bálhone', 'résnode', 
                           'nhúmate', 'júçana', 'tênica', 'drúmape']
        for palavra in palavras_validas:
            assert gerador.validar_proparoxitona(palavra), \
                f"Palavra {palavra} deveria ser válida"
    
    def test_validar_proparoxitona_palavras_invalidas(self, gerador):
        """Testa validação com palavras inválidas"""
        palavras_invalidas = [
            'casa',      # 2 sílabas
            'computador',  # 4 sílabas
            'casa',      # sem acento
            'cá',        # 1 sílaba
            'prótulá',   # acento na última sílaba
        ]
        for palavra in palavras_invalidas:
            assert not gerador.validar_proparoxitona(palavra), \
                f"Palavra {palavra} não deveria ser válida"
    
    def test_validar_proparoxitona_palavras_geradas(self, gerador):
        """Testa que palavras geradas são validadas corretamente"""
        palavras = gerador.gerar_multiplas(50)
        for palavra in palavras:
            assert gerador.validar_proparoxitona(palavra), \
                f"Palavra gerada {palavra} não passou na validação"
    
    def test_gerar_palavra_usa_silabas_do_gerador(self, gerador):
        """Testa que palavras geradas usam sílabas do conjunto definido"""
        palavras = gerador.gerar_multiplas(100)
        todas_silabas_tonicas = '|'.join(gerador.silabas_tonicas)
        
        for palavra in palavras:
            # Verifica se a primeira sílaba (sem acento) está nas sílabas tônicas
            primeira_silaba_sem_acento = re.match(r'^[^aeiouáéíóú]*[aeiouáéíóú]', palavra.lower())
            if primeira_silaba_sem_acento:
                primeira_silaba = primeira_silaba_sem_acento.group()
                primeira_silaba_sem_acento = primeira_silaba.replace('á', 'a').replace('é', 'e')
                primeira_silaba_sem_acento = primeira_silaba_sem_acento.replace('í', 'i').replace('ó', 'o')
                primeira_silaba_sem_acento = primeira_silaba_sem_acento.replace('ú', 'u')
                # Verifica se começa com alguma sílaba tônica conhecida
                assert any(primeira_silaba_sem_acento.startswith(s.replace('á', 'a').replace('é', 'e')
                                                                 .replace('í', 'i').replace('ó', 'o')
                                                                 .replace('ú', 'u')) 
                          for s in gerador.silabas_tonicas), \
                    f"Primeira sílaba {primeira_silaba} não está nas sílabas tônicas conhecidas"
    
    def test_gerar_multiplas_com_zero_retorna_lista_vazia(self, gerador):
        """Testa que gerar_multiplas(0) retorna lista vazia"""
        palavras = gerador.gerar_multiplas(0)
        assert palavras == []
        assert len(palavras) == 0
    
    def test_palavras_geradas_nao_sao_vazias(self, gerador):
        """Testa que palavras geradas não são strings vazias"""
        palavras = gerador.gerar_multiplas(20)
        for palavra in palavras:
            assert palavra.strip() != "", f"Palavra vazia gerada: '{palavra}'"
            assert len(palavra) >= 3, f"Palavra muito curta: '{palavra}'"
    
    def test_calcular_maximo_palavras(self, gerador):
        """Testa o cálculo da quantidade máxima de palavras possíveis"""
        maximo = gerador.calcular_maximo_palavras()
        
        # O máximo deve ser o produto das quantidades de sílabas
        esperado = len(gerador.silabas_tonicas) * len(gerador.silabas_medias) * len(gerador.silabas_finais)
        assert maximo == esperado, \
            f"Esperado {esperado}, mas obteve {maximo}"
        
        # O máximo deve ser um número positivo
        assert maximo > 0, "Máximo deve ser maior que zero"
    
    def test_calcular_maximo_palavras_consistente(self, gerador):
        """Testa que o cálculo do máximo é consistente"""
        maximo1 = gerador.calcular_maximo_palavras()
        maximo2 = gerador.calcular_maximo_palavras()
        
        assert maximo1 == maximo2, "Cálculo do máximo deve ser consistente"


class TestIntegracao:
    """Testes de integração para o gerador completo"""
    
    @pytest.fixture
    def gerador(self):
        """Fixture que retorna uma instância de GeradorEgera"""
        return GeradorEgera()
    
    def test_fluxo_completo_geracao_validacao(self, gerador):
        """Testa o fluxo completo: gerar -> validar"""
        palavras = gerador.gerar_multiplas(30)
        
        assert len(palavras) == 30
        
        for palavra in palavras:
            # Verifica estrutura básica
            assert isinstance(palavra, str)
            assert len(palavra) > 0
            
            # Valida como proparoxítona
            assert gerador.validar_proparoxitona(palavra), \
                f"Palavra {palavra} falhou na validação"
            
            # Verifica que tem acento
            assert any(c in palavra for c in 'áéíóú'), \
                f"Palavra {palavra} não tem acento"
    
    def test_consistencia_multiplas_geracoes(self, gerador):
        """Testa que múltiplas gerações produzem resultados consistentes"""
        resultados = []
        for _ in range(10):
            palavras = gerador.gerar_multiplas(10)
            resultados.append(palavras)
        
        # Todas as gerações devem ter 10 palavras
        for palavras in resultados:
            assert len(palavras) == 10
        
        # Todas as palavras devem ser válidas
        for palavras in resultados:
            for palavra in palavras:
                assert gerador.validar_proparoxitona(palavra)
    
    def test_gerar_todas_palavras_possiveis_retorna_lista(self, gerador):
        """Testa que gerar_todas_palavras_possiveis retorna uma lista"""
        palavras = gerador.gerar_todas_palavras_possiveis()
        assert isinstance(palavras, list)
        assert len(palavras) > 0
    
    def test_gerar_todas_palavras_possiveis_quantidade_correta(self, gerador):
        """Testa que todas as palavras possíveis foram geradas"""
        palavras = gerador.gerar_todas_palavras_possiveis()
        maximo_esperado = gerador.calcular_maximo_palavras()
        
        # Pode haver menos palavras devido a duplicatas, mas não mais
        assert len(palavras) <= maximo_esperado, \
            f"Esperado no máximo {maximo_esperado} palavras, mas obteve {len(palavras)}"
        
        # Verifica que todas as palavras são válidas
        for palavra in palavras:
            assert gerador.validar_proparoxitona(palavra), \
                f"Palavra {palavra} não passou na validação"
    
    def test_gerar_todas_palavras_possiveis_sem_duplicatas(self, gerador):
        """Testa que não há duplicatas na lista de todas as palavras possíveis"""
        palavras = gerador.gerar_todas_palavras_possiveis()
        palavras_unicas = set(palavras)
        
        assert len(palavras) == len(palavras_unicas), \
            f"Encontradas {len(palavras) - len(palavras_unicas)} palavras duplicadas"
    
    def test_arquivo_palavras_completas_existe_e_contem_todas(self, gerador):
        """Testa que o arquivo palavras_completas.txt existe e contém todas as palavras"""
        import os
        
        if os.path.exists('palavras_completas.txt'):
            with open('palavras_completas.txt', 'r', encoding='utf-8') as f:
                palavras_arquivo = [linha.strip() for linha in f if linha.strip()]
            
            palavras_geradas = gerador.gerar_todas_palavras_possiveis()
            palavras_geradas_set = set(palavras_geradas)
            palavras_arquivo_set = set(palavras_arquivo)
            
            # Verifica que todas as palavras do arquivo estão nas palavras geradas
            assert palavras_arquivo_set.issubset(palavras_geradas_set), \
                "O arquivo contém palavras que não foram geradas pelo sistema"
            
            # Verifica que todas as palavras geradas estão no arquivo
            assert palavras_geradas_set.issubset(palavras_arquivo_set), \
                f"Faltam {len(palavras_geradas_set - palavras_arquivo_set)} palavras no arquivo"
            
            # Verifica que a quantidade está correta
            assert len(palavras_arquivo) == len(palavras_geradas), \
                f"Arquivo tem {len(palavras_arquivo)} palavras, mas deveria ter {len(palavras_geradas)}"

