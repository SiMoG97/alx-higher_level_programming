--
SELECT tvg.name
FROM tv_show_genres AS tvgs
JOIN tv_shows AS tvs
ON tvgs.show_id=tvs.id
JOIN tv_genres AS tvg
ON tvgs.genre_id=tvg.id
WHERE tvs.title="Dexter"
ORDER BY tvg.name;
