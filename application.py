from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
	if request.method == 'POST':
		x = int(request.form['x'])
		y = int(request.form['y'])

		def run_simulaton(x, y):
			return x * y

		xtimesy = run_simulaton(x, y)
		return render_template('result.html', xtimesy = xtimesy)
	return render_template('index.html')

@app.route('/redirect')
def redirect_eg():
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=True)
