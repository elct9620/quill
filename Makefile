all: test

test:
	devbox run test

preview:
	devbox run preview

build:
	poetry run nuitka Quill.py --standalone --macos-create-app-bundle

clean:
	rm -rf Quill.dist
	rm -rf Quill.build
	rm -rf Quill.app
