-- sql script that list all cities container in the database

SELECT `c`.`id`, `c`.`name`, `s`.`name` FROM `cities` c
INNER JOIN `states` s on `s`.`id` = `c`.`state_id`
ORDER BY `c`.`id` ASC;
