import sys
from flask import render_template, redirect, url_for, request, abort

from models.AuditRequest import AuditRequest

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    ...

def store():
    ...

def show(userId):
    ...

def update(userId):
    ...

def destroy(userId):
    ...