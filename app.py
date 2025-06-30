import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

def load_courses_data():
    """Load courses data from JSON file"""
    try:
        with open('static/courses_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    """Main page showing all courses"""
    courses = load_courses_data()
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    """Course detail page"""
    courses = load_courses_data()
    
    # Find course by ID
    course = None
    for c in courses:
        if c['id'] == course_id:
            course = c
            break
    
    if course is None:
        abort(404)
    
    return render_template('course_detail.html', course=course)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
