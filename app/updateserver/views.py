from flask import request, Blueprint
from git import Repo
updateserver = Blueprint("updateserver", __name__)

@updateserver.route('/update_server', methods=['POST','GET'])
def webhook():
    print('in webhook')
    if request.method == 'GET':
        print(f'Before repo assignment')
        #repo = Repo('https://github.com/chris-mastic/flask_application_prototype.git')
        repo = Repo('/home/chris/bailey-tech/source-code/flask_application_prototype')
        print(f'repo {repo}')
        origin = repo.remotes.origin
        print(f'origin {origin}')
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
