SELECT campaign_name, SUM(sale_amount) AS total_sales
FROM sales
GROUP BY campaign_name
ORDER BY total_sales DESC
LIMIT 1;