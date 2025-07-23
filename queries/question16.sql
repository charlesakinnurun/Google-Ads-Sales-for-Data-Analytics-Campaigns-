SELECT location,avg(sale_amount)
FROM sales
GROUP BY location
ORDER BY avg(sale_amount) DESC
LIMIT 1;