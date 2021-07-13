-- sql script that lists all shows contained in hbtn_0d_tvshows

SELECT `s`.`title`, `g`.`genre_id` FROM `tv_show_genres` `g`
INNER JOIN `tv_shows` `s` ON `s`.`id` = `g`.`show_id`
ORDER BY `s`.`title`, `g`.`genre_id` ASC;
