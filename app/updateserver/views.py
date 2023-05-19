from flask import request, Blueprint
from git import Repo
updateserver = Blueprint("updateserver", __name__)

@updateserver.route('/update_server', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        repo = Repo('/home/chrism/flask_application_prototype')
        # repo = Repo('/home/chris/bailey-tech/source-code/flask_application_prototype')
        origin = repo.remotes.origin
        repo.create_head('master',
                         origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400

