from flask import Flask
from views import homepage,welcome


def configure_routes(app):
    app.add_url_rule('/', 'homepage', homepage,methods=["POST","GET"])
    app.add_url_rule('/welcome/<username>', 'welcome', welcome)
    