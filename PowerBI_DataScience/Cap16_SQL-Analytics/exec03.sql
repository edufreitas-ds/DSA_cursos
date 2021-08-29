/* Retorne a média de salário por estado. */

SELECT ROUND(AVG(F.salario_hora)), E.estado
FROM cap16."TB_FUNC" F, cap16."TB_ENDERECO" E
WHERE F.id = E.id_func
GROUP BY E.estado
