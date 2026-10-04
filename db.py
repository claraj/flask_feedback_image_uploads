import shelve 

database_file = 'feedbacks.db'   # delete this file to delete all the stored data. 
feedback_key = 'feedback'

def save_feedback(feedback):
    with shelve.open(database_file) as db:
        if feedback_key in db:  # if there is already a list of feedback
            feedbacks = db[feedback_key]  # Get the existing list of feedback from the shelf
        else:
            feedbacks = []  # otherwise, create a new empty list 

        feedbacks.append(feedback)  # add the new feedback to the ebd 
        db[feedback_key] = feedbacks  # save the updated list back to the shelf


def get_all_feedback():
    with shelve.open(database_file) as db:
        feedbacks = db.get(feedback_key)  # Get the feedback list, will be None if there is no feedback list 
    return feedbacks



if __name__ == '__main__':
    print(get_all_feedback())