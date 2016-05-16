# Fetch Classwork

1. Activate [virtualenv](https://virtualenv.pypa.io/en/latest/)
2. Run make: `make`
3. Run the file: `python fetch.py`
4. Edit the crontab with your own path to auto-download the files every week after the lecture:  

		0	22	*	5,6	4	path/to/your/python2.7 path/to/your/fetch.py
