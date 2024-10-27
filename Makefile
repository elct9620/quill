all: test

test:
	devbox run test

preview:
	devbox run preview

build-frontend:
	npm run build -ws

build: build-frontend
	poetry run nuitka Quill.py --standalone

clean:
	rm -rf Quill.dist
	rm -rf Quill.build
	rm -rf Quill.app
