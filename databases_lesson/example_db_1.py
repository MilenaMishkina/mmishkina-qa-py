import pyodbc

connection = pyodbc.connect(
    'DRIVER={SQLite3};'
    'DATABASE=db.sqlite'
)