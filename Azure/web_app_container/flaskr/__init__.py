# __init__.pyはサーバ起動時に実行される
from flask import Flask
app = Flask(__name__)
import flaskr.main

from flaskr import db
db.create_books_table()