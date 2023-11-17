# from .models import *
from .models import Movie, Show, Theater, User, Admin, Booking_movies, Booking_show, Booking_venue, Base
from flask import Blueprint, jsonify
from flask import Flask, render_template, request, redirect, flash, session, url_for
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime

bp = Blueprint('views', __name__)
engine = create_engine("sqlite:///./ticket_show.db")


@bp.route('/')
def Index():
  if "email" in session:
    with Session(engine) as ses:
      movie_rows = ses.query(Movie).order_by(
        Movie.rating.desc()).limit(4).all()
      show_rows = ses.query(Show).order_by(Show.rating.desc()).limit(4).all()
      movie_rows_rec = ses.query(Movie).order_by(
        Movie.rating.desc()).limit(2).all()
      show_rows_rec = ses.query(Show).order_by(
        Show.rating.desc()).limit(2).all()

    return render_template('index.html',
                           movie_rows=movie_rows,
                           show_rows=show_rows,
                           movie_rows_rec=movie_rows_rec,
                           show_rows_rec=show_rows_rec,
                           status='logged')
  else:
    with Session(engine) as ses:
      movie_rows = ses.query(Movie).order_by(
        Movie.rating.desc()).limit(4).all()
      show_rows = ses.query(Show).order_by(Show.rating.desc()).limit(4).all()
      movie_rows_rec = ses.query(Movie).order_by(
        Movie.rating.desc()).limit(2).all()
      show_rows_rec = ses.query(Show).order_by(
        Show.rating.desc()).limit(2).all()

    return render_template('index.html',
                           movie_rows=movie_rows,
                           show_rows=show_rows,
                           movie_rows_rec=movie_rows_rec,
                           show_rows_rec=show_rows_rec)


@bp.route('/movies', methods=['GET', 'POST'])
def movies():
  headers = request.headers
  if headers.get('flag') == 'json':
    with Session(engine) as ses:
      rows = ses.query(Movie).all()
    movies = [row.__dict__ for row in rows]
    for movie in movies:
      movie.pop('_sa_instance_state', None)
    # Return the JSON response
    return jsonify(movies)
  if request.headers.get(
      'User-Agent'
  ) != 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36':
    # Return an error response for curl requests
    return "Curl requests are not allowed without headers.", 400

  if "email" in session:
    if request.method == 'POST':
      # print('inside post')
      category = request.form.get('tag')
      # print(category)
      city = request.form.get('city')
      # print(city)
      rating = request.form.get('sort_by_rating')
      # print(type(category),type(city),type(rating))
      if category == "None" and city == None and rating == None:
        with Session(engine) as ses:
          rows = ses.query(Movie).all()
          cities = ses.query(Theater).all()
          return render_template('movies.html',
                                 movies=rows,
                                 status='logged',
                                 cities=cities)

      else:
        with Session(engine) as ses:
          rows = ses.query(Movie).all()

          if category != None:
            filtered_rows = []
            for row in rows:
              if row.tags == category:
                filtered_rows.append(row)
            rows = []
            rows = filtered_rows
          if rating != None:
            rows = ses.query(Movie).order_by(Movie.rating.desc()).all()

          cities = ses.query(Theater).all()
          return render_template('movies.html',
                                 movies=rows,
                                 status='logged',
                                 cities=cities)
    else:
      with Session(engine) as ses:
        rows = ses.query(Movie).all()
        cities = ses.query(Theater).all()
        # print('sdsd')
        # print(cities)
        return render_template('movies.html',
                               movies=rows,
                               status='logged',
                               cities=cities)
  else:
    if request.method == 'POST':
      print('inside post')
      category = request.form.get('tag')
      print(category)
      city = request.form.get('city')
      print(city)
      rating = request.form.get('sort_by_rating')
      print(type(category), type(city), type(rating))
      if category == "None" and city == None and rating == None:
        with Session(engine) as ses:
          rows = ses.query(Movie).all()
          cities = ses.query(Theater).all()
          return render_template('movies.html', movies=rows, cities=cities)

      else:
        with Session(engine) as ses:
          rows = ses.query(Movie).all()

          if category != None:
            filtered_rows = []
            for row in rows:
              if row.tags == category:
                filtered_rows.append(row)
            rows = []
            rows = filtered_rows
          if rating != None:
            rows = ses.query(Movie).order_by(Movie.rating.desc()).all()

          cities = ses.query(Theater).all()
          return render_template('movies.html', movies=rows, cities=cities)
    else:
      with Session(engine) as ses:
        rows = ses.query(Movie).all()
        cities = ses.query(Theater).all()
        # print('sdsd')
        # print(cities)
        return render_template('movies.html', movies=rows, cities=cities)


