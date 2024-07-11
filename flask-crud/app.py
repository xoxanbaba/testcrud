from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import EntryForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)

# Models
from models import Entry, User

# Routes
@app.route('/')
def index():
    entries = Entry.query.paginate(per_page=10)
    stats = {
        'total': Entry.query.count(),
        'active': Entry.query.filter_by(status='aktiv').count(),
        'reserve': Entry.query.filter_by(status='rezerv').count(),
        'empty': Entry.query.filter_by(status='boş').count()
    }
    search = request.args.get('search', '')
    return render_template('index.html', entries=entries, stats=stats, search=search)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if username and password are correct (example)
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            flash('Daxil oldunuz!', 'success')
            return redirect(url_for('index'))
        else:
            flash('İstifadəçi adı və ya şifrə yanlışdır.', 'danger')

    return render_template('login.html', form=form)

@app.route('/add_edit', methods=['GET', 'POST'])
def add_edit():
    form = EntryForm()
    if form.validate_on_submit():
        # Əlavə ediləcək işlər burada yer alacaq
        flash('Məlumat əlavə edildi/düzəldildi.', 'success')
        return redirect(url_for('index'))
    
    # Əgər POST metod deyilsə, səhifəni yüklə
    return render_template('add_edit.html', form=form)

# Initialize database and run app
if __name__ == '__main__':
    app.run(debug=True)
