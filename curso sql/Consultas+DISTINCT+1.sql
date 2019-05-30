SELECT EMBALAGEM, TAMANHO FROM [TABELA DE PRODUTOS]

SELECT DISTINCT EMBALAGEM, TAMANHO FROM [TABELA DE PRODUTOS]

SELECT DISTINCT EMBALAGEM, TAMANHO FROM [TABELA DE PRODUTOS] WHERE
[SABOR] = 'Laranja'

SELECT DISTINCT EMBALAGEM, TAMANHO, SABOR FROM [TABELA DE PRODUTOS]


SELECT  * FROM [NOTAS FISCAIS] WHERE DATA = '2017-01-01' 

SELECT * FROM [ITENS NOTAS FISCAIS]
SELECT * FROM [TABELA DE PRODUTOS]

SELECT [NOME DO PRODUTO], [ITENS NOTAS FISCAIS].* FROM [TABELA DE PRODUTOS]
JOIN [ITENS NOTAS FISCAIS] ON [TABELA DE PRODUTOS].[CODIGO DO PRODUTO] = [ITENS NOTAS FISCAIS].[CODIGO DO PRODUTO]
WHERE [NOME DO PRODUTO] = 'Linha Refrescante - 1 Litro - Morango/Lim�o'
ORDER BY QUANTIDADE DESC