# MCP Server and Client

## Requirements

1. Python Version = 3.11.9
2. virtualenv

## Running application

1. Create VirtualEnv
   -> **python -m virtualenv venv**
2. Use VirtualEnv
   -> **source venv/bin/activate**
3. Install dependencies
   -> **python -m pip install -e .**
4. Initialize database
   -> **python init_db.py**
5. Populate database
   -> **python populate_database.py**
6. Run app
   -> **python client.py**
