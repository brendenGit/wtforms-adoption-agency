from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/pets/add", methods=['GET','POST'])
def add_pet():
    """a route to add a pet to the adoption agency"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        if form.photo_url.data:
            photo_url = form.photo_url.data
        else:
            photo_url = 'https://shorturl.at/cfkq7'
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, 
                  age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    
    else:
        return render_template("add_pet.html", form=form)
    
@app.route("/pets/view/<int:pet_id>", methods=['GET', 'POST'])
def view_pet(pet_id):
    """view a specific pet details"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        if form.photo_url.data:
            pet.photo_url = form.photo_url.data
        else:
            pet.photo_url = 'https://shorturl.at/cfkq7'
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")

    else:
        return render_template("view_pet.html", pet=pet, form=form)