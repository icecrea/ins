# -*- encoding=UTF-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os
app=Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
#flask_login部分
login_manager=LoginManager(app)
#没有登录的情况下点击图片访问不到 会进入这个页面
login_manager.login_view='/regloginpage/'
mail=Mail(app)

app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')
app.config.from_pyfile('app.conf')
app.secret_key='icecrea'
db=SQLAlchemy(app)

from ins import views,models


