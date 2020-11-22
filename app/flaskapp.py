#!/usr/bin/env python
from flask import Flask
from redis import Redis, RedisError

import os
import socket
redis = Redis(host="redis-server", db=0, socket_connect_timeout=10, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hey World</h1>"

@app.route("/visit")
def hello():
	try:
		visits = redis.incr("counter")
	except RedisError:
		visits = "<i>cannot connect to Redis server to count</i>"
	html = "<h3>Hello World!</h3>\n" \
		   "<b>Hostname:</b> {hostname}<br/>\n" \
		   "<b>Visits:</b> {visits}\n"
	return html.format(hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)








# docker run --name myredisdb -d redis
# docker run --name flaskapap -P --link myredisdb:redis-server 8eb22f5deaf8
