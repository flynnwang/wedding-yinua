# -*- coding: utf-8 -*-

from bottle import mako_template as template
from app import image_paths
import random

def gen():
    slide_imgs = image_paths('static/images')
    gallery_imgs = image_paths('static/gallery')
    random.shuffle(gallery_imgs)
    return template('index_tmpl.html', **locals())

if __name__ == '__main__':
    open('index.html', 'w').write(gen().encode('utf-8'))
