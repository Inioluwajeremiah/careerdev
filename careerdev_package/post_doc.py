from flask import Blueprint, app, flash, render_template, request
from careerdev_package.models import PostModel
from flask_login import login_required, current_user


post_doc = Blueprint('post_doc', __name__)

@post_doc.route('/postdoc')
def all_post_doc_posts():
    rows_per_page = 10
    page = request.args.get('page', 1, type=int)
    # post_doc_posts = PostModel.query.paginate(page=page, per_page = rows_per_page )
    post_doc_post = PostModel.query.filter_by(post_cat='Post Doc')
    post_doc_posts = post_doc_post.paginate(page=page, per_page=rows_per_page )
   
    return render_template('post_doc.html', post_doc_posts=post_doc_posts, user=current_user)

@post_doc.route('/postdoc/details')
def all_post_doc_details():
    rows_per_page = 1
    page = request.args.get('page', 1, type=int)
    # post_doc_posts = PostModel.query.paginate(page=page, per_page = rows_per_page )
    post_doc_detail = PostModel.query.filter_by(post_cat='Post Doc')
    post_doc_details = post_doc_detail.paginate(page=page, per_page=rows_per_page )
   
    return render_template('postDocAllDetails.html', post_doc_details=post_doc_details, user=current_user)


@post_doc.get("/post_doc/details/<id>")
def getInternPage(id):

    int_id = int(id)
    # rpt1= int(id)+1
    # rpt2 = int(id)+2
    # rpt3 = int(id)+3
    # rpt4 = int(id)+4
    # rpt5 = int(id)+5
    # rpt6 = int(id)+6
    rpt1= int_id+1
    rpt2 = int_id+2
    rpt3 = int_id+3
    rpt4 = int_id+4
    rpt5 = int_id+5
    rpt6 = int_id+6

    ids = [rpt1,rpt2,rpt3,rpt4,rpt5,rpt6]

    singlePost = PostModel.query.filter_by(id=id).first()
    # rel_sp_1 = PostModel.query.filter_by(id=rpt1).first()
    # rel_sp_2 = PostModel.query.filter_by(id=rpt2).first()
    # rel_sp_3 = PostModel.query.filter_by(id=rpt3).first()
    # rel_sp_4 = PostModel.query.filter_by(id=rpt4).first()
    # rel_sp_5 = PostModel.query.filter_by(id=rpt5).first()
    # rel_sp_6 = PostModel.query.filter_by(id=rpt6).first()
    related_posts = PostModel.query.filter_by(post_cat="Post Doc").filter(PostModel.id.in_(ids)).all()

    return render_template('post_docDetails.html', singlePost=singlePost, user=current_user, related_posts=related_posts)
        # rel_sp_1=rel_sp_1,rel_sp_2=rel_sp_2,rel_sp_3=rel_sp_3,rel_sp_4=rel_sp_4,rel_sp_5=rel_sp_5,rel_sp_6=rel_sp_6


