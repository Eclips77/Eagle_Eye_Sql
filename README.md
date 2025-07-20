# Eagle Eye SQL

Eagle Eye SQL is a simple Python application for managing a list of agents
stored in a MySQL database. The project provides two user interfaces:

* **ConsoleUI** – a command line menu.
* **TkUI** – a basic Tkinter GUI.

Both interfaces allow you to add, update, delete and view agents.

## Requirements

- Python 3.8+
- [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/)
- A running MySQL server with a database named `eagleeyedb` and a table
  `agents` that matches the expected schema.

## Running the app

The default UI is the console menu:

```bash
python main.py
```

To start the Tkinter UI pass `use_tk=True` to `run()` in `main.py` or modify
the code accordingly.

Database connection parameters are configured in
`Dal/agent_dal.py`.

## Features

- Add a new agent
- Update existing agents
- Delete agents by ID
- Find a specific agent by ID
- View all agents (IDs are displayed so they can be referenced later)

## Notes

This project is a minimal example and does not include migrations or input
validation beyond the basics. Ensure your MySQL server is running and the
connection parameters are correct before launching the application.
