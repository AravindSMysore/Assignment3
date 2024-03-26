import random
import datetime
import time
import json
import os

# Dummy data
users = ['user123', 'user456', 'user789']
movies = ['tt0111161', 'tt0068646', 'tt0071562']

def generate_dummy_recommendation():
    # Select a random user and movie
    user = random.choice(users)
    movie_id = random.choice(movies)
    # Get the current timestamp in ISO format
    timestamp = datetime.datetime.now().isoformat()
    # Return the recommendation in the specified format
    log_entry = {"user": user, "action": "recommend", "movie_id": movie_id, "timestamp": timestamp}
    return json.dumps(log_entry)


if __name__ == "__main__":
    while True:
        with open(os.path.join('logs', 'movie_recommendation.log'), 'a') as log_file:
            log_entry = generate_dummy_recommendation()
            log_file.write(log_entry)
            log_file.write('\n')
            time.sleep(10)
