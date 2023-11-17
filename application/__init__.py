from flask import Flask
from os import path
import os


def create_app():
  app = Flask(__name__)
  app.secret_key = 'very secrete'

  from .models import Movie, Show, Theater, User, Admin, Booking_movies, Booking_show, Booking_venue

  from .views import bp, engine
  app.register_blueprint(bp)
  from .models import Base
  # db_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ticket_show.db")
  # print(db_file_path)
  # if not os.path.exists(db_file_path):
  #   Base.metadata.create_all(engine)
  #   print("Created database!")
  # return app
#app\Code\ticket_show.db
  if not path.exists("ticket_show.db"):
    Base.metadata.create_all(engine )
    print("Created database!")
  return app
#app\Code\ticket_show.db