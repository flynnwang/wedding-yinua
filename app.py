# -*- coding: utf-8 -*-
"""Usage: app.py [-p=PORT]

-p PORT   listening on this port [default: 8000]
"""
import os
#import sys
import random
from docopt import docopt
from bottle import Bottle, mako_template as template, static_file

app = Bottle()

def image_paths(dir):
    imgs = [(dir + '/' + img) for img in os.listdir(dir) if img.endswith('jpg')]
    #random.shuffle(imgs)
    return imgs

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.path.join(os.path.dirname(__file__), 'static'))

@app.route('/')
def index():
    slide_imgs = image_paths('static/images')
    gallery_imgs = image_paths('static/gallery')
    return template('index_tmpl.html', **locals())

if __name__ == '__main__':
    arguments = docopt(__doc__)
    port = arguments['-p']
    app.run(host='0.0.0.0', port=port, reloader=True, debug=True)
