# HazenTTElo
An [Elo](https://en.wikipedia.org/wiki/Elo_rating_system) ranking system for the [Hazen Table Tennis Club](https://www.facebook.com/groups/HazenTT/) using [this](https://github.com/HankSheehan/EloPy) Python library.

Provides an interface for the EloPy library and an excel spreadsheet for tracking matches.

<strong>WORK IN PROGRESS</strong>

# Usage
Record matches in an [Excel spreadsheet](Log.xlsx) (.xlsx file extension) and pass it to the calculate method.
The first row must be a header. The columns should be: date, player 1, player 1 score, player 2, player 2 score.
Matches are read top to bottom so record the most recent matches at the bottom.
Names must match exactly with previous entries. For consistency, use the first and last names as written on school ID.

# View rankings
