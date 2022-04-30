# GradeEz Backend

Backend built with Django complete with caching, rate limiting, etc.

# Prerequisites:

- Python version `3.7`. I am personally running `3.7.13`
- `pip` installed compatible with the same python version as above.

# To run:

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

- Run the server.

```
python3 manage.py runserver
```

This will start the server on port 8000. You can visit it at [localhost:8000](http://localhost:8000/).

- After you're done, deactivate the virtual environment.

```
deactivate
```

# Notes:

- The model will be downloaded the first time you run the server. After that it will be saved in the `model/` directory. The size is about 1.2 GB.
- The `api/` directory is for the JSON response. For normal templates, use other apps instead.