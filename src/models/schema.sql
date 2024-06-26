-- Create User table
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

-- Create Place table
CREATE TABLE IF NOT EXISTS Place (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    host_id INTEGER,
    price INTEGER NOT NULL,
    FOREIGN KEY (host_id) REFERENCES User (id)
);

-- Create Review table
CREATE TABLE IF NOT EXISTS Review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text VARCHAR NOT NULL,
    place_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (place_id) REFERENCES Place (id),
    FOREIGN KEY (user_id) REFERENCES User (id)
);

-- Create Country table
CREATE TABLE IF NOT EXISTS Country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL
);

-- Create City table
CREATE TABLE IF NOT EXISTS City (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES Country (id)
);

-- Create Amenity table
CREATE TABLE IF NOT EXISTS Amenity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL
);

-- Create PlaceAmenity table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS PlaceAmenity (
    place_id INTEGER,
    amenity_id INTEGER,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place (id),
    FOREIGN KEY (amenity_id) REFERENCES Amenity (id)
);