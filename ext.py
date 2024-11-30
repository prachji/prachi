from flask import Flask, render_template

app = Flask(__name__)

# Sample data: List of repositories
repositories = [
    {
        "name": "Repo1",
        "description": "This is the first repository.",
        "url": "https://github.com/user/repo1"
    },
    {
        "name": "Repo2",
        "description": "This is the second repository.",
        "url": "https://github.com/user/repo2"
    },
    {
        "name": "Repo3",
        "description": "This is the third repository.",
        "url": "https://github.com/user/repo3"
    }
]

@app.route('/')
def home():
    return render_template('index.html', repositories=repositories)

if __name__ == '__main__':
    app.run(debug=True)
