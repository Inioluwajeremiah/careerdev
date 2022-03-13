from flask import Blueprint, app, flash, render_template, request
from careerdev_package.models import PostModel
from flask_login import login_required, current_user

ga_ast = Blueprint('ga_ast', __name__)

@ga_ast.route('/graduateasst')
def all_ga_post():

    rows_per_page = 10
    page = request.args.get('page', 1, type=int)
    # grad_assistantships = PostModel.query.paginate(page=page, per_page = rows_per_page )
    grad_assistantship = PostModel.query.filter_by(post_cat='Graduate Assistantship')
    grad_assistantships = grad_assistantship.paginate(page=page, per_page=rows_per_page )
    if not grad_assistantships:
        # return render_template('scholarship.html', user=current_user)
        flash("No recent posts", category="error")
    else:
        return render_template('ga.html', grad_assistantships=grad_assistantships, user=current_user)
    # grad_assistantship = PostModel.query.filter_by(post_cat='Graduate Assistantship').all()
    return render_template('ga.html', grad_assistantships = grad_assistantships, user=current_user)

@ga_ast.route('/graduateassist/details')
def details_all_ga_post():

    rows_per_page = 1
    page = request.args.get('page', 1, type=int)
    # grad_assistantships = PostModel.query.paginate(page=page, per_page = rows_per_page )
    grad_assistantship = PostModel.query.filter_by(post_cat='Graduate Assistantship')
    grad_assistantships = grad_assistantship.paginate(page=page, per_page=rows_per_page )
    if not grad_assistantships:
        # return render_template('scholarship.html', user=current_user)
        flash("No recent posts", category="error")
        return render_template('gaDetails2.html', user=current_user)
    
    return render_template('gaDetails2.html', grad_assistantships=grad_assistantships, user=current_user)
    
    


@ga_ast.get("/graduateasst/details/<id>")
def getSchPage(id):

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
    related_posts = PostModel.query.filter(PostModel.id.in_(ids)).all()

    if not singlePost:
        flash("Post does not exiast", category="error")
    else:
        return render_template('gaDetails.html', singlePost=singlePost, user=current_user, related_posts=related_posts)
        # rel_sp_1=rel_sp_1,rel_sp_2=rel_sp_2,rel_sp_3=rel_sp_3,rel_sp_4=rel_sp_4,rel_sp_5=rel_sp_5,rel_sp_6=rel_sp_6
