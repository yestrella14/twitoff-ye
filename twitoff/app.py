from flask import Flask, render_template
from models import DB, User, insert_data
from twitter import add_or_update_users
from predict import predict_user

def create_app():
    
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

    DB.init_app(app)

    @app.route('/')#, methods=["GET"])
    def landing():
        DB.drop_all()
        DB.create_all()
        example_users = ["yestrella14", "elonmusk", "rihanna", "katyperry"]
        for user in example_users:
            add_or_update_users(user)
        return render_template("my_twitapp.html", title="Lambda Lesson 2 Unit 3 Sprint 3", users= User.query.all())

        @app.route('/compare', methods=['POST'])
        def compare():
            user1= request.values["selected_user_1"]
            user2= request.values['selected_user_2']
            tweet_text = request.values['tweet_text']

            if user1 == user2:
                message = "Cannot compare the same to itself"
            else:
                prediction= predict_user(user1, user2, tweet_text)
                message = prediction + " is more likely to have said " + tweet_text

            return render_template("prediction.html", title= "compare tweets", message=message)


    return app

app = create_app()

if __name__ =="__main__":
    app.run()
