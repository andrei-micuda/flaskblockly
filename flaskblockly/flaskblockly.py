from flask import send_from_directory, abort
from werkzeug.exceptions import NotFound
from os import path

class Blockly(object):
    DEFAULT_CONFIG = {
        "endpoint": "blockly",
        "user_static_folder": "blockly_static"
    }

    def __init__(self, app=None, config=None):
        self.init_config(config)

        if app:
            self.init_app(app)

    def init_config(self, config):
        if config:
            self.config = dict(self.DEFAULT_CONFIG.copy(), **config)
        else:
            self.config = self.DEFAULT_CONFIG.copy()

    def init_app(self, app):
        self.app = app
        self.register_views(app)

    def register_views(self, app):
        """
        Register Blockly routes for static files.
        """
        app.add_url_rule(f'/{self.config.get("endpoint")}/<path:subpath>', view_func=self.blockly_static)

    def blockly_static(self, subpath):
        try:
            disk_path = path.realpath(self.config.get("user_static_folder"))
            res = send_from_directory(disk_path, subpath)
        except NotFound as e:
            # file not found in user's overwrite folder, serving from module
            module_dir = path.abspath(path.dirname(__file__))
            module_path = path.join(module_dir, "static")
            res = send_from_directory(module_path, subpath)
        return res
