"""
    main blueprint routes
"""

from flaskr.main import bp

from flask import (
    render_template
)

@bp.route("/", methods=["GET"])
def main():
    """
        entry point for the application
        => Home Page
    """
    return render_template("main/index.html")


