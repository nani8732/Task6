from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # In real case, you might store this in a database or send email
    print(f"New contact from {name} ({email}): {message}")
    flash("Thank you for your message!")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
