SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
JOIN tv_show_genres AS tvsg
ON tvs.id=tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id;
