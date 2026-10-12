# TP3
Aluno : Afonso Dinis Barbosa Machado Costa.  
Id: A109929.


<img src="../17333.jpg" alt="Foto" width="200">

# [Enunciado](tpc3.pdf)

# Resolução:

## 1. Importação das bibliotecas

```python
import sys
import re
```

- `sys`: permite ler texto introduzido através da entrada padrão.
- `re`: permite utilizar expressões regulares para identificar padrões no texto.

## 2. Definição da função `tokenize()`

```python
def tokenize(input_string):
    reconhecidos = []
    linha = 1
```

- `input_string`: texto que será analisado.
- `reconhecidos`: lista onde serão guardados os tokens válidos.
- `linha`: contador que indica a linha atual do texto, começando em 1.

## 3. Identificação dos tokens

```python
mo = re.finditer(r'...', input_string)
```

A função `re.finditer()` percorre o texto e procura correspondências com os padrões definidos na expressão regular.

Cada padrão identifica um tipo de elemento:

- `COM`: comentários iniciados por `#`. 
```python
 r"\#.*" 
 ``` 
- `VAR`: variáveis iniciadas por `?`.
```python
 r"\?\w+" 
 ``` 
- `LING`: identificadores de linguagem, como `@pt`.
```python
 r"@[A-Za-z]{2}" 
 ``` 
- `STRING`: texto entre aspas.
```python
 r"\"[^"]*\"" 
 ``` 
- `LIMIT`: palavra reservada `LIMIT`.
```python
 r"LIMIT\b" 
 ``` 
- `INT`: números inteiros.
```python
 r"\d+" 
 ``` 
- `CONCEITOS`: palavras e identificadores que podem incluir `:`.
```python
 r"[\w:]+" 
 ``` 
- `DELIMITER`: delimitadores, como `{`, `}`, `.` e `\`.
```python
 r"[{}\.]" 
 ``` 
- `SKIP`: espaços e tabulações.
```python
 r"[ \t]+" 
 ``` 
- `NEWLINE`: mudança de linha.
```python
 r"\n" 
 ``` 
- `ERRO`: qualquer carácter que não corresponda aos padrões anteriores.
```python
 r"."
```
## 4. Percorrer as correspondências

```python
for m in mo:
    dic = m.groupdict()
```

- `for m in mo`: percorre cada correspondência encontrada.
- `m.groupdict()`: cria um dicionário com os grupos nomeados da expressão regular, permitindo identificar qual dos padrões correspondeu ao texto.

## 5. Classificação dos tokens

```python
if dic['COM']:
    t = ("COM", dic['COM'], linha, m.span())
# ...
elif dic['INT']:
    t = ("INT", dic['INT'], linha, m.span())
```

O código verifica qual dos padrões foi reconhecido e cria uma tupla `t` com quatro elementos:

1. **Tipo:** categoria do token.
2. **Valor:** texto reconhecido.
3. **Linha:** linha em que aparece.
4. **Posição:** intervalo de caracteres devolvido por `m.span()`.

O mesmo processo é repetido para os restantes tipos de tokens.

## 6. Tratamento dos espaços e das linhas

```python
elif dic['SKIP']:
    t = ("SKIP", dic['SKIP'], linha, m.span())
elif dic['NEWLINE']:
    t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    linha += 1
```

- `SKIP`: identifica espaços e tabulações.
- `NEWLINE`: identifica uma mudança de linha e incrementa o contador `linha`.

Assim, os tokens seguintes ficam associados à linha correta.

## 7. Tratamento de erros

```python
elif dic['ERRO']:
    t = ("ERRO", dic['ERRO'], linha, m.span())
```

Se um carácter não corresponder a nenhum padrão específico, é classificado como `ERRO`. Isto permite detetar caracteres inesperados no texto.

## 8. Armazenamento dos tokens

```python
if not dic['SKIP'] and t[0] not in ('UNKNOWN', 'COM', 'NEWLINE'):
    reconhecidos.append(t)
```

Esta condição adiciona à lista apenas os tokens que interessam para a análise posterior.

São excluídos:
- Espaços e tabulações (`SKIP`).
- Tokens desconhecidos (`UNKNOWN`).
- Comentários (`COM`).
- Mudanças de linha (`NEWLINE`).

Os tokens classificados como `ERRO` são mantidos na lista.

## 9. Devolver o resultado

```python
return reconhecidos
```

A função devolve a lista com todos os tokens reconhecidos e selecionados.

## 10. Leitura e impressão do resultado

```python
for tok in tokenize(sys.stdin.read()):
    print(tok)
```

- `sys.stdin.read()`: lê todo o texto recebido pela entrada padrão.
- `tokenize(...)`: analisa o texto e devolve os tokens.
- `print(tok)`: imprime cada token individualmente.


### Teste

Para testar o analisador léxico, foi criado um ficheiro de texto com exemplos dos diferentes elementos reconhecidos pelo programa, como variáveis, strings, números inteiros, conceitos e delimitadores. O resultado apresenta os tokens identificados, incluindo o seu tipo, valor, número da linha e posição no texto.

Para executar o programa e apresentar os tokens no terminal:

```bash
python3 Analizador_lexico.py < Teste.txt
```

O programa lê o conteúdo do ficheiro `Teste.txt`, identifica os tokens através das expressões regulares definidas e apresenta os resultados no terminal.

Para guardar os resultados num ficheiro:

```bash
python3 Analizador_lexico.py < Teste.txt > Result.txt
```

Desta forma, os tokens gerados são guardados em `Result.txt`, permitindo consultar e verificar os elementos reconhecidos pelo analisador léxico.

## Links 

[Ver código Python](Analizador_lexico.py)

[Ver ficheiro de teste](Teste.txt)

[Ver ficheiro de resultado](Result.txt)