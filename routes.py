from flask import Flask, url_for, render_template, request
from app import app
from main import Chatbot as cb
import os
#from school import Chatbot as cb

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create')
def create():
	return render_template('cq.html')

@app.route('/name/<name>')
def name(name):
	return 'Your name is ' + name

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		ans = request.form['response']
		fout = open('lastinput.txt', 'r')
		contents = fout.read()
		fout.close()
		os.remove('lastinput.txt')
		response = cb(ans, contents)
		fin = open('lastinput.txt', 'w+')
		if isinstance(response, list):
			fin.write("Hey")
		else:
			fin.write(str(response))
			if response is not None:
				response = response.split(' . ')
			else:
				return render_template('contact.html', message = ans, response = ["Sorry not able to Display", " "])
		fin.close()
		return render_template('contact.html', message = ans, response = response)
		
	return render_template('contact.html')

@app.route('/contact')

@app.route('/about')
def about():
	return render_template('about.html')