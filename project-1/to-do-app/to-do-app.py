"""
    main file to call the application factory and run the application
"""

from flaskr import create_app

app = create_app()

# code to run the application if this main file is directly run
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=False
    )
