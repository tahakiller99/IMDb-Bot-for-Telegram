# IMDb-Bot-for-Telegram

## Overview

The Bot is a Telegram bot that allows users to search for movie information using the OMDB API. Users can either input a movie name to get details or provide the IMDb ID directly. Additionally, the bot features a section dedicated to displaying the IMDb Top 250 movies.

## Features

- **Search by Movie Name:** Users can use the `/search` command to get a movie to find relevant information.
- **Search by IMDb ID:** Users can provide the IMDb ID of a movie to get details directly.
- **IMDb Top 250 Movies:** Explore the list of the top-rated movies on IMDb using the `/top250` command.
- **Key Movie Information:** The bot provides details such as title, year, genre, plot, and ratings.
- **User-friendly Interaction:** Simple and intuitive commands for a smooth user experience.

## IMDb Top 250 Movies

Browse the curated list of the top-rated movies on IMDb using the `/top250` command.

## Code Files

In the code repository, you will find the following important files:

- **Top250.json:** This file is utilized for creating the `/top250` command section. It contains information about the IMDb Top 250 movies, including their titles, years, and IMDb IDs. The bot reads this file to provide users with a curated list of top-rated movies.

Feel free to explore these files if you are interested in the internal workings of the Bot application.

## Installation

To run the bot locally, follow these steps:

1. Clone the repository: `git clone [repository URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Obtain an API key from OMDB API (https://www.omdbapi.com/) and update the configuration.
4. Run the bot: `python bot.py`

## Configuration

- `API_KEY`: Your OMDB API key. Obtain it from https://www.omdbapi.com/.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to OMDB for providing the movie database API.
