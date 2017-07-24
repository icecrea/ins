# -*- encoding=UTF-8 -*-

from ins import app,db
from flask_script import Manager
from ins.models import User,Image,Comment
import random

manager= Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'
   #return 'http://lorempixel.com/600/' + str(random.randint(500, 700)) + '/'


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+str(i+1),'a'+str(i+1)))
        for j in range(0,3):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('this is a comment'+str(k),1+3*i+j,i+1))
    db.session.commit()

    for i in range(50,100,2):
        user=User.query.get(i)
        user.username='[New1]'+user.username

    User.query.filter_by(id=51).update({'username':'[new2]'})
    db.session.commit()

    for i in range(50,100,2):
        comment=Comment.query.get(i+1)
        db.session.delete(comment)
    db.session.commit()

    # print(1,User.query.all())
    # print(2, User.query.get(3))
    # print(3,User.query.filter_by(id=5).first())
    # print(4,User.query.order_by(User.id.desc()).offset(1).limit(2).all())
    # #orm
    # print(5,User.query.get(1).images)
    # print(6,Image.query.get(1).user)
    # print(7,Image.query.order_by(Image.id.desc()).limit(10).all())

if __name__=='__main__':
    manager.run()