SELECT campaign_name,AVG(cost) AS avg_cost
FROM sales
GROUP BY campaign_name
ORDER BY AVG(cost) ASC
LIMIT 1;