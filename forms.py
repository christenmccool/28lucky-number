from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, Length, AnyOf, ValidationError, NumberRange

colors = ['red', 'green', 'orange', 'blue']
illegal_characters = ['<', '>', '{', '}', '[', ']', '(', ')']

def contains_character(str, characters):
    for char in str:
        if char in characters:
            return True
    return False

def illegal_character_check(form, field):
    if contains_character(field.data, illegal_characters):
        raise ValidationError('Field must be less than 50 characters')

def character_check():
    if len(field.data) > 50:
        raise ValidationError(f"Special characters {(' ').join(illegal_characters)} not allowed in username.")

class NumForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(6, 20), illegal_character_check])
    email = StringField(validators=[InputRequired(), Email(), Length(6, 30), illegal_character_check])
    year = IntegerField(validators=[InputRequired(), NumberRange(1900,2000)])
    color = StringField(validators=[InputRequired(), AnyOf(colors)])
