SELECT location, SUM(leads) AS total_leads
FROM sales
GROUP BY location
ORDER BY total_leads DESC
LIMIT 1;