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
    
    #Criando matriz de string
    tabela = [['', 'A', '', '', '', 'A', '', 'A', '', 'A', 'A', '', '', '', '', '', '', '', '', '', ''],
            ['', 'B.V', '', '', '', 'B.V', '', 'B.V', '', 'B.V', 'B.V', '', '', '', '', '', '', '', '', '', ''],
            ['a.B.V', 'a.B.V', '', '$', '$', '', '$', '', '', '', '', '', '', '', '', '', '', '', '', '', '$'],
            ['', 'C', '', '', '', 'D', '', 'E', '', 'F', 'G', '', '', '', '', '', '', '', '', '', ''],
            ['', 'b.H.c.A.X', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '$', '', 'd.A.E', '$', '', '$', '', '', '', '', '', '', '', '', '', '', '', '', '', '$'],
            ['', '', '', '', '', 'f.A.g.H', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'i.j.H', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', 'r.i', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', 'w.H', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'I.W', '', '', '', '', '', '', '', '', '', 'I.W', '', 'I.W', ''],
            ['$', '', '$', '$', '$', '', '$', '', '', '', '', 'J.I', 'J.I', '', '', '', '', '', '$', '', '$'],
            ['', '', '', '', '', '', '', '', '', '', '', '<', '=', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'L.Y', '', '', '', '', '', '', '', '', '', 'L.Y', '', 'L.Y', ''],
            ['$', '', '$', '$', '$', '', '$', '', '', '', '', '$', '$', 'K.L.Y', 'K.L.Y', '', '', '', '$', '', '$'],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '+', '-', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'N.Z', '', '', '', '', '', '', '', '', '', 'N.Z', '', 'N.Z', ''],
            ['$', '', '$', '$', '$', '', '$', '', '', '', '', '$', '$', '$', '$', 'M.N.Z', 'M.N.Z', '', '$', '', '$'],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '*', '/', '', '', '', ''],
            ['', '', '', '', '', '', '', 'i', '', '', '', '', '', '', '', '', '', '(.H.)', '', 'n', '']]
    
    #Função Análise Sintática Preditiva
    #Cabeçote = p -> pointer
    
    #Declaração de listas necessárias no código
    variaveis = ['S', 'A', 'V', 'B', 'C', 'X', 'D', 'E', 'F', 'G', 'H', 'W', 'J', 'I', 'Y',
                 'K', 'L', 'Z', 'M', 'N']
    
    terminais = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'r', 'w', '<', '=', '+', '-',
                 '*', '/', '(', ')', 'n']
    
    #Função corresponde() para substituição dos tokens pelos terminais da tabela
    def corresponde(p):
        x = p.split(',')
        if x[0] == '<IF':
            return 'b'
        elif x[0] == '<THEN':
            return 'c'
        elif x[0] == '<ELSE':
            return 'd'
        elif x[0] == '<END':
            return 'e'
        elif x[0] == '<REPEAT':
            return 'f'
        elif x[0] == '<UNTIL':
            return 'g'
        elif x[0] == '<READ':
            return 'r'
        elif x[0] == '<WRITE':
            return 'w'
        elif x[0] == '<PLUS':
            return '+'
        elif x[0] == '<MINUS':
            return '-'
        elif x[0] == '<TIMES':
            return '*'
        elif x[0] == '<DIV':
            return '/'
        elif x[0] == '<EQUAL':
            return '='
        elif x[0] == '<LESS':
            return '<'
        elif x[0] == '<LBRACKET':
            return '('
        elif x[0] == 'RBRACKET':
            return ')'
        elif x[0] == '<DOTCOMA':
            return 'a'
        elif x[0] == '<ATRIB':
            return 'j'
        elif x[0] == '<NUM':
            return 'n'
        elif x[0] == '<ID':
            return 'i'        
            
    pilha = ['$', 'S']
    X = pilha.pop()
    p = 0 #variável que percorre a fita de entrada p -> [0; qntdTokens]
    while X != '$':
        a = corresponde(listaTokens[p])
        if X in terminais: #se X é um terminal
            if X == a:
                p = p+1
            else:
                print('ERRO')
        else: #X é uma variável
            if tabela[variaveis.index(X)][terminais.index(a)] == '$':
                print('Epsilon')
            elif tabela[variaveis.index(X)][terminais.index(a)] != '':
                producao = tabela[variaveis.index(X)][terminais.index(a)].split('.')
                print(producao)
                while not not producao:
                    pilha.append(producao.pop())
            else:
                print('ERRO, prod vazia')
        X = pilha.pop()
        if p == qntdTokens - 1:
            break
                
            
        
                
if __name__ == "__main__":
    main()
    