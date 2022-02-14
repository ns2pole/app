#!/home/ns2pole/.pyenv/versions/3.6.6-flask/bin/python
from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)
