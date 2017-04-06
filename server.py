#!/usr/bin/env python2.7

"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver

To run locally:

    python server.py

Go to http://localhost:8111 in your browser.

A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
from jinja2 import Template

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@104.196.18.7/w4111
#
# For example, if you had username biliris and password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://biliris:foobar@104.196.18.7/w4111"
#
DATABASEURI = "postgresql://tw2579:6846@104.196.18.7/w4111"


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # DEBUG: this is debugging code to see what request looks like
  # print request.args


  #
  # example of a database query
  #
  # cursor = g.conn.execute("SELECT name FROM test")
  # names = []
  # for result in cursor:
  #   names.append(result['name'])  # can also be accessed using result[0]
  # cursor.close()

  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #
  # context = dict(data = names)


  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #
  return render_template("index.html")

#
# This is an example of a different path.  You can see it at:
# 
#     localhost:8111/another
#
# Notice that the function name is another() rather than index()
# The functions for each app.route need to have different names
#
@app.route('/course')
def course():
  # name = request.form['name']
  s = """select * from course"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("course.html", **context)

@app.route('/knowledge')
def knowledge():
  # name = request.form['name']
  s = """select * from knowledge"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("knowledge.html", **context)

@app.route('/reference')
def reference():
  # name = request.form['name']
  s = """select link_id, link_name from reference"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("reference.html", **context)

@app.route('/theorem')
def theorem():
  # name = request.form['name']
  s = """select * from theorem"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("theorem.html", **context)

@app.route('/event')
def event():
  s = """Select * FROM EVENT"""
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(data=names)
  return render_template("event.html", **context)


@app.route('/course2knowledge', methods = ['GET', 'POST'])
def course2knowledge():
  name = request.form['name']
  s = """select k_name from cover where cover.course_id = """
  s += name
  # s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("knowledge.html", **context)

@app.route('/course2course', methods = ['GET', 'POST'])
def course2course():
  name = request.form['name']
  s = """select prerequisite.course_id_pre, course.c_name from prerequisite, course where prerequisite.course_id_pre = course.course_id and prerequisite.course_id_post = """
  s += name
  # s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("course.html", **context)

@app.route('/course2reference', methods = ['GET', 'POST'])
def course2reference():
  name = request.form['name']
  s = """select about.link_id from about where about.course_id = """
  s += name
  # s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("reference.html", **context)

@app.route('/knowledge2event', methods = ['GET', 'POST'])
def knowledge2event():
  name = request.form['name']
  s = """select relateto.event_id, event.event_name from event, relateto where relateto.event_id = event.event_id and relateto.k_name ='"""
  s += name
  s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("event.html", **context)

@app.route('/knowledge2theorem', methods = ['GET', 'POST'])
def knowledge2theorem():
  name = request.form['name']
  s = """select theorem_id, theorem_name from theorem where k_name ='"""
  s += name
  s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("theorem.html", **context)

@app.route('/knowledge2course', methods = ['GET', 'POST'])
def knowledge2course():
  name = request.form['name']
  s = """select cover.course_id, course.c_name where cover.course_id =course.c_name and cover.k_name = '"""
  s += name
  s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("course.html", **context)

@app.route('/knowledge2knowledge', methods = ['GET', 'POST'])
def knowledge2knowledge():
  name = request.form['name']
  s = """select knowledge_sub from subordinate where knowledge_sup ='"""
  s += name
  s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("knowledge.html", **context)


@app.route('/reference2course', methods = ['GET', 'POST'])
def reference2course():
  name = request.form['name']
  s = """select about.couse_id, course.c_name from about where about.course_id =course.course_id and about.link_id = """
  s += name
  #s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("course.html", **context)

@app.route('/theorem2knowledge', methods = ['GET', 'POST'])
def theorem2knowledge():
  name = request.form['name']
  s = """select k_name from theorem where theorem_id = """
  s += name
  #s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("knowledge.html", **context)

@app.route('/theorem2scientist', methods = ['GET', 'POST'])
def theorem2scientist():
  name = request.form['name']
  s = """select prove.person_id, scientist.s_name from scientist, prove where prove.person_id = scientist.person_id and prove.theorem_id = """
  s += name
  #s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("scientist.html", **context)

@app.route('/theorem2axiom', methods = ['GET', 'POST'])
def theorem2axiom():
  name = request.form['name']
  s = """select axiom_name from premise where theorem_id = """
  s += name
  #s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("axiom.html", **context)

@app.route('/theoremContent', methods = ['GET', 'POST'])
def theoremContent():
  name = request.form['name']
  s = """select theorem_content from theorem where theorem_id = """
  s += name
  #s += """'"""
  print s
  cursor = g.conn.execute(s)

  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  print names

  context = dict(data=names)

  return render_template("theorem.html", **context)


