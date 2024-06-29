from flask import Blueprint, render_template

r_d_bp = Blueprint('r_d_bp', __name__)

@r_d_bp.route('/r_d')
def show_r_d():
    return render_template('r_d.html')

@r_d_bp.route('/history_of_architecture')
def history_of_architecture():
    return render_template('history_of_architecture.html')
