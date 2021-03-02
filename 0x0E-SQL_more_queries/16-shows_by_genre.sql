-- ALL TV SHOWS BY THEIR GENRE 
-- TASK 16
SELECT tv_shows.title, tv_genres.name
FROM tv_shows AS tv_shows
LEFT JOIN tv_show_genres AS tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres AS tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
