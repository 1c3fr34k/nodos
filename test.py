import os
import webview


# os.system("start cmd /k python manage.py runserver")
webview.create_window("Nodos", "http://127.0.0.1/notes")
webview.start()
