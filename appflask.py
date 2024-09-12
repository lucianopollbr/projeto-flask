from flask import Flask, send_from_directory

appflask = Flask(__name__)

@appflask.route('/')
def serve_index():
    return send_from_directory('site/', 'index.html')

@appflask.route('/hamburger.jpg')
def hamburger():
    return send_from_directory('site', 'hamburger.jpg')

@appflask.route('/tablesetting2.jpg')
def tablesetting2():
    return send_from_directory('site', 'tablesetting2.jpg')

@appflask.route('/tablesetting.jpg')
def tablesetting():
    return send_from_directory('site', 'tablesetting.jpg')

@appflask.route('/favicon.ico')
def favicon():
    return send_from_directory('venv', 'favicon.ico')

@appflask.route('/test')
def test():
    return "Flask está funcionando!"

if __name__ == '__main__':
    appflask.run(host='0.0.0.0', port=3001)

