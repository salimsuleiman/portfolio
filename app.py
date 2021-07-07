from flask import *

data = [
    {
        'name': 'Customer Relation Manager (Django)',
        'link': 'https://django-crm-2021.herokuapp.com/',
        'image': 'djangoCrm.png',
        'description': 'For managing customers leads and assign any agent to lead by an oraganisation'
    },

    {
        'name': 'Personal Website (html, css)',
        'image': 'pweb.png',
        'link': 'https://salimsuleiman.github.io/personal_website/',
        'description': 'This is my personal website design :)'
    },

    {
        'name': 'Instagram clone (Flask)', 
        'image': 'igClone.png',
        'link': 'https://instagramcloneproject111.herokuapp.com/',
        'description': 'This is for posting image/photos (with caption) you can delete your post like a post and create an account'
    },
    {
        'name': 'News App (Flask)',
        'link': 'https://newsgramproject.herokuapp.com/',
        'image': 'NewsGram.png',
        'description': 'This is build not for english i generated the api using the news api and then translate it to my language (Hausa) for my dad :)'
    },
    {
        'name': 'Salim Blog (Flask)',
        'link': 'https://salim-blog.herokuapp.com/',
        'image': 'blog.png',
        'description': ''
    }
]
app = Flask(__name__)


@app.get('/')
def home():
    return render_template('index.html', portfolios=data)


if __name__ == '__main__':
    app.run(debug=True)