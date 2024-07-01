DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS amenity;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(128) NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE place (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128) NOT NULL,
    city_id INTEGER,
    FOREIGN KEY(city_id) REFERENCES city(id)
);

CREATE TABLE review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    place_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY(place_id) REFERENCES place(id),
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE amenity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE city (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128) NOT NULL,
    country_id INTEGER,
    FOREIGN KEY(country_id) REFERENCES country(id)
);

CREATE TABLE country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128) NOT NULL
);