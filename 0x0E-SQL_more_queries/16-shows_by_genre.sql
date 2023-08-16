-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
SELECT tvs.title, tvg.name
FROM tv_shows as tvs
LEFT JOIN tv_show_genres AS tvsg
ON tvs.id = tvsg.show_id
LEFT JOIN tv_genres AS tvg
ON tvg.id=tvsg.genre_id
ORDER BY tvs.title, tvg.name;
