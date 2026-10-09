import sys 
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<COM>\#.*)|(?P<VAR>\?\w+)|(?P<LING>@[A-Za-z]{2})|(?P<STRING>\"[^"]*\")|(?P<CONCEITOS>[\w:]+)|(?P<DELIMITER>[{}\.])|(?P<LIMIT>LIMIT\b)|(?P<INT>\d+)|(?P<SKIP>[ \t]+)|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['COM']:
            t = ("COM", dic['COM'], linha, m.span())

        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
    
        elif dic['LING']:
            t = ("LING", dic['LING'], linha, m.span())
    
        elif dic['STRING']:
            
            t = ("STRING", dic['STRING'], linha, m.span())
    
        elif dic['CONCEITOS']:
            
            t = ("CONCEITOS", dic['CONCEITOS'], linha, m.span())
    
        elif dic['DELIMITER']:
            
            t = ("DELIMITER", dic['DELIMITER'], linha, m.span())
    
        elif dic['LIMIT']:
            
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['INT']:
            
            t = ("INT", dic['INT'], linha, m.span())
    
        elif dic['SKIP']:
            
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
            linha+=1
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)

    return reconhecidos

for tok in tokenize(sys.stdin.read()):
    print(tok)
