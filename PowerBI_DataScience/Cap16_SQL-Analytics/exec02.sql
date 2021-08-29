/*Retorne todos os registros dos funcionários com dois filhos */
SELECT * FROM cap16."TB_FUNC" WHERE numero_filhos = CAST('2' AS VARCHAR)