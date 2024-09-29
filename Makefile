all: test

test: codegen
	devbox run test

codegen:
	devbox run codegen

preview: codegen
	devbox run preview
