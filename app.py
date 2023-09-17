from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency_db"
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'sage123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()


@app.route("/")
def home():
    """home page - shows all pets"""

    users = User.query.all()
    return render_template("user_list.html", users=users)