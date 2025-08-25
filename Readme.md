# Password Manager v2

A simple yet effective password manager tool built with Python that securely stores your passwords along with associated contact information. This is version 2 of the project, upgraded from plain text file storage to a persistent database using Python’s built-in `shelve` module for better data management and reliability.

## Features

- Store multiple password entries for different apps/websites.
- Save associated contact information (email, phone, username).
- Timestamp each password entry with the date and time saved.
- Search passwords by app or website name.
- Display all saved passwords in a readable format.
- Easy-to-use command-line interface with clear options.
- Handles data storage reliably with `shelve` for persistent key-value storage.

---

## Why Version 2?

The original version used plain text files to save passwords, which led to:

- Difficulties in managing and searching data.
- Risk of data corruption during file read/write.
- Limited scalability as the data grew.

This version leverages `shelve` to act like a persistent dictionary, storing app names as keys and lists of password entries as values. This structure makes data retrieval and updates seamless and robust.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/TheGhostAnalyst/password-manager-v2.git
cd password-manager-v2
````

2. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install pyinputplus
```

---

## Usage

Run the script with Python:

```bash
python3 password-manager-v2.py
```

You will be presented with a menu:

1. Save a new password
2. Find likely websites you stored passwords for
3. Show all saved passwords
4. Exit

Follow prompts to add, search, or view password entries.

---

## Code Overview

* **save(app, contact, password)**: Saves password info with timestamp for a given app.
* **search(app)**: Retrieves all saved entries for the specified app.
* **debug\_show\_all()**: Lists all saved passwords for all apps.
* Data is stored persistently in a `shelve` database file named `Manager`.

---

## Future Improvements

* Add encryption to store passwords securely.
* Implement delete/update functionality for entries.
* Build a graphical user interface (GUI) for better usability.
* Explore integration with password generators.
* Migrate to a more advanced database for scalability (e.g., SQLite).

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

---

## License

This project is licensed under the MIT License.

---

## Author

The Ghost Analyst
*Passionate Python developer leveling up one project at a time.*

---

Thank you for checking out Password Manager v2! Stay secure and keep coding. 🚀
