import re
import sys
text = sys.stdin.read()
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