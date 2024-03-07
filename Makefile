.PHONY: all install dev-install uninstall chat image clean

all: dev-install

install: clean
	pip install .

dev-install: clean
	pip install -e .

uninstall: clean
	pip uninstall barrier

chat:
	python scripts/chat.py

image:
	python scripts/image_gen.py

clean:
	$(RM) -rf build barrier.egg-info *.so dist/ barrier/__pycache__/
