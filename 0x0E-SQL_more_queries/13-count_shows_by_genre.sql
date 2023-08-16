-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
SELECT tvg.name AS genre, COUNT(tvg.name) AS number_of_shows
FROM tv_show_genres AS tvsg
JOIN tv_shows AS tvs
ON tvsg.show_id=tvs.id
JOIN tv_genres AS tvg
ON tvsg.genre_id=tvg.id
GROUP BY tvg.name
ORDER BY number_of_shows DESC;
