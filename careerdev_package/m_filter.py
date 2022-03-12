from flask import Blueprint, app, flash
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from careerdev_package.models import PostModel
from . import db
from .models import User, PostModel

m_filter = Blueprint('m_filter', __name__)

@m_filter.route('/filter', methods=['GET', 'POST'])
def filterPost():
    return render_template('filter.html', user=current_user)
