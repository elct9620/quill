import webview

is_compiled = "__compiled__" in globals()


def main():
    if is_compiled:
        webview.create_window("Quill", html="<h1>Working in progress</h1>")
        webview.start()
    else:
        webview.create_window("Quill", html="<h1>Hello, World!</h1>")
        webview.start()


if __name__ == "__main__":
    main()
