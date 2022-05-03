# GradeEz Backend

Backend built with Django complete with caching, rate limiting, etc.

## Prerequisites:

- Python version `3.7`. I am personally running `3.7.13`
- `pip` installed compatible with the same python version as above.

## To run:

- Clone this repo.
- Create a virtual environment.
  
```
python3 -m venv venv
# you can just use 'python' instead of 'python3' instead
```
- Start the virtual environment.
  
```
source venv/bin/activate
```
This will now start a virtual environment. Next time you only need to start it, no need to create again.

- Create a file called `.env` in the root directory (where `manage.py` is present) and fill it up with the API keys specified in `.env.sample` in the same directory.

- Run the server.

```
python3 manage.py runserver
```

- Run the scheduer which is used to send emails asynchronously in another termial parallely.

```
python3 manage.py process_tasks
```

This will start the server on port 8000. You can visit it at [localhost:8000](http://localhost:8000/).

- After you're done, deactivate the virtual environment.

```
deactivate
```

## Notes:

- The model will be downloaded the first time you run the server. After that it will be saved in the `model/` directory. The size is about 1.2 GB.
- The `api/` directory is for the JSON response. For normal templates, use other apps instead.

### The aim of the project / how it is supposed to work

- Passages, questions will be saved in the site. If the teacher wants, he/she can add more passages or add more questions to existing passages.
- Then the teacher can create a new test. This will create a unique test ID/number to identify the test. This will be used in the test link.
- Students need to login with their accounts to be able to answer the test. When they do, they'll be shown the passage, questions in the test and will have the ability to fill and submit their answers. This will be stored in the DB and a score will be given by the AI model to each answer.
- When creating a test a time limit may be set. If the student's time overflows, then the answers won't be accepted.

## Metadata:

- Colour of site: `#57b846`