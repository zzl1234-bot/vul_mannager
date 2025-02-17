#!coding=utf-8
import time
from hashlib import md5

from playhouse.shortcuts import model_to_dict

from tornadoweb import *
from logic.model import *
from logic.utility import LoginedRequestHandler
#add by wuq
from PIL import Image
# 可以想文件一样使用, 只是存放在内存
from io import StringIO,BytesIO

@url(r"/image/upload", needcheck = False, category = "图片")
class ImageAdd(LoginedRequestHandler):
    """
        图片上传

        images: 文件
    """
    def post(self):
        img = self.request.files['image'][0]
        filename = img.get('filename')

        if filename.split(".")[-1].lower() not in ["jpg", "png", "jpeg"]:
            self.write(dict(status = False, msg = "图片格式错误"))
            return

        body = img.get('body')
        body_md5 = md5(body).hexdigest()

        new_filename = "{}.{}".format(body_md5, filename.split(".")[-1])
        path = "{}/images/{}".format(__conf__.STATIC_DIR_NAME, new_filename)

        with open(path, "wb") as f:

            #add by wuq  控制图片宽度大小
            # image有多种打开方式，一种是 Image.open('xx.png')
            # 另一种就是 Image.open(StringIO(buffer)) 
            im = Image.open(BytesIO(body))
            # 修改图片大小resize接受两个参数, 第一个是宽高的元组数据,第二个是对图片细节的处理，本文表示抗锯齿
            #先不修改了，图片失真厉害，by wuq 
            #im = im.resize((500, round(im.height*500/im.width)), Image.ANTIALIAS)
            # 打开io 就像文件一样
            im_file = BytesIO()
            im.save(im_file, format='png')
            # 这是获取io中的内容
            im_data = im_file.getvalue() 
            f.write(im_data)

        self.write(dict(status = True, path = "{}/images/{}".format(__conf__.STATIC_DIR_NAME, new_filename)))

@url(r"/paper/cover", needcheck = False, category = "图片")
class ImageArticleCover(LoginedRequestHandler):
    """
        文章封面上传

        images: 文件
    """
    def post(self):
        img = self.request.files['file'][0]
        filename = img.get('filename')

        if filename.split(".")[-1].lower() not in ["jpg", "png", "jpeg"]:
            self.write(dict(status = False, msg = "图片格式错误"))
            return

        body = img.get('body')
        body_md5 = md5(body).hexdigest()

        new_filename = "{}.{}".format(body_md5, filename.split(".")[-1])
        path = "{}/images/{}".format(__conf__.STATIC_DIR_NAME, new_filename)

        with open(path, "wb") as f:
            f.write(body)

        self.write(dict(status = True, path = "{}/images/{}".format(__conf__.STATIC_DIR_NAME, new_filename)))

@url(r"/avatar/upload", needcheck = False, category = "图片")
class ImageAvatarUpload(LoginedRequestHandler):
    """
        头像上传

        file: 文件
    """
    def post(self):
        img = self.request.files['file'][0]
        filename = img.get('filename')

        if filename.split(".")[-1].lower() not in ["jpg", "png", "jpeg"]:
            self.write(dict(status = False, msg = "图片格式错误"))
            return

        body = img.get('body')
        body_md5 = md5(body).hexdigest()

        new_filename = "{}.{}".format(body_md5, filename.split(".")[-1])
        path = "{}/images/avatar/{}".format(__conf__.STATIC_DIR_NAME, new_filename)

        with open(path, "wb") as f:
            f.write(body)

        self.write(dict(status = True, path = "{}/images/avatar/{}".format(__conf__.STATIC_DIR_NAME, new_filename)))



