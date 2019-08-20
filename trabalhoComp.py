# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:39:25 2018

@author: LUCAS
"""

# Trabalho Compiladores - Analisador Léxico

def main():
    arq = open("codFonte.txt", "r")
    code = arq.read()
    linhas = code.split("\n")
    qntdLinhas = len(linhas)
    i = 0
    listaTokens = []
    qntdTokens = 0
    erros = []
    qntdErros = 0
    palavraValida = True #flag para palavra inválida;
    abriuColchete = False #True quando abriu, False quando fechou
    while i < qntdLinhas:
        j = 0 #j controla os elementos dentro de atual
        atual = linhas[i].split(' ') #atual contém as palavras da linhas atual que está sendo tratada
        if(len(atual) != 1 or atual[0] != ''):
            for w in atual:
                palavraValida = True
                if w == '}':
                    abriuColchete = False
                    continue
                if abriuColchete == True:
                    continue
                if w == '{':
                    abriuColchete = True
                elif w == 'if':
                    listaTokens.append('<IF, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == 'then':
                    listaTokens.append('<THEN, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == 'else':
                    listaTokens.append('<ELSE, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == 'end':
                    listaTokens.append('<END, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == 'repeat':
                    listaTokens.append('<REPEAT, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == 'until':
                    listaTokens.append('<UNTIL, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == 'read':
                    listaTokens.append('<READ, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == 'write':
                    listaTokens.append('<WRITE, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == '+':
                    listaTokens.append('<PLUS, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == '-':
                    listaTokens.append('<MINUS, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == '*':
                    listaTokens.append('<TIMES, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == '/':
                    listaTokens.append('<DIV, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == '=':
                    listaTokens.append('<EQUAL, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == '<':
                    listaTokens.append('<LESS, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == '(':
                    listaTokens.append('<LBRACKET, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == ')':
                    listaTokens.append('<RBRACKET, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == ';':
                    listaTokens.append('<DOTCOMA, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif w == ':=':
                    listaTokens.append('<ATRIB, ')
                    listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                    qntdTokens += 1
                elif ord(w[0]) > 47 and ord(w[0]) < 58:
                    for l in w:
                        if ord(l) <= 47 or ord(l) >= 58:
                            erros.append('Erro linha ')
                            erros[qntdErros] += str(i+1) + ': Número inválido'
                            qntdErros += 1
                            palavraValida = False
                            break
                    if palavraValida:
                        listaTokens.append('<NUM, ')
                        listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                        qntdTokens += 1
                else:
                    for l in w:
                        if(ord(l) <= 47 or ord(l) >= 58 and ord(l) <= 64 or ord(l) >= 91 and ord(l) <= 96 or ord(l) >= 123):
                            erros.append('Erro linha ')
                            erros[qntdErros] += str(i+1) + ': Identificador inválido'
                            qntdErros += 1
                            palavraValida = False
                            break
                    if palavraValida:
                        listaTokens.append('<ID, ')
                        listaTokens[qntdTokens] = listaTokens[qntdTokens] + str(i+1) + '>'
                        qntdTokens += 1
                j += 1
        i += 1
    
    print(listaTokens)
    print(erros)
                
if __name__ == "__main__":
    main()
    