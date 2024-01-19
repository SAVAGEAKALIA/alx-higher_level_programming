-- Script to print full table description
-- Assuming the script is saved as 5-full_table.sql

-- Set the database to the one passed as an argument
SELECT
    TABLE_NAME AS 'Table',
    CREATE_OPTIONS AS 'Create Table'
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';