@bp.route('/shows', methods=['GET', 'POST'])
def shows():
  headers = request.headers
  # print(headers)
  if headers.get('flag') == 'json':
    with Session(engine) as ses:
      rows = ses.query(Show).all()
    shows = [row.__dict__ for row in rows]
    for show in shows:
      show.pop('_sa_instance_state', None)
    # Return the JSON response
    return jsonify(shows)
  if request.headers.get(
      'User-Agent'
  ) != 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36':
    # Return an error response for curl requests
    return "Curl requests are not allowed without headers.", 400
  if "email" in session:
    if request.method == 'POST':
      category = request.form.get('tag')
      rating = request.form.get('sort_by_rating')
      if category == "None" and rating == None:
        with Session(engine) as ses:
          rows = ses.query(Show).all()
          return render_template(
            'shows.html',
            shows=rows,
            status='logged',
          )
      else:
        with Session(engine) as ses:
          rows = ses.query(Show).all()
          if category != "None":
            filtered_rows = []
            for row in rows:
              if row.tags == category:
                filtered_rows.append(row)
            rows = []
            rows = filtered_rows
          if rating != None:
            rows = ses.query(Show).order_by(Show.rating.desc()).all()
          return render_template(
            'shows.html',
            shows=rows,
            status='logged',
          )
    else:
      with Session(engine) as ses:
        rows = ses.query(Show).all()
        return render_template('shows.html', shows=rows, status='logged')
  else:
    if request.method == 'POST':
      print('inside post')
      category = request.form.get('tag')
      rating = request.form.get('sort_by_rating')
      # print(type(category),type(city),type(rating))
      if category == "None" and rating == None:
        with Session(engine) as ses:
          rows = ses.query(Show).all()
          return render_template(
            'shows.html',
            shows=rows,
          )
      else:
        with Session(engine) as ses:
          rows = ses.query(Show).all()
          if category != "None":
            filtered_rows = []
            for row in rows:
              if row.tags == category:
                filtered_rows.append(row)
            rows = []
            rows = filtered_rows
          if rating != None:
            rows = ses.query(Show).order_by(Show.rating.desc()).all()
          return render_template('shows.html', shows=rows)
    else:
      with Session(engine) as ses:
        rows = ses.query(Show).all()
        return render_template(
          'shows.html',
          shows=rows,
        )


########################################
@bp.route('/venues', methods=['GET', 'POST'])
def venues():
  headers = request.headers
  if headers.get('flag') == 'json':
    with Session(engine) as ses:
      rows = ses.query(Theater).all()
    theaters = [row.__dict__ for row in rows]
    for theater in theaters:
      theater.pop('_sa_instance_state', None)
    # Return the JSON response
    return jsonify(theaters)
  if request.headers.get(
      'User-Agent'
  ) != 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36':
    # Return an error response for curl requests
    return "Curl requests are not allowed without headers.", 400
  if "email" in session:
    if request.method == 'POST':
      city = request.form.get('tag')
      rating = request.form.get('sort_by_rating')
      if city == "None" and rating == None:
        with Session(engine) as ses:
          rows = ses.query(Theater).all()
          return render_template(
            'venues.html',
            venues=rows,
            status='logged',
          )
      else:
        with Session(engine) as ses:
          rows = ses.query(Theater).all()
          if city != "None":
            filtered_rows = []
            for row in rows:
              if row.place == city:
                filtered_rows.append(row)
            rows = []
            rows = filtered_rows
          if rating != None:
            rows = ses.query(Theater).order_by(Theater.rating.desc()).all()
          return render_template(
            'venues.html',
            venues=rows,
            status='logged',
          )
    else:
      with Session(engine) as ses:
        rows = ses.query(Theater).all()
        return render_template('venues.html', venues=rows, status='logged')
  else:
    if request.method == 'POST':
      print('inside post')
      city = request.form.get('tag')
      rating = request.form.get('sort_by_rating')
      # print(type(category),type(city),type(rating))
      if city == "None" and rating == None:
        with Session(engine) as ses:
          rows = ses.query(Theater).all()
          return render_template(
            'venues.html',
            venues=rows,
          )

      else:
        with Session(engine) as ses:
          rows = ses.query(Theater).all()
          if city != "None":
            filtered_rows = []
            for row in rows:
              if row.place == city:
                filtered_rows.append(row)
            rows = []
            rows = filtered_rows
          if rating != None:
            rows = ses.query(Theater).order_by(Theater.rating.desc()).all()
          return render_template('venues.html', venues=rows)
    else:
      with Session(engine) as ses:
        rows = ses.query(Theater).all()
        return render_template(
          'venues.html',
          venues=rows,
        )


