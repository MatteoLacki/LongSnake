ve: clean
	python -m virtualenv ve
	ve/bin/pip install -e long_snake
	ln -s ve/bin/activate activate
clean:
	rm -rf ve
