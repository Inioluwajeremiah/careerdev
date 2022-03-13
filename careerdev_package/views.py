from crypt import methods
from flask import Blueprint, app, flash
from flask.json import jsonify
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from careerdev_package.models import PostModel
import json
from . import db
from .models import User, PostModel

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def dataPage():
    # return redirect(request.url)
    # allRecords = PostModel.query.all()
    # print(allRecords)
    # if not allRecords:
    #     # return render_template('main.html', allRecords = allRecords)
    #     return render_template('index.html', user=current_user)
    # else:
    #     return render_template('index.html', allRecords=allRecords, user=current_user)
    grad_assistantship = PostModel.query.filter_by(post_cat='Graduate Assistantship').all()
    scholarship = PostModel.query.filter_by(post_cat='Scholarship').all()
    internship = PostModel.query.filter_by(post_cat="Internship").all()
    post_doc = PostModel.query.filter_by(post_cat='Post Doc').all()

    return render_template('index.html', user=current_user, grad_ast_post = grad_assistantship, sch_post = scholarship, 
                intern_posts = internship, post_doc_post = post_doc)