@bp.route('/account')
def account():
  if "email" in session:
    with Session(engine) as ses:
      rows = ses.query(User).filter(User.email == session['email']).all()
      # print(rows[0].id)
      bookings = ses.query(Booking_movies).filter(
        Booking_movies.user_id == rows[0].id).all()
      # print(bookings)
      movies = []
      theaters = []
      for booking in bookings:
        movie = ses.query(Movie).filter(Movie.id == booking.movie_id).first()
        # print(movie.name)
        # print(type(movie))
        movies.append(movie.name)
        # print(movies)
        theater = ses.query(Theater).filter(
          Theater.id == booking.theater_id).first()
        # print(theater.name)
        theaters.append(theater.name + ", " + theater.place)
      # print(movies,theaters)
      bookings_shows = ses.query(Booking_show).filter(
        Booking_show.user_id == rows[0].id).all()
      shows = []
      theaters_shows = []
      for booking in bookings_shows:
        show = ses.query(Show).filter(Show.id == booking.show_id).first()
        shows.append(show.name)
        theater = ses.query(Theater).filter(
          Theater.id == booking.theater_id).first()
        theaters_shows.append(theater.name + ", " + theater.place)
      bookings_venues = ses.query(Booking_venue).filter(
        Booking_venue.user_id == rows[0].id).all()

      theaters_venues = []
      for booking in bookings_venues:

        theater = ses.query(Theater).filter(
          Theater.id == booking.theater_id).first()
        theaters_shows.append(theater.name + ", " + theater.place)
      return render_template('account.html',
                             status='logged',
                             user=rows[0],
                             bookings=bookings,
                             movies=movies,
                             theaters=theaters,
                             bookings_shows=bookings_shows,
                             shows=shows,
                             theaters_shows=theaters_shows,
                             bookings_venues=bookings_venues,
                             theaters_venues=theaters_shows)
  else:
    return redirect('/login')


@bp.route('/logout')
def logout():
  session.pop('email', None)
  return redirect('/movies')


@bp.route('/login', methods=["GET", 'POST'])
def login():

  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    if "email" in session and session['email'] == email:
      return redirect(f'/account')
    else:
      with Session(engine) as ses:
        rows = ses.query(User).filter(User.email == email).all()
        if len(rows) != 0 and password == rows[0].password:
          session['email'] = email
          return redirect(f'/account')
        else:
          msg = "Inavlid Username or Password"
          return render_template('login.html', msg=msg)
  else:
    return render_template('login.html')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    # password=sha256_crypt.encrypt(str(password))
    mno = request.form.get('mobile_no')
    with Session(engine) as session:
      rows = session.query(User).filter(User.email == email).all()
      # print(type(rows))
      if len(rows) == 0:
        entry = User(name=name, email=email, password=password, mobile=mno)
        with Session(engine) as session:
          session.add(entry)
          session.commit()
          flash("Account Created. Now Login...")
          return redirect('/login')
      else:
        flash("You already have an account. LogIn Here...")
        return redirect('/login')
    return redirect('/login')
    # return render_template('signup.html')
  else:
    return render_template('signup.html')


@bp.route('/book/movie/<int:movie_name>', methods=["GET", 'POST'])
def book(movie_name):
  if "email" in session:
    with Session(engine) as ses:
      rows = ses.query(Movie).filter(Movie.id == movie_name)
      # my_list = my_string.split(", ")
      # print(rows[0].theaters.split(", "))
      theater_ids = rows[0].theaters.split(", ")
      # print((theater_ids))
      theaters = []
      for t in theater_ids:
        # print(t)
        theater = ses.query(Theater).filter(Theater.id == int(t)).first()
        theaters.append(theater)
      # print(theaters[0], theaters[0])
    return render_template('book.html',
                           name=rows[0],
                           status='logged',
                           event="Movie",
                           theaters=theaters)

  else:
    flash("Please Log In first.")
    return redirect('/login')


