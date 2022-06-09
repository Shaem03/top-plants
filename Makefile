all: clean test run

run-server:
	gunicorn --bind localhost:5000 --workers 1 wsgi:application
	#CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:application", "--workers=5", "--timeout=300"]

run-client:
	npm start --prefix client

clean:
	rm -rf *.pyc
	rm -rf *__pycache__