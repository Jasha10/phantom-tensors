install:
	pip install phantom-types beartype pytest hypothesis mypy
	pip install -e '.[test,torch,numpy]'

clean:
	rm -rf .direnv
