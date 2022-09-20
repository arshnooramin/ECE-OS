from flask import *
from markupsafe import escape
from ordersys.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        db = get_db()
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user:
            project = db.execute(
                'SELECT * FROM project p JOIN user u ON p.user_id = u.id WHERE u.id = ?', (user["id"],)
            ).fetchone()
            
            if project:
                return redirect(url_for('project.index', project_id=project["id"]))
            else:
                flash('No projects found.')

        else:
            flash('Incorrect username.')
    
    return render_template('auth/login.html')