@bp.route('/book/movie', methods=["GET", 'POST'])
def book_movie():
  if "email" in session:
    if request.method == 'POST':
      m_id = request.form.get('movie_id')
      print(m_id)
      theater = request.form.get('theater')
      date = request.form.get('date')
      time = request.form.get('time')
      seats = request.form.get('seats')
      with Session(engine) as ses:
        rows = ses.query(User).filter(User.email == session['email']).all()
        print(rows[0].id)
        venue = ses.query(Theater).filter(Theater.id == int(theater)).first()
        if int(venue.capacity_pre) + int(seats) <= venue.capacity:
          venue.capacity_pre = venue.capacity_pre + int(seats)
          ses.commit()
          booking = Booking_movies(movie_id=m_id,
                                   date=date,
                                   theater_id=theater,
                                   amount=int(venue.base_price) * int(seats),
                                   seats=seats,
                                   user_id=rows[0].id,
                                   time=time)
          with Session(engine) as ses:
            ses.add(booking)
            ses.commit()
        else:
          flash(
            f'Not Enough Seats Available.Available Seats are-{venue.capacity-venue.capacity_pre}'
          )
          return redirect(f'/book/movie/{m_id}')
      return redirect('/account')

    else:
      redirect('/movies')
  else:
    flash("Before Booking, Log In Here...")
    return redirect('/login')


#show bookings


@bp.route('/book/show/<int:show_id>', methods=["GET", 'POST'])
def book_s(show_id):
  if "email" in session:
    with Session(engine) as ses:
      rows = ses.query(Show).filter(Show.id == show_id)
      # my_list = my_string.split(", ")
      # print(rows[0].theaters.split(", "))
      theater_ids = rows[0].theaters.split(", ")
      # print((theater_ids))
      theaters = []
      for t in theater_ids:
        # print(t)
        theater = ses.query(Theater).filter(Theater.id == int(t)).first()
        theaters.append(theater)
      # print(theaters[0], theaters[0])
    return render_template('book_shows.html',
                           name=rows[0],
                           status='logged',
                           theaters=theaters)

  else:
    flash("Before Booking, Log In Here...")
    return redirect('/login')


@bp.route('/book/show', methods=["GET", 'POST'])
def book_show():
  if "email" in session:
    if request.method == 'POST':
      s_id = request.form.get('movie_id')
      # print(s_id)
      theater = request.form.get('theater')
      date = request.form.get('date')
      time = request.form.get('time')
      seats = request.form.get('seats')
      with Session(engine) as ses:
        rows = ses.query(User).filter(User.email == session['email']).all()
        print(rows[0].id)
        venue = ses.query(Theater).filter(Theater.id == int(theater)).first()
        show = ses.query(Show).filter(Show.id == int(s_id)).first()
        if int(venue.capacity_pre) + int(seats) <= venue.capacity:
          venue.capacity_pre = venue.capacity_pre + int(seats)
          ses.commit()

          booking = Booking_show(show_id=s_id,
                                 date=date,
                                 theater_id=theater,
                                 amount=(int(venue.base_price) * int(seats)) +
                                 ((int(show.duration) / 60) * venue.rph),
                                 seats=seats,
                                 user_id=rows[0].id,
                                 time=time)
          with Session(engine) as ses:
            ses.add(booking)
            ses.commit()
        else:
          flash(
            f'Not Enough Seats Available.Available Seats are-{venue.capacity-venue.capacity_pre}'
          )
          return redirect(f'/book/show/{s_id}')
      return redirect('/account')

    else:
      redirect('/shows')
  else:
    flash("Before Booking, Log In Here...")
    return redirect('/login')


#shows booking end here
#venue booking starts here


@bp.route('/book/venue/<int:venue_id>', methods=["GET", 'POST'])
def book_v(venue_id):
  if "email" in session:
    with Session(engine) as ses:
      row = ses.query(Theater).filter(Theater.id == venue_id).first()

    return render_template(
      'book_venue.html',
      name=row,
      status='logged',
    )

  else:
    flash("Before Booking, Log In Here...")
    return redirect('/login')


