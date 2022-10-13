import re
from flask import *
from ordersys.db import get_db
from flask_login import login_required, current_user
from ordersys.enums import *

bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/new', methods=('GET', 'POST'))
@login_required
def new_order():
    db = get_db()
    cur = db.cursor()
    
    item_costs = 0

    if request.method == 'POST':
        if request.form['vendor'] == 'Other':
            vendor = request.form['vendor-other-name']
            vendor_url = request.form['vendor-other-url']
        else:
            vendor = request.form['vendor']
            vendor_url = vendors[vendor]
        
        order_data = (
            current_user.project_id,
            vendor,
            vendor_url,
            request.form['order-date'],
            request.form['order-speed'],
        )
        
        cur.execute('INSERT INTO eorder (project_id, vendor, vendor_url, order_time, shipping_speed) VALUES (?, ?, ?, ?, ?)', order_data)
        order_id = cur.lastrowid

        db.commit()

        item_nums = set()
        for f_re in request.form:
            c_item_num = f_re.split('-')[-1]
            if c_item_num.isnumeric() and c_item_num not in item_nums:
                item_nums.add(c_item_num)
        
        for item_num in item_nums:
            item_costs += float(request.form['item-price-' + item_num])
            item_data = (
                order_id,
                request.form['item-description-' + item_num],
                request.form['item-number-' + item_num],
                request.form['item-price-' + item_num],
                request.form['item-quantity-' + item_num],
                request.form['item-justification-' + item_num]
            )

            db.execute('INSERT INTO item (order_id, description, item_number, price, quantity, justification) VALUES (?, ?, ?, ?, ?, ?)', item_data)
            db.commit()
        
        db.execute(f'UPDATE eorder SET item_costs = {str(item_costs)} WHERE id = {order_id}')
        db.commit()
        
        return redirect(url_for('project.index'))

    return render_template('order/new.html', vendors=vendors)