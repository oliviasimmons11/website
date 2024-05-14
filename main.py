from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html', page_title='Home')


@app.route('/about')  # note the leading slash, it’s important
def about():
   return render_template('about.html', page_title='ABOUT')

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', user_name=name)

@app.route('/user/<name>')
def user(name):
  favourite_food = ["Burgers", "Pizza", "Chocolate", "Sushi", "Fried Chicken", "Combination 4"]
  stuff = "This is <strong>Bold</strong>"
  return render_template('user.html', user_name=name, stuff=stuff, favourite_food=favourite_food)


if __name__ == "__main__":  
   app.run(debug=True)