@bp.route('/book/venue', methods=["GET", 'POST'])
def book_venue():
  if "email" in session:
    if request.method == 'POST':
      v_id = request.form.get('movie_id')
      # print(s_id)
      date = request.form.get('date')
      time = request.form.get('time')
      duration = request.form.get('duration')
      with Session(engine) as ses:
        rows = ses.query(User).filter(User.email == session['email']).all()
        # print(rows[0].id)
        venue = ses.query(Theater).filter(Theater.id == int(v_id)).first()
        if int(venue.capacity_pre) < venue.capacity:

          booking = Booking_venue(
            date=date,
            theater_id=v_id,
            amount=(int(venue.base_price) *
                    int(venue.capacity - venue.capacity_pre)) +
            ((int(duration) / 60) * venue.rph),
            seats=venue.capacity - venue.capacity_pre,
            user_id=rows[0].id,
            time=time,
            duration=duration,
          )
          venue.capacity_pre = venue.capacity
          ses.commit()
          with Session(engine) as ses:
            ses.add(booking)
            ses.commit()
        else:
          flash(
            f'Not Enough Seats Available.Available Seats are-{venue.capacity-venue.capacity_pre}'
          )
          return redirect(f'/book/venue/{v_id}')
      return redirect('/account')

    else:
      redirect('/venues')
  else:
    flash("Before Booking, Log In Here...")
    return redirect('/login')


#venue booking ends here
@bp.route('/admin-login', methods=['GET', "POST"])
def admin_login():
  if 'email' in session:
    session.pop('email', None)
    return render_template('admin_login.html')

  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    # print(email,password)
    with Session(engine) as ses:
      # rows = ses.query(Admin).filter(Admin.uname == email).all()
      try:
        rows = ses.query(Admin).filter(Admin.uname == email).all()
      except Exception as e:
        print(f"Erro: {e}")
      print(len(rows))
      # print(rows[0].password)
      if len(rows) != 0 and password == rows[0].password:
        session['admin'] = email
        return redirect('/admin')
      else:
        msg = "Inavlid Username or Password"
        return render_template('admin_login.html', msg=msg, status='admin')
  else:
    return render_template('admin_login.html')


@bp.route('/admin_logout')
def admin_logout():
  session.pop('admin', None)
  return redirect('/movies')


@bp.route('/admin')
def admin():
  if 'admin' in session:
    # print(session['admin'])
    with Session(engine) as ses:
      m_rows = ses.query(Movie).count()
      s_rows = ses.query(Movie).count()
      v_rows = ses.query(func.count(Theater.id)).scalar()
      total_capacity, total_capacity_pre, percentage_vacant_seats = ses.query(
        func.sum(Theater.capacity), func.sum(Theater.capacity_pre),
        ((func.sum(Theater.capacity) - func.sum(Theater.capacity_pre)) *
         100.0 / func.sum(Theater.capacity))).first()
      return render_template('admin.html',
                             t_movies=m_rows,
                             t_shows=s_rows,
                             t_venues=v_rows,
                             t_capacity=total_capacity,
                             t_booked=total_capacity_pre,
                             p_vacant=round(percentage_vacant_seats, 2),
                             status='admin',
                             admin=session['admin'])
  else:
    return redirect('/admin-login')


@bp.route('/admin/movie_management')
def movie_management():
  if 'admin' in session:
    with Session(engine) as ses:
      rows = ses.query(Movie).all()
      return render_template(
        'movie_manage.html',
        movies=rows,
        status='admin',
      )
  else:
    return redirect('/admin-login')


@bp.route('/admin/movie_management/delete/<int:id>')
def movie_delete(id):
  if 'admin' in session:
    with Session(engine) as ses:
      # movie = Movie.query.get(id)
      movie = ses.query(Movie).filter(Movie.id == id)
      print(movie)
      if movie is None:
        return render_template(
          'movie_manage.html',
          movies=rows,
          status='admin',
        )
      else:
        ses.query(Movie).filter(Movie.id == id).delete()
        ses.commit()
      with Session(engine) as ses:
        rows = ses.query(Movie).all()
    flash("Record deleted.")
    return redirect('/admin/movie_management')
    # return render_template('movie_manage.html',movies=rows,status='admin',)
  else:
    return redirect('/admin-login')


@bp.route('/admin/movie_management/update/<int:id>')
def movie_update(id):
  if 'admin' in session:
    with Session(engine) as ses:
      movie = ses.query(Movie).filter(Movie.id == id).first()
      rows = ses.query(Theater).all()
      print("prinitin", movie)
      if movie is None:
        return render_template(
          'movie_manage.html',
          movies=movie,
          status='admin',
        )
      else:

        return render_template('update_movie.html',
                               movies=movie,
                               status='admin',
                               theaters=rows)
  else:
    return redirect('/admin-login')


