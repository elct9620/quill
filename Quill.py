import webview

if __name__ == "__main__":
    window = webview.create_window("Quill", html="<h1>Hello, World!</h1>")
    webview.start()
