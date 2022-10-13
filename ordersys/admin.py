from flask import *
from ordersys.db import get_db
from flask_login import login_required
from ordersys.auth import admin_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=('GET', 'POST'))
@login_required
@admin_required
def index():
    db = get_db()
    
    if request.method == 'POST':
        if request.form['add-type'] == 'project':
            project_name = request.form['project-name']
            db.execute('INSERT INTO project (name) VALUES (?)', (project_name,))
            db.commit()
        else:
            user_data = (
                str(request.form['project-id']), 
                request.form['user-name'],
                request.form['email'] + '@bucknell.edu', 1
                )
            db.execute(
                'INSERT INTO user (project_id, name, email, auth_level) VALUES (?, ?, ?, ?);', user_data
            )
            db.commit()

    projects = db.execute(
        'SELECT p.id AS project_id, u.name AS user_name, p.name AS project_name, p.total AS total FROM project p LEFT JOIN user u ON p.id = u.project_id'
    ).fetchall()

    return render_template('admin/index.html', projects=projects)

@bp.route('/delete/<project_id>')
@login_required
@admin_required
def delete_project(project_id):
    db = get_db()
    
    db.execute('DELETE FROM project WHERE id = ?', (project_id,))
    db.commit()
    
    return redirect(url_for('admin.index'))