@bp.route('/admin/movie_management/update', methods=['POST'])
def movie_u():
  if 'admin' in session:
    if request.method == 'POST':
      name = request.form.get('name')
      id = request.form.get('movie_id')
      desc = request.form.get('desc')
      rating = request.form.get('rating')
      date_ = request.form.get('date')
      date_obj = datetime.datetime.strptime(date_, '%Y-%m-%d').date()
      theaters = request.form.getlist('theaters')
      tags = request.form.get('tags')
      with Session(engine) as ses:
        movie = ses.query(Movie).filter(Movie.id == id).first()
        movie.name = name
        movie.desc = desc
        movie.rating = rating
        movie.date = date_obj
        movie.theaters = ', '.join(theaters)
        movie.tags = tags
        ses.commit()
      flash('Record Updated Successfully.')
      return redirect('/admin/movie_management')
  else:
    return redirect('/admin-login')


@bp.route('/admin/add_movie', methods=['POST', 'GET'])
def add_movie():
  if 'admin' in session:
    if request.method == 'POST':
      name = request.form.get('name')
      desc = request.form.get('desc')
      rating = request.form.get('rating')
      date_ = request.form.get('date')
      date_obj = datetime.datetime.strptime(date_, '%Y-%m-%d').date()
      theaters = request.form.getlist('theaters')
      tags = request.form.get('tags')
      f = request.files['file']
      # print(name,desc,rating,date_obj,theaters)
      entry = Movie(name=name,
                    desc=desc,
                    rating=rating,
                    date=date_obj,
                    theaters=', '.join(theaters),
                    tags=tags,
                    filename=f.filename)
      # my_list = my_string.split(", ")
      with Session(engine) as ses:
        ses.add(entry)
        ses.commit()
      with Session(engine) as ses:
        rows = ses.query(Theater).all()
      return render_template(
        'add_movie.html',
        theaters=rows,
        msg="Added Succesfully",
        status='admin',
      )
    else:
      with Session(engine) as ses:
        rows = ses.query(Theater).all()
      return render_template(
        'add_movie.html',
        theaters=rows,
        status='admin',
      )
  else:
    return redirect('/admin-login')


@bp.route('/admin/show_management')
def show_management():
  if 'admin' in session:
    with Session(engine) as ses:
      rows = ses.query(Show).all()
    return render_template(
      'show_manage.html',
      shows=rows,
      status='admin',
    )
  else:
    return redirect('/admin-login')


@bp.route('/admin/show_management/delete/<int:id>')
def show_delete(id):
  if 'admin' in session:
    with Session(engine) as ses:
      # movie = Movie.query.get(id)
      show = ses.query(Show).filter(Show.id == id)
      # print(movie)
      if show is None:
        return render_template(
          'show_manage.html',
          movies=rows,
          status='admin',
        )
      else:
        ses.query(Show).filter(Show.id == id).delete()
        ses.commit()
      with Session(engine) as ses:
        rows = ses.query(Show).all()
    flash("Record deleted.")
    return redirect('/admin/show_management')
    # return render_template('show_manage.html',shows=rows,status='admin',)
  else:
    return redirect('/admin-login')


###############
@bp.route('/admin/show_management/update/<int:id>')
def show_update(id):
  if 'admin' in session:
    with Session(engine) as ses:
      show = ses.query(Show).filter(Show.id == id).first()
      rows = ses.query(Theater).all()
      # print("prinitin",show)
      return render_template('update_show.html',
                             shows=show,
                             status='admin',
                             theaters=rows)
  else:
    return redirect('/admin-login')


@bp.route('/admin/show_management/update', methods=['POST'])
def show_u():
  if 'admin' in session:
    if request.method == 'POST':
      id = request.form.get('show_id')
      name = request.form.get('name')
      rating = request.form.get('rating')
      tags = request.form.get('tags')
      duration = request.form.get('duration')
      theaters = request.form.getlist('theaters')
      about = request.form.get('about')
      with Session(engine) as ses:
        show = ses.query(Show).filter(Show.id == id).first()
        show.name = name
        show.about = about
        show.rating = rating
        show.duration = duration
        show.theaters = ', '.join(theaters)
        show.tags = tags
        ses.commit()
      flash('Record Updated Successfully.')
      return redirect('/admin/show_management')
  else:
    return redirect('/admin-login')


