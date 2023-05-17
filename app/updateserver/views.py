from flask import request, Blueprint
from git import Repo
updateserver = Blueprint("updateserver", __name__)

@updateserver.route('/update_server', methods=['POST'])
def webhook():
    print('in webhook fx')
    if request.method == 'POST':
        print(f'Before repo assignment')
        repo = Repo('/home/chrism/flask_application_prototype')
        #repo = Repo('/home/chris/bailey-tech/source-code/flask_application_prototype')
        print(f'repo {repo}')
        origin = repo.remotes.origin
        print(f'origin {origin}')
        origin.pull('https://github.com/chris-mastic/flask_application_prototype', 'master')
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
