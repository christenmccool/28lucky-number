from flask import Flask, render_template, jsonify, request
import requests
from random import randint
from forms import NumForm, contains_character, illegal_characters
from werkzeug.datastructures import MultiDict

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


# def contains_character(str, characters):
#     for char in str:
#         if char in characters:
#             return True
#     return False


def check_for_errors(request):
    """Check that user input meets requirements.

    Returns a dictionary containing the errors found. Keys are field names.
    Returns an empty dictionary if no errors are found.
    """
    errors = {}

    name = request.json.get('name')
    email = request.json.get('email')
    year = request.json.get('year')
    color = request.json.get('color')

    # illegal_characters = ['<', '>', '{', '}', '[', ']', '(', ')']

    if name == "":
        errors['name'] = "This field is required"
    elif len(name) > 20:
        errors['name'] = "Maximum username length is 20 characters."
    elif contains_character(name, illegal_characters):
        errors['name'] = "Special characters " + (' ').join(illegal_characters) + " not allowed in username."

    if email == "":
        errors['email'] = "This field is required"
    elif len(email) > 30:
        errors['email'] = "Maximum email length is 30 characters."
    elif contains_illegal_character(email, illegal_characters):
        errors['email'] = "Special characters " + (' ').join(illegal_characters) + " not allowed in email."


    if year == "":
        errors['year'] = "This field is required"
    elif not year.isnumeric() or int(year) <= 1900 or int(year) >= 2000:
        errors['year'] = "The year must be an integer between 1900 and 2000"

    colors = ['red', 'green', 'orange', 'blue']
    if color == "":
        errors['color'] = "This field is required"
    elif color not in colors:
        errors['color'] = "Invalid value, must be one of: " + ', '.join(colors) + '.'

    return errors


def check_for_errors2(request):
    """Check that user input meets requirements using WTForms validation.

    Returns a dictionary containing the errors found. Keys are field names.
    Returns an empty dictionary if no errors are found.
    """
    errors = {}

    data = MultiDict(mapping=request.json)
    form = NumForm(data)
    form.validate()
    
    if form.name.errors:
        errors['name'] = form.name.errors[0] 
    if form.email.errors:
        errors['email'] = form.email.errors[0] 
    if form.year.errors:
        errors['year'] = form.year.errors[0]
    if form.color.errors:
        errors['color'] = form.color.errors[0] 

    print(errors)
    return errors


def get_num_fact(num):
    """Returns a random piece of trivia about a given number.

    Fact obtained from numbersapi API: http://numbersapi.com/
    """
    base_url = "http://numbersapi.com/"
    url = base_url + str(num) + "/trivia" 

    response = requests.get(url)
    fact = response.text

    return fact


def get_year_fact(year):
    """Returns a random piece of trivia about a given year.

    Fact obtained from numbersapi API: http://numbersapi.com/
    """
    base_url = "http://numbersapi.com/"
    url = base_url + str(year) + "/year" 

    response = requests.get(url)
    fact = response.text

    return fact


@app.route("/api/get-lucky-num", methods=["POST"])
def get_lucky_num():
    """
    Returns a numberrandom number and a random fact about that number.

    Returns a random fact about the user's birthyear.

    Data format: 
        "num": {
            "fact": "67 is the number of throws in Judo.",
            "num": 67
        },
        "year": {
            "fact": "1950 is the year that nothing remarkable happened.",
            "year": "1950"
        }

    If entries aren't validated, returns a dictionary of errors. 
    """

    errors = check_for_errors(request)

    if len(errors) > 0:
        return jsonify(errors=errors)

    year = request.json.get('year')
    
    num = randint(1, 100)
    num_fact = get_num_fact(num)
    num_data = {"fact": num_fact, "num": num}

    year_fact = get_year_fact(year)
    year_data = {"fact": year_fact, "year": year}

    return jsonify(num=num_data, year=year_data)

