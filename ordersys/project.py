from flask import *
from ordersys.db import get_db

bp = Blueprint('project', __name__, url_prefix='/project')

@bp.route('/<project_id>')
def index(project_id):
    db = get_db()
    project = db.execute(
        'SELECT * FROM project WHERE id = ?', (project_id,)
    ).fetchone()
    orders = db.execute(
        'SELECT o.id, o.vendor FROM eorder o JOIN project p ON p.id = o.project_id WHERE p.id = ? ORDER BY created DESC', (project_id,)
    ).fetchall()
    
    return render_template('project/index.html', project=project, orders=orders)