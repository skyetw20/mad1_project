# Project Overview

## Description

The project is a simple ticket booking app that allows registered users to book tickets for shows and movies, and also allows them to reserve venues. The app enables users to sort and filter movies and shows based on rating, genre, and city. APIs provide data for further app integrations to advanced users.

## Technologies Used

- **Flask (2.2.3)**: A micro web framework written in Python used to build the web application.
- **SQLAlchemy (2.0.9)**: A Python SQL toolkit and ORM that provides a set of high-level APIs for connecting to SQL databases.
- **Jinja2 (3.1.2)**: A modern and designer-friendly templating language for Python, used to generate dynamic HTML templates in the Flask application.
- **Werkzeug (2.2.3)**: A Python utility library for building web applications, used in Flask as a toolkit for HTTP requests handling.
- **itsdangerous (2.1.2)**: A Python library that provides various ways to generate and verify cryptographically signed tokens, used in Flask for generating secure cookies.

The purpose behind using Flask is to build a web application that can handle HTTP requests and responses. SQLAlchemy is used to provide a high-level API for connecting to SQL databases, allowing the application to store and retrieve data efficiently. Jinja2 is used to generate dynamic HTML templates for the web application, while Werkzeug is used to handle HTTP requests and responses. itsdangerous is used to generate secure cookies for user authentication.

## DB Schema Design

The database consists of the following tables:

1. **admins**: Stores the credentials of the admins
   - Fields: id, uname, password

2. **bookings_movies**: Stores bookings for movies.
   - Fields: id, movie_id, date, theater_id, amount, seats, user_id, time

3. **bookings_shows**: Stores bookings for shows.
   - Fields: id, show_id, date, theater_id, amount, seats, user_id, time

4. **bookings_venues**: Stores bookings of venues.
   - Fields: id, theater_id, date, amount, seats, user_id, time, duration

5. **movies**: Stores available movies.
   - Fields: id, name, desc, rating, date, theaters, tags, filename

6. **shows**: Stores available shows.
   - Fields: id, name, rating, tags, duration, about, theaters, filename

7. **theaters**: Stores available venues for booking.
   - Fields: id, name, place, filename, capacity, rph, rating, capacity_pre, base_price

8. **users**: Stores information about users.
   - Fields: id, name, email, password, mobile

The database design facilitates easy retrieval of information and logical organization of data. Tables are designed to minimize data redundancy and enhance data integrity.

## API Design

The implemented API is a REST API using OpenAPI 3.0.0, providing three paths for different resources: movies, shows, and venues. Each path has a GET method to retrieve data related to that resource. The API returns JSON files containing details of the movies, shows, and theaters. The responses include HTTP status codes, and the OK response has a JSON object with the requested data. The API requires the header parameter `Flag: json` to be set for receiving JSON files in response. Additionally, there is a 400-status code response for Curl requests without headers.

## Architecture and Features

The main application logic is in the "application" subdirectory, containing the "models.py" and "views.py" files for defining data models and handling HTTP requests, respectively. The "__init__.py" file initializes the Flask app and connects it to the database file "ticket_show.db". The "static" subdirectory contains various static files, such as images and CSS stylesheets used in the templates. The "templates" subdirectory contains all HTML templates rendering different pages of the application.

The application provides a user-friendly interface for signing up, signing in, booking movie and show tickets, and reserving venues. While signing in is required for certain actions, users can browse movies, shows, and venues without logging in.

The application offers sorting and filtering options based on ratings, genres, and cities to help users quickly find the right movie, show, or venue that matches their preferences.

For admins, the application offers a powerful dashboard displaying key statistics on bookings, such as occupancy rates and revenue. Admins can manage the content by adding, updating, or deleting movies, shows, and venues with just a few clicks.

## Video

[Project Overview Video](https://drive.google.com/file/d/1NptR_AlR8gf1nehfGXbeESIK3YXsJqEM/view?usp=sharing)
