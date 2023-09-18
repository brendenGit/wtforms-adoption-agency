from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, TextAreaField, BooleanField
from wtforms.validators import InputRequired, AnyOf, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    
    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), 
                                                 AnyOf(['cat', 'dog', 'porcupine'],
                                                       message='We only allow dogs, cats, and porcupines for adoption')])
    photo_url = StringField("Picture", validators=[URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30,
                                                      message='Please input a valid age')])
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing pets."""
    
    photo_url = StringField("Picture", validators=[URL()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available", default=True)