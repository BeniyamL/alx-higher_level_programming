-- sql script that displays average temperatere by city 
-- order by temperature in desending order

SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`
GROUP BY `city` ORDER BY `avg_temp` DESC;
