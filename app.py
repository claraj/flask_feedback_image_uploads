from flask import Flask, render_template, request, send_from_directory
import os 
import uuid
import db

app = Flask(__name__)

# Lots of security issues with uploading files
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
app.config['UPLOAD_FOLDER'] = 'user_feedback_images'

@app.route('/')
def homepage():
    return render_template('feedback_form.html')


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.to_dict()  # all the text feedback
    image_file = request.files['image']  # the file, if one is uploaded
    if image_file.filename:
        save_filename = f'{uuid.uuid4()}_{image_file.filename}'
        save_location = os.path.join(app.config['UPLOAD_FOLDER'], save_filename)
        image_file.save(save_location)
        feedback['image_path'] = save_filename

    db.save_feedback(feedback)

    # TODO error handling
    # TODO several security-related tasks for file uploads

    return render_template('thank_you.html')


@app.route('/admin') # A real app would require authentication for this page
def admin_page():  
    feedbacks = db.get_all_feedback()
    if feedbacks is None:
        feedbacks = []

    feedback_count = len(feedbacks)
    user_image_location = app.config['UPLOAD_FOLDER']
    return render_template('admin.html', feedbacks=feedbacks, user_image_location=user_image_location, feedback_count=feedback_count) 


@app.route('/user_feedback_images/<filename>')
def user_feedback_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)