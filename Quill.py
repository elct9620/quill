# nuitka-project-if: {OS} in ("Windows", "Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --onefile
# nuitka-project-else:
#    nuitka-project: --standalone
# nuitka-project: --macos-create-app-bundle
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/frontend/dist=frontend
import webview

is_compiled = "__compiled__" in globals()


def main():
    if is_compiled:
        webview.create_window("Quill", "frontend/index.html")
        webview.start()
    else:
        webview.create_window("Quill", "http://localhost:5173")
        webview.start()


if __name__ == "__main__":
    main()
