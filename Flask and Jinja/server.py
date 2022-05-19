from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

# Jinja (in HTML)
# Any text with {{ }} around it gets evaluated as Python code and inserted into the HTML

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.date.today().year
    return render_template("index.html", num=random_number, current_year=year)


# Using an API
@app.route('/guess/<name>')
def guess_name_details(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)  # This returns a JSON (be sure to check for each particular API)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)  # This returns a JSON (be sure to check for each particular API)
    age_data = age_response.json()
    age = age_data['age']

    return render_template("guess.html", name=name, gender=gender, age=age)


# Multiline statements and API again w/ npoint
@app.route("/blog/<blog_number>")
def get_blog(blog_number):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    # Passing in JSON full list to HTML for Jinja parsing
    return render_template("blog.html", posts=all_posts, blog_number=blog_number)



if __name__ == "__main__":
    app.run(debug=True)