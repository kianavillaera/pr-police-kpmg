from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Vulnerable to SQL injection
@app.route('/user/<user_id>')
def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # No parameterization!
    cursor.execute(query)
    return str(cursor.fetchall())

# Vulnerable to XSS
@app.route('/search')
def search():
    term = request.args.get('q', '')
    return f"<h1>Results for: {term}</h1><script>alert('hi')</script>"  # No escaping!

if __name__ == '__main__':
    app.run(debug=True)
