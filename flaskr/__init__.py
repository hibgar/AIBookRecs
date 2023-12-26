import os
import sqlite3
import traceback

from flask import Flask, request, flash, redirect, url_for, render_template

from flaskr.scraper import analyzeUserList


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import scraper
    app.register_blueprint(scraper.bp)
    app.add_url_rule('/', endpoint='index')

    from . import db
    db.init_app(app)

    @app.route('/process_user_list', methods=['POST'])
    def process_form_user():
        user_list = request.form['userList']  # Assuming 'userList' is the name of your form field
        #analyzeUserList(user_list)  # Pass the user input to the function in scraper.py
        #return f'User list submitted: {user_list}'
        return user_list

    @app.route('/', methods=['GET'])
    def create():
        if request.method == 'POST':


            try:
                link1 = request.form.get('userList')
                link2 = request.form.get('publicList')

                # Validate the form data
                if not link1 or not link2:
                    print('Name and email are required fields.')
                print(link1, link2)
                # Add data to the database
                conn = sqlite3.connect('your_database.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO links (link1, link2) VALUES (?, ?)", (link1, link2))
                conn.commit()
                conn.close()

                print('Data submitted successfully!')
            except Exception as e:
                print('An error occurred while processing the form.', str(e))
                traceback.print_exc()  # Print the traceback for debugging
                return redirect('/')
        return 1

    return app

