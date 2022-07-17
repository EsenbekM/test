PYTHON 4 MONTH

Домашнее задание 1.

Создать django проект (afisha_api) с одним приложением. Будут 4 модели:

Cinema
name

Movie
title
description
cinema(ForeignKey)
genres(ManyToManyField)

Review
text
movie(ForeignKey)

Genre
name

Вывести список Фильмов /api/v1/movies/
Вывести фильм /api/v1/movies/<int:id>/
