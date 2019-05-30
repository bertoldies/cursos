SELECT * FROM [TABELA DE PRODUTOS]

SELECT [NOME DO PRODUTO],
CASE WHEN [PRE�O DE LISTA] >= 12 THEN 'PRODUTO CARO'
WHEN [PRE�O DE LISTA] >= 7 AND [PRE�O DE LISTA] < 12 THEN 'PRODUTO EM CONTA'
ELSE 'PRODUTO BARATO' END
FROM
[TABELA DE PRODUTOS]

SELECT [NOME DO PRODUTO],
CASE WHEN [PRE�O DE LISTA] >= 12 THEN 'PRODUTO CARO'
WHEN [PRE�O DE LISTA] >= 7 AND [PRE�O DE LISTA] < 12 THEN 'PRODUTO EM CONTA'
-- ELSE 'PRODUTO BARATO' END,
--AVG([PRE�O DE LISTA])
end
FROM
[TABELA DE PRODUTOS]
GROUP BY [NOME DO PRODUTO],
CASE WHEN [PRE�O DE LISTA] >= 12 THEN 'PRODUTO CARO'
WHEN [PRE�O DE LISTA] >= 7 AND [PRE�O DE LISTA] < 12 THEN 'PRODUTO EM CONTA'
ELSE 'PRODUTO BARATO' END

SELECT YEAR(DATA), COUNT(*) FROM [NOTAS FISCAIS] GROUP BY YEAR(DATA)

select [NOME],
case 
    when year([DATA DE NASCIMENTO]) < 1990 then 'Adulto'
    when year([DATA DE NASCIMENTO]) between 1990 and 1995 then 'Jovem'
    else 'Crian�a' end as [Classifica��o Et�ria]
 from [TABELA DE CLIENTES]



