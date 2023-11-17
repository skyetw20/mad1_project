from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import select
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# Base.metadata.create_all(engine)


class Movie(Base):
  __tablename__ = 'movies'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  desc = Column(String(255), nullable=False)
  rating = Column(Integer)
  date = Column(String, nullable=False)
  theaters = Column(String(50))
  tags = Column(String(50))
  filename = Column(String, nullable=False)


class Show(Base):
  __tablename__ = 'shows'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  rating = Column(Integer, nullable=False)
  tags = Column(String, nullable=False)
  duration = Column(Integer)
  about = Column(String, nullable=False)
  theaters = Column(String, nullable=False)
  filename = Column(String, nullable=False)


class Theater(Base):
  __tablename__ = 'theaters'
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  place = Column(String, nullable=False)
  filename = Column(String, nullable=False)
  capacity = Column(Integer, nullable=False)
  rph = Column(Integer)
  rating = Column(Integer)
  capacity_pre = Column(Integer)
  base_price = Column(Integer)


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  email = Column(String(120), unique=True, nullable=False)
  password = Column(String(50), nullable=False)
  mobile = Column(String(15), nullable=False)


class Admin(Base):
  __tablename__ = 'admins'
  id = Column(Integer, primary_key=True, autoincrement=True)
  uname = Column(String(50), nullable=False, unique=True)
  password = Column(String(50), nullable=False)


class Booking_movies(Base):
  __tablename__ = 'bookings_movies'
  id = Column(Integer, primary_key=True, autoincrement=True)
  movie_id = Column(Integer, nullable=False)
  date = Column(String(20), nullable=False)
  theater_id = Column(Integer, nullable=False)
  amount = Column(Integer, nullable=False)
  seats = Column(Integer, nullable=False)
  user_id = Column(Integer, nullable=False)
  time = Column(String(10), nullable=False)


class Booking_show(Base):
  __tablename__ = 'bookings_shows'
  id = Column(Integer, primary_key=True)
  show_id = Column(Integer, nullable=False)
  user_id = Column(Integer, nullable=False)
  theater_id = Column(Integer, nullable=False)
  amount = Column(Integer, nullable=False)
  seats = Column(Integer, nullable=False)
  date = Column(String(20), nullable=False)
  time = Column(String(20), nullable=False)


class Booking_venue(Base):
  __tablename__ = 'bookings_venues'
  id = Column(Integer, primary_key=True)
  seats = Column(Integer, nullable=False)
  user_id = Column(Integer, nullable=False)
  theater_id = Column(Integer, nullable=False)
  amount = Column(Integer, nullable=False)
  date = Column(String(20), nullable=False)
  time = Column(String(20), nullable=False)
  duration = Column(Integer, nullable=False)