#########
@bp.route('/admin/add_show', methods=['POST', 'GET'])
def add_show():

  if 'admin' in session:
    if request.method == 'POST':
      #name,rating,tags,ticket_price,duration,about
      name = request.form.get('name')
      rating = request.form.get('rating')
      tags = request.form.get('tags')
      duration = request.form.get('duration')
      theaters = request.form.getlist('theaters')
      about = request.form.get('about')
      f = request.files['file']
      entry = Show(name=name,
                   rating=rating,
                   tags=tags,
                   duration=duration,
                   about=about,
                   theaters=', '.join(theaters),
                   filename=f.filename)
      with Session(engine) as ses:
        ses.add(entry)
        ses.commit()
      # with Session(engine) as session:
      #     rows = session.query(Show).all()
      return render_template(
        'add_show.html',
        msg="Added Succesfully",
        status='admin',
      )

    else:
      with Session(engine) as ses:
        rows = ses.query(Theater).all()
        print(rows)
      return render_template(
        'add_show.html',
        theaters=rows,
        status='admin',
      )
  else:
    return redirect('/admin-login')


@bp.route('/admin/venue_management')
def venue_management():
  with Session(engine) as session:
    rows = session.query(Theater).all()
  return render_template(
    'venue_manage.html',
    venues=rows,
    status='admin',
  )


@bp.route('/admin/venue_management/delete/<int:id>')
def venue_delete(id):
  if 'admin' in session:
    with Session(engine) as ses:
      # movie = Movie.query.get(id)
      venue = ses.query(Theater).filter(Theater.id == id)
      # print(movie)
      if venue is None:
        return render_template(
          'venue_manage.html',
          venues=rows,
          status='admin',
        )
      else:
        ses.query(Theater).filter(Theater.id == id).delete()
        ses.commit()
    with Session(engine) as ses:
      rows = ses.query(Theater).all()
    flash("Record deleted.")
    return redirect('/admin/venue_management')
    # return render_template('venue_manage.html',shows=rows,status='admin',)
  else:
    return redirect('/admin-login')


#######################################
@bp.route('/admin/venue_management/update/<int:id>')
def venue_update(id):
  if 'admin' in session:
    with Session(engine) as ses:
      theater = ses.query(Theater).filter(Theater.id == id).first()
      return render_template('update_venue.html',
                             venue=theater,
                             status='admin')
  else:
    return redirect('/admin-login')


@bp.route('/admin/venue_management/update', methods=['POST'])
def venue_u():
  if 'admin' in session:
    if request.method == 'POST':
      id = request.form.get('venue_id')
      name = request.form.get('name')
      place = request.form.get('place')
      capacity = request.form.get('capacity')
      rph = request.form.get('rph')
      rating = request.form.get('rating')
      capacity_pre = request.form.get('capacity_pre')
      base_price = request.form.get('base_price')
      with Session(engine) as ses:
        venue = ses.query(Theater).filter(Theater.id == id).first()
        venue.name = name
        venue.place = place
        venue.capacity = capacity
        venue.rph = rph
        venue.rating = rating
        venue.capacity_pre = capacity_pre
        venue.base_price = base_price
        ses.commit()
      flash('Record Updated Successfully.')
      return redirect('/admin/venue_management')
  else:
    return redirect('/admin-login')


###############################
@bp.route('/admin/add_venue', methods=['POST', 'GET'])
def add_venue():
  if 'admin' in session:
    if request.method == 'POST':
      name = request.form.get('name')
      place = request.form.get('place')
      capacity = request.form.get('capacity')
      rph = request.form.get('rph')
      rating = request.form.get('rating')
      capacity_pre = request.form.get('capacity_pre')
      base_price = request.form.get('base_price')
      f = request.files['file']
      # print(f.filename)
      entry = Theater(name=name,
                      place=place,
                      capacity=capacity,
                      rph=rph,
                      rating=rating,
                      capacity_pre=capacity_pre,
                      base_price=base_price,
                      filename=f.filename)
      with Session(engine) as ses:
        ses.add(entry)
        ses.commit()
      return render_template(
        'add_venue.html',
        msg='Added Successfuly',
        status='admin',
      )
    else:
      return render_template(
        'add_venue.html',
        status='admin',
      )
  else:
    return redirect('/admin-login')
