SELECT COUNT(*) AS ads_above_avg_cost
FROM sales
WHERE cost > (SELECT AVG(cost) FROM sales)