# Blockly

## Quickstart

### Install the latest package version
```bash
pip install -i https://test.pypi.org/simple/ flaskblockly
```

### 1. Add flaskblockly to your project
`app.py`:
```python
from flask import Flask 
from flaskblockly import Blockly

app = Flask(__name__)
Blockly(app)
```

Blockly will register a route in the app (`/blockly` by default) that will currently serve 2 files:
* `foo.html`
* `bar.html`

### 2. Run the app
```bash
flask run
```
Navigate to both `/blockly/foo.html` & `/blockly/bar.html` and observe the files being served.

### 3. Overwrite static files
By default, the `blockly_static` folder is used to overwrite the static files served by Blockly.

Create the following folder structure inside your project:
```
flaskblockly-demo/
├── app.py
└── blockly_static/
    └── foo.html
```

Write any valid HTML in `foo.html`. Restart the app and navigate to `/blockly/foo.html`, the app should serve your custom static file instead.

## Configuration
`flaskblockly` currently supports the following configuration options:
* `endpoint`: specifies the route used inside your app (default `/blockly`)
* `user_static_folder`: name of the folder that will be used for static files overwrites (default `blockly_static`)

### Usage
```python
from flask import Flask 
from flaskblockly import Blockly

app = Flask(__name__)
Blockly(app, config={'endpoint': 'blocklyy', 'user_static_folder': 'user_static'})
```