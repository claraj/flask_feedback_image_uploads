import shelve 

database_file = 'feedbacks.db'   # delete this file to clear the database. 
feedback_key = 'feedback'

def save_feedback(feedback):
    with shelve.open(database_file) as db:
        if feedback_key in db: 
            feedbacks = db[feedback_key]
            feedbacks.append(feedback)
        else:
            feedbacks = []

        db[feedback_key] = feedbacks


def get_all_feedback():
    with shelve.open(database_file) as db:
        feedbacks = db.get(feedback_key)
    return feedbacks


def clear_database():
    with shelve.open(database_file) as db:
        db.clear()

