from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///STORE-FEEDBACK.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/our_users'
app.config['SECRET_KEY'] = "123456"

db = SQLAlchemy(app)
#資料庫-----------------------------------------------------------------------------------------------------------------------------------------
#早餐好樂評論資料庫------------------------------------------>
class Htbfs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#找午餐評論資料庫-------------------------------------------->
class Seeks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#阿嫂赤肉羹評論資料庫-------------------------------------------->
class Yshs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#古記燒臘評論資料庫-------------------------------------------->
class Gos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#牛媽媽牛肉麵評論資料庫-------------------------------------------->
class Cows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#一茶園評論資料庫-------------------------------------------->
class Oneteas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#嘗湘麻辣燙評論資料庫-------------------------------------------->
class Tshs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#穎素齋評論資料庫-------------------------------------------->
class Inss(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#野川堂秘境鍋物評論資料庫-------------------------------------------->
class Yas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name
#Flask-what-the-form-------------------------------------->
class UserForm(FlaskForm):
    name = StringField("稱呼", validators=[DataRequired()])
    email = StringField("評論", validators=[DataRequired()])
    submit = SubmitField("送出")

#main.route------------------------------------------------------------------------------------------------------------------------------------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/breaks')
def breaks():
    return render_template('breaks.html')

@app.route('/lunch')
def lunch():
    return render_template('lunch.html')

@app.route('/dinner')
def dinner():
    return render_template('dinner.html')

@app.route('/dssert')
def dessert():
    return render_template('dessert.html')
@app.route('/drink')
def drink():
    return render_template('drink.html')

@app.route('/about')
def help():
    return render_template('about.html')

@app.route('/food')
def food():
    return render_template('food.html')

#store.route------------------------------------------------------------------------------------------------------------------------------------
#早餐好樂-------------------------------------------->
@app.route('/how-the-breakfast', methods=['GET','POST'])
def htbf():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Htbfs.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Htbfs(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Htbfs.query.order_by(Htbfs.date_added)
    return render_template('store/how-the-breakfast.html', form=form, name=name, our_users=our_users)
#找午餐-------------------------------------------->
@app.route('/seek', methods=['GET','POST'])
def seek():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Seeks.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Seeks(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Seeks.query.order_by(Seeks.date_added)
    return render_template('store/seek.html', form=form, name=name, our_users=our_users)
#阿嫂赤肉羹-------------------------------------------->
@app.route('/ysh', methods=['GET','POST'])
def ysh():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Yshs.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Yshs(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Yshs.query.order_by(Yshs.date_added)
    return render_template('store/ysh.html', form=form, name=name, our_users=our_users)
#古記燒臘-------------------------------------------->
@app.route('/go', methods=['GET','POST'])
def go():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Gos.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Gos(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Gos.query.order_by(Gos.date_added)
    return render_template('store/go.html', form=form, name=name, our_users=our_users)
#牛媽媽牛肉麵-------------------------------------------->
@app.route('/cow', methods=['GET','POST'])
def cow():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Cows.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Cows(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Cows.query.order_by(Cows.date_added)
    return render_template('store/cow.html', form=form, name=name, our_users=our_users)
#一茶園-------------------------------------------->
@app.route('/onetea', methods=['GET','POST'])
def onetea():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Oneteas.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Oneteas(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Oneteas.query.order_by(Oneteas.date_added)
    return render_template('store/onetea.html', form=form, name=name, our_users=our_users)
#嘗湘麻辣燙-------------------------------------------->
@app.route('/tsh', methods=['GET','POST'])
def tsh():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Tshs.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Tshs(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Tshs.query.order_by(Tshs.date_added)
    return render_template('store/tsh.html', form=form, name=name, our_users=our_users)
#穎素齋-------------------------------------------->
@app.route('/ins', methods=['GET','POST'])
def ins():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Inss.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Inss(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Inss.query.order_by(Inss.date_added)
    return render_template('store/ins.html', form=form, name=name, our_users=our_users)
#野川堂秘境鍋物-------------------------------------------->
@app.route('/ya', methods=['GET','POST'])
def ya():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Yas.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Yas(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
    our_users = Yas.query.order_by(Yas.date_added)
    return render_template('store/ya.html', form=form, name=name, our_users=our_users)
#kind.route------------------------------------------------------------------------------------------------------------------------------------
@app.route('/rice')
def rice():
    return render_template('kind/rice.html')

@app.route('/noodle')
def noodle():
    return render_template('kind/noodle.html')

@app.route('/sweet')
def sweet():
    return render_template('kind/sweet.html')
#run--------------------------------------------------------------------------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(i):
    return render_template('500.html'), 500

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
