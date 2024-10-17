# Use the official MySQL image
FROM mysql:9.0

# Copy the SQL script to initialize the database
COPY database.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306
