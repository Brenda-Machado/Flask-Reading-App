"""
My Books App - CS50 Final Project

Author: Brenda S. M.

app.py
"""

from flask import Flask, render_template, request, redirect, url_for, g
import os
import sqlite3

APP = Flask(__name__)
DATABASE = os.path.join(APP.instance_path, "library.db")

# Database Funcitions

def get_database():
    if "db" not in g: #  simple namespace object that has the same lifetime as an application context.
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
