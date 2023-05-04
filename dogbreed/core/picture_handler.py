#users/picture_handler.py

import os
from PIL import Image
from datetime import datetime
from flask import url_for,current_app

def add_profile_pic(pic_upload):

    filename = pic_upload.filename
    # "mypicture.jpg"
    ext_type = filename.split('.')[-1]
    # "username.jpg"
    storage_filename = datetime.now().strftime('%m%d%Y%H%M%S') +'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static\dog_pics',storage_filename)

    output_size = (200,200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
