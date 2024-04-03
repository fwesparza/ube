from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from app.models import Order, Item, ItemType, Table, OrderedItem, Order
from app.forms.AddItem import AddItemForm

bp = Blueprint("orders", __name__, url_prefix="")

@bp.route("/")
@login_required
def index():
    orders = Order.query.filter_by(employee_id = current_user.id).all()
    return render_template("orders.html", orders=orders)


@bp.route("/update-order", methods=["GET"])
def updateOrder():
    form = AddItemForm()
    path='orders.updateOrder'
    title = 'Update Order'
    return render_template("forms/form.html", form=form, title=title, path=path)


@bp.route("/create-order", methods=["GET"])
def createOrder():
    return "<h1>Create Order</h1>"