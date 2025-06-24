
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy credentials
users = {
    "admin@school.com": {"password": "admin123", "role": "admin"},
    "teacher@school.com": {"password": "teacher123", "role": "teacher"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = users.get(email)
    if user and user['password'] == password:
        session['role'] = user['role']
        return redirect(url_for(f"{user['role']}_dashboard"))
    return "Invalid credentials", 401

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/submit_class_info', methods=['POST'])
def submit_class_info():
    entry = {
        'class_name': request.form['class_name'],
        'teacher_name': request.form['teacher_name'],
        'student_name': request.form['student_name'],
        'class_timings': request.form['class_timings']
    }
    session.setdefault('class_entries', []).append(entry)
    session.modified = True
    return redirect(url_for('view_class_info'))

@app.route('/admin/class_info')
def view_class_info():
    entries = session.get('class_entries', [])
    return render_template('admin/class_info.html', entries=entries)

@app.route('/teacher/dashboard')
def teacher_dashboard():
    return render_template('teacher/dashboard.html')

@app.route('/teacher/mark_attendance', methods=['POST'])
def mark_attendance():
    entry = {
        'student_name': request.form['student_name'],
        'status': request.form['status']
    }
    session.setdefault('attendance', []).append(entry)
    session.modified = True
    return redirect(url_for('view_attendance'))

@app.route('/teacher/attendance_output')
def view_attendance():
    attendance = session.get('attendance', [])
    return render_template('teacher/attendance_output.html', attendance=attendance)

if __name__ == '__main__':
    app.run(debug=True)
