from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    if 'count' in session: #Preguntando si existe count en session
        session['count'] += 1 #Si existe, sumamos uno a lo que antes teníamos
    else:
        session['count'] = 0 #Si no existe, entonces inicializamos el count en 1

    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)