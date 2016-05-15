--
-- File generated with SQLiteStudio v3.0.7 on Sat May 14 21:45:19 2016
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: weather
CREATE TABLE weather (date_time DATETIME PRIMARY KEY UNIQUE DEFAULT (NOW()), temperature INTEGER DEFAULT (0), icon STRING DEFAULT ('clear-day'), precipitation INTEGER DEFAULT (0), city_name STRING DEFAULT ('Warszawa'));

-- Table: water_supply
CREATE TABLE water_supply (date_time DATETIME UNIQUE DEFAULT (NOW()), level INTEGER);

-- Table: moisture_level
CREATE TABLE moisture_level (sensor_id INTEGER, date_time DATETIME DEFAULT (NOW()), city_name STRING DEFAULT ('Warszawa'), level INTEGER DEFAULT (0));

-- Index: water_level_measurement
CREATE INDEX water_level_measurement ON water_supply (date_time, level);

-- Index: moisture_level_measurement
CREATE UNIQUE INDEX moisture_level_measurement ON moisture_level (sensor_id, date_time DESC);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
