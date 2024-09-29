all: test

test: codegen
	devbox run test

codegen:
	devbox run codegen

preview: codegen
	devbox run preview

build: codegen
	poetry run nuitka Quill.py --standalone --plugin-enable=pyside6 --macos-create-app-bundle

clean:
	rm -rf Quill.dist
	rm -rf Quill.build
	rm -rf Quill.app
