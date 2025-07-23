SELECT AVG(cost / clicks) AS avg_cost_per_click
FROM sales
WHERE clicks > 0;