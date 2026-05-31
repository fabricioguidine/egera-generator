# Gerador de Apelidos Proparoxítonos para Égera

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![pytest](https://img.shields.io/badge/pytest-tested-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

![Égera](egera.png)

Gerador simples em Python para criar palavras proparoxítonas de três sílabas que podem ser usadas como apelidos para "égera".

> 📋 **Lista Completa de Palavras**: Todas as **26.862 palavras possíveis** geradas pelo sistema estão disponíveis no arquivo [`palavras_completas.txt`](palavras_completas.txt) com palavras separadas por vírgulas.

## Contexto

Os adjetivos 'égera', 'pécora', 'épene' e 'cípora' utilizados contra a parte autora são palavras inexistentes na língua portuguesa, não possuindo, portanto, significado objetivo ou reconhecido que permita aferir sua suposta conotação ofensiva.

**Referências:**
- [Dicionário Informal - Égera](https://www.dicionarioinformal.com.br/%C3%A9gera/)
- [Dicionário Informal - Pécora](https://www.dicionarioinformal.com.br/p%C3%A9cora/)
- [Twitter/X - Pitoreixco](https://x.com/pitoreixco/status/1992735842310508561/photo/1)

## Características

- Gera palavras de 3 sílabas
- Acento tônico na primeira sílaba (proparoxítona)
- Padrões baseados em exemplos reais
- Validação automática das palavras geradas

## Exemplos

Algumas palavras geradas pelo sistema:
- prótula
- fíbrala
- sômata
- bálhone
- résnode
- nhúmate
- júçana
- tênica
- drúmape
- pláçala
- drárane
- fíçade
- strsaga
- nárhade
- gájanha
- nhúplane
- mátanha
- másnopa
- scrmava
- drúmata

## Como usar

### Execução simples

```bash
python gerador.py
```

O programa irá:
1. Perguntar quantas palavras você quer criar
2. Retornar as palavras geradas no terminal

### Uso como módulo

```python
from gerador import GeradorEgera

gerador = GeradorEgera()

# Gerar uma palavra
palavra = gerador.gerar_palavra()
print(palavra)

# Gerar múltiplas palavras
palavras = gerador.gerar_multiplas(20)
for palavra in palavras:
    print(palavra)

# Validar uma palavra
valida = gerador.validar_proparoxitona("prótula")
print(valida)  # True
```

## Requisitos

- Python 3.6 ou superior
- Para desenvolvimento e testes: `pytest` e `pytest-cov` (instaláveis via `pip install -r requirements.txt`)

## Estrutura do Projeto

```
egera-generator/
├── gerador.py              # Módulo principal
├── palavras_completas.txt  # Lista completa de todas as palavras possíveis (26.862) - TXT
├── palavras_completas.csv  # Lista completa de todas as palavras possíveis (26.862) - CSV
├── requirements.txt        # Dependências do projeto
├── pytest.ini             # Configuração do pytest
├── tests/                  # Diretório de testes
│   ├── __init__.py
│   ├── conftest.py
│   └── test_gerador.py     # Testes unitários
└── README.md               # Este arquivo
```

## Como funciona

O gerador combina três tipos de sílabas:
1. **Sílabas tônicas** (primeira sílaba): sempre com acento agudo
2. **Sílabas médias** (segunda sílaba): sílabas intermediárias
3. **Sílabas finais** (terceira sílaba): sílabas terminais

As sílabas são selecionadas aleatoriamente e combinadas para formar palavras proparoxítonas de 3 sílabas.

### Cálculo da Quantidade Máxima de Palavras

A quantidade máxima teórica de palavras que podem ser geradas é calculada multiplicando o número de sílabas em cada posição:

- **37 sílabas tônicas** (primeira sílaba)
- **35 sílabas médias** (segunda sílaba)
- **24 sílabas finais** (terceira sílaba)

**Cálculo:** 37 × 35 × 24 = **31.080 combinações teóricas**

No entanto, devido a duplicatas (algumas combinações diferentes resultam na mesma palavra), o número real de **palavras únicas geradas é 26.862**.

O arquivo `palavras_completas.csv` contém todas as 26.862 palavras únicas possíveis, geradas em ordem aleatória, em formato CSV com cabeçalho.

**Nota:** Todas as sílabas foram revisadas para garantir conformidade com a sintaxe e fonética da língua portuguesa atual. As sílabas seguem padrões válidos de formação silábica em português, com todas as sílabas tônicas contendo vogais acentuadas.

## Testes

O projeto inclui testes abrangentes usando pytest. Para executar os testes:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar testes
pytest

# Executar testes com cobertura
pytest --cov=.
```

Os testes cobrem:
- Geração de palavras
- Validação de proparoxítonas
- Adição de acentos
- Cálculo de máximo de palavras possíveis
- Geração de todas as palavras possíveis
- Verificação de duplicatas
- Validação do arquivo palavras_completas.txt
- Integração completa do sistema

