#!/usr/bin/env python3

import json
import shutil
from flask import Flask, make_response, request, send_file
from flask_cors import CORS, cross_origin
import random

from file_list_generator import *

app = Flask(__name__)
CORS(app)

app.config['CORS_EXPOSE_HEADERS'] = ['Content-Disposition']

jpgs = None
cfgFile = "./config.json"
f = open(cfgFile)
config = json.load(f)
f.close()
all_files = config['all_files']
approved_folder = config['approved_files']
denied_folder = config['denied_files']
local_ip = config['local_ip']
src = all_files

@app.route('/random_image', methods = ['GET'])
@cross_origin(allow_headers=['Content-Disposition'])
def random_image():
   if request.method == 'GET':
      filename = random.choice(jpgs)
      filepath = src + filename
      resp = send_file(filepath, mimetype='jpeg')
      return resp

@app.route('/approved', methods = ['PUT'])
def approved():
   if request.method == 'PUT':
      filename = request.json['filename'][1:-1]
      filepath = all_files + filename
      newFilepath = approved_folder + filename
      shutil.move(filepath, newFilepath)
      resp = make_response({'status': 'ok'}, 200)
      return resp

@app.route('/denied', methods = ['PUT'])
def denied():
   if request.method == 'PUT':
      filename = request.json['filename'][1:-1]
      filepath = all_files + filename
      newFilepath = denied_folder + filename
      shutil.move(filepath, newFilepath)
      resp = make_response({'status': 'ok'}, 200)
      return resp

if(__name__ == '__main__'):
   jpgs = init_jpg_list(init_file_list())
   app.run(host=local_ip, port=5000)
