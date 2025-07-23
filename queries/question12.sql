SELECT keyword, SUM(leads) AS total_leads
FROM sales
GROUP BY keyword
ORDER BY total_leads DESC
LIMIT 1;