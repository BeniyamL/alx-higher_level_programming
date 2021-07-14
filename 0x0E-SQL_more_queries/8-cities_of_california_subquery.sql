-- sql script to list all the cities of california

SELECT `c`.`id`, `c`.`name` FROM `cities` c
WHERE `c`.`state_id` = 
		(SELECT `s`.`id` FROM `states` s
		WHERE `s`.`name` = 'California');
