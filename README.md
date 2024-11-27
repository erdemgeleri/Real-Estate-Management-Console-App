# Real Estate Management App

## Description

This is a simple real estate management application developed in Python. It enables users to perform basic CRUD (Create, Read, Update, Delete) operations for managing property records stored in a PostgreSQL database. The application is designed to be beginner-friendly, focusing on simplicity and functionality, making it ideal for small-scale use or as a learning project.

### Key Features:
- 📋 **View All Properties**: Display a list of all registered properties with details such as title, price, number of rooms, and description.
- ➕ **Add a New Property**: Easily input property details like price, status (for sale/rent), and description.
- ✏️ **Update Existing Properties**: Modify any information of an existing property.
- ❌ **Delete Properties**: Remove properties from the database by entering their ID.

This application operates in a **console-based interface** with clear instructions, making it easy to use.

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/real-estate-management.git
2.Install the required library:
  ```bash
  pip install psycopg2
  ```
3.Set up the PostgreSQL database:
-Create a database (e.g., real_estate).
-Run the following SQL command to create the table:
```bash
CREATE TABLE emlak (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    price INTEGER,
    number_of_rooms INTEGER,
    situation VARCHAR(50),
    description TEXT
);
```
4.Configure the database credentials in the code:
-Update the dbname, user, password, and host fields in the psycopg2.connect() function.
5.Run the application:
```bash
python emlak.py
```
## Why Choose This Project?

This project is:

- **Beginner-Friendly**: Perfect for those who want to learn Python and PostgreSQL integration.
- **Well-Documented**: Includes clear setup instructions and usage guidelines.
- **Customizable**: Easily extendable with additional features like property filters or advanced analytics.

---

## Planned Improvements

- 🔍 Add a search feature to filter properties based on criteria.
- 📊 Implement analytics to display property trends and statistics.
- 🌐 Upgrade to a web-based or graphical interface for improved usability.

---

Feel free to fork this repository, make improvements, or report issues. Contributions are always welcome!