# Example of adding new data to the database
@app.route('/interesting_example')
def interesting_example():
  return render_template("example.html")

@app.route('/example1', methods=['POST'])
def example1():
  name = request.form['name']
  s = """select c0.course_id, c0.c_name from course c0 where c0.course_id <> """
  s += name
  s += """ and
                                c0.course_id not in (select c7.course_id from course c7, prerequisite p5 where
                                p5.course_id_pre = """
  s += name
  s += """ and p5.course_id_post = c7.course_id) and c0.course_id
                                not in (select c3.course_id from course c1, course c2, course c3, prerequisite p1,
                                prerequisite p2 where p1.course_id_pre = c1.course_id and p1.course_id_post =
                                c2.course_id and p2.course_id_pre = c2.course_id and p2.course_id_post = c3.course_id and
                                c1.course_id = """
  s += name
  s += """) and c0.course_id in (select c4.course_id from course c4, prerequisite
                                p3 where c4.course_id = p3.course_id_post) and c0.course_id not in (select c6.course_id from
                                course c5, course c6, prerequisite p4 where p4.course_id_pre = c5.course_id and
                                p4.course_id_post = c6.course_id and c5.course_id not in (select c4.course_id from
                                course c4, prerequisite p3 where c4.course_id = p3.course_id_post))"""
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  context = dict(data=names)
  return render_template("example1.html", **context)

# Example of adding new data to the database
@app.route('/example2', methods=['POST'])
def example2():
  s = """select event.event_name, scientist.s_name from scientist, event, regardto where regardto.event_id
          = event.event_id and regardto.person_id = scientist.person_id and date_of_birth > '1800-01-01 00:00:00'
          and nationality in (select nationality from scientist where date_of_birth > '1800-01-01 00:00:00'
          group by nationality having count(*) = (select max(cnt) from (select count(*) as cnt from scientist
          where date_of_birth > '1800-01-01 00:00:00' group by nationality) S))"""
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()
  context = dict(data=names)
  return render_template("example2.html", **context)

# Example of adding new data to the database
@app.route('/example3', methods=['POST'])
def example3():
  name = request.form['name']
  s = """select distinct theorem.theorem_name as
        theorem_name, reference.link_name from reference, course, theorem,
        about, cover where about.course_id = course.course_id and about.link_id = reference.link_id
        and cover.course_id = course.course_id and cover.k_name = theorem.k_name and theorem.theorem_id = """
  s += name
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(data=names)
  return render_template("example3.html", **context)


# Example of adding new data to the database
@app.route('/event2scientist', methods=['POST'])
def event2scientist():
  name = request.form['name']
  s = """select * from scientist, regardto , event where regardto.person_id = scientist.person_id and
          regardto.event_id = event.event_id and s_name = '"""
  s += name
  s += """'"""
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(data=names)
  return render_template("scientist.html", **context)

@app.route('/event2knowledge', methods=['POST'])
def event2knowledge():
  name = request.form['name']
  s = """select knowledge from knowledge, relateto where relateto.k_name = knowledge.k_name and
          relateto.event_id = '"""
  s += name
  s += """'"""
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(data=names)
  return render_template("knowledge.html", **context)

@app.route('/insert_course', methods=['POST'])
def insert_course():
  c_id = request.form['c_id']
  c_name = request.form['c_name']
  k_name = request.form['k_name']

  s = """INSERT INTO course (course_id, c_name)  VALUES("""
  s += c_id
  s += """, '"""
  s += c_name
  s += """')"""
  g.conn.execute(s)
  s = """INSERT INTO cover (k_name, course_id) VALUES('"""
  s += k_name
  s += """', """
  s += c_id
  s += """)"""
  g.conn.execute(s)
  s = """select * from course"""
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(data=names)
  return render_template("course.html", **context)

@app.route('/insert_prerequisite', methods=['POST'])
def insert_prerequisite():
  c_id_pre = request.form['c_id_pre']
  c_id_post = request.form['c_id_post']
  s = """INSERT INTO prerequisite (course_id_pre, course_id_post)  VALUES("""
  s += c_id_pre
  s += """, """
  s += c_id_post
  s += """)"""
  g.conn.execute(s)
  s = """select prerequisite.course_id_pre, course.c_name from prerequisite,
        course where prerequisite.course_id_pre = course.course_id and prerequisite.course_id_post = """
  s += c_id_post
  # s += """'"""
  cursor = g.conn.execute(s)
  s = """select * from prerequisite"""
  cursor = g.conn.execute(s)
  names = []
  for result in cursor:
    names.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(data=names)
  return render_template("course.html", **context)
@app.route('/another')
def another():
  return render_template("event.html")



# Example of adding new data to the database
@app.route('/add', methods=['POST'])
def add():
  name = request.form['name']
  g.conn.execute('INSERT INTO test VALUES (NULL, ?)', name)
  return redirect('/')


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
