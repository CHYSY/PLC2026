# TP1
Aluno : Afonso Dinis Barbosa Machado Costa.  
Id: A109929.


<img src="../17333.jpg" alt="Foto" width="200">


# Enunciado: 
## TPC2: Conversor de MarkDown para HTML

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

### Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: `# Exemplo`

Out: `<h1>Exemplo</h1>`

### Bold: pedaços de texto entre "**":

In: `Este é um **exemplo** ...`

Out: `Este é um <b>exemplo</b> ...`

### Itálico: pedaços de texto entre "*":

In: `Este é um *exemplo* ...`

Out: `Este é um <i>exemplo</i> ...`

### Lista numerada:

In:
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

Out:
```
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

### Link: [texto](endereço URL)

In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`

Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

### Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`

Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`


# Resolução:

```python
import re 
import sys 
text = sys.stdin.read()
```
Neste bloco são importados os módulos re e sys. O módulo re permite trabalhar com expressões regulares, usadas para identificar os elementos de Markdown. O sys.stdin.read() lê todo o texto introduzido através da entrada padrão e guarda-o na variável text.

### Cabeçalhos:


```python
hashtag1 = r"^(#{1,3}) (.+)$"
def aux(match):
    nivel = len(match.group(1))
    texto = match.group(2)
    return f"<h{nivel}>{texto}</h{nivel}>"
text = re.sub(hashtag1,aux,text,flags=re.MULTILINE)
```
Neste bloco é definida a expressão regular hashtag1, que identifica cabeçalhos com um, dois ou três #. A função aux determina o nível do cabeçalho através do número de # e transforma o texto para a respetiva tag HTML (\<h1>, \<h2> ou \<h3>). Por fim, re.sub substitui os cabeçalhos encontrados pelo seu equivalente em HTML.
### Bold e Itálico:

```python
asteriscos = r"(\*{1,2})(.*?)(\1)"
def asteriscos_aux(match):
    qts = len(match.group(1))
    texto = match.group(2)
    if qts == 1:
        return f"<i>{texto}</i>"
    else:
        return f"<b>{texto}</b>"
text = re.sub(asteriscos,asteriscos_aux,text)
```
Neste bloco é utilizada uma expressão regular para identificar texto entre um ou dois asteriscos. A função asteriscos_aux verifica a quantidade de asteriscos: com um asterisco transforma o texto em itálico (\<i>) e com dois transforma-o em negrito (\<b>). A substituição é feita através de re.sub.

### Listas:
```python
listas = r"(?:^\d+\. .+(?:\n|$))+"
def listas_aux(match):
    linhas = match.group(0).strip().split("\n")

    texto = [
        f"<li>{re.sub(r'^\d+\. ', '', linha)}</li>"
        for linha in linhas
    ]

    return "<ol>\n" + "\n".join(texto) + "\n</ol>\n"

text = re.sub(listas, listas_aux, text, flags=re.MULTILINE)
```
Neste bloco é identificada uma sequência de itens de uma lista ordenada. A função listas_aux separa cada linha e remove a numeração (1., 2., 3., etc.), colocando cada item dentro de uma tag \<li>. No final, todos os itens são agrupados dentro das tags \<ol>.

### Links e Imagens:
```python
midia = r"(!)?\[([^\]]+)\]\(([^\)]+)\)"
def midia_aux(match):
    is_image = match.group(1) # Será "!" se for imagem, ou None se for link
    texto = match.group(2)
    url = match.group(3)
    
    if is_image:
        return f'<img src="{url}" alt="{texto}"/>'
    else:
        return f'<a href="{url}">{texto}</a>'
        
text = re.sub(midia, midia_aux, text)
```
Neste bloco são identificados links e imagens através da mesma expressão regular. A função midia_aux verifica se existe um ! antes dos parênteses. Se existir, o elemento é uma imagem e é convertido para \<img>. Caso contrário, é convertido para um link através da tag \<a>.

### Função completa:
A função converte aplica todas as transformações ao texto pela ordem definida e devolve o resultado final em HTML. Por fim, print() apresenta esse resultado.

```python
def converte(text):

    hashtag1 = r"^(#{1,3}) (.+)$"
    def aux(match):
        nivel = len(match.group(1))
        texto = match.group(2)
        return f"<h{nivel}>{texto}</h{nivel}>"
    text = re.sub(hashtag1,aux,text,flags=re.MULTILINE)
    
    asteriscos = r"(\*{1,2})(.*?)(\1)"
    def asteriscos_aux(match):
        qts = len(match.group(1))
        texto = match.group(2)
        if qts == 1:
            return f"<i>{texto}</i>"
        else:
            return f"<b>{texto}</b>"
    text = re.sub(asteriscos,asteriscos_aux,text)

    listas = r"(?:^\d+\. .+(?:\n|$))+"
    def listas_aux(match):
        linhas = match.group(0).strip().split("\n")

        texto = [
            f"<li>{re.sub(r'^\d+\. ', '', linha)}</li>"
            for linha in linhas
        ]

        return "<ol>\n" + "\n".join(texto) + "\n</ol>\n"

    text = re.sub(listas, listas_aux, text, flags=re.MULTILINE)


    midia = r"(!)?\[([^\]]+)\]\(([^\)]+)\)"
    def midia_aux(match):
        is_image = match.group(1) # Será "!" se for imagem, ou None se for link
        texto = match.group(2)
        url = match.group(3)
        
        if is_image:
            return f'<img src="{url}" alt="{texto}"/>'
        else:
            return f'<a href="{url}">{texto}</a>'
            
    text = re.sub(midia, midia_aux, text)

    return text

print(converte(text))
```
### Teste

Para testar o conversor, foi criado um ficheiro `teste.md` com exemplos dos diferentes elementos de Markdown suportados pelo programa. O resultado pode ser apresentado diretamente no terminal ou guardado num ficheiro HTML para ser visualizado num navegador.

Para apresentar o resultado no terminal:

```bash
python3 Conversor.py < teste.md
```

Para guardar o resultado num ficheiro HTML:

```bash
python3 Conversor.py < teste.md > resultado.html
```

O ficheiro `resultado.html` pode depois ser aberto num navegador, permitindo verificar visualmente se os elementos de Markdown foram corretamente convertidos para HTML.
```bash
xdg-open resultado.html
```
## Links 
[Ver código Python](Conversor.py)

[Ver ficheiro de teste](teste.md)

[Ver ficheiro resultado](resultado.html)
