from flask import Flask, render_template, request, redirect, url_for
from models.teacher import Teacher
from utils.email import send_email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    # Display homepage
    return render_template('index.html')

@app.route('/teachers')
def teachers():
    # Fetch and display list of teachers
    teachers = Teacher.get_all_teachers()
    return render_template('teachers.html', teachers=teachers)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Send email to selected teacher
        teacher_id = request.form['teacher_id']
        teacher = Teacher.get_teacher_by_id(teacher_id)
        recipient_email = teacher.email
        subject = request.form['subject']
        message = request.form['message']
        send_email(recipient_email, subject, message)
        return redirect(url_for('index'))
    else:
        # Display contact form
        teacher_id = request.args.get('teacher_id')
        teacher = Teacher.get_teacher_by_id(teacher_id)
        return render_template('contact.html', teacher=teacher)

if __name__ == '__main__':
    app.run(debug=True)
