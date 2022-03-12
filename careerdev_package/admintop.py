from flask import Blueprint, app, flash
from flask.json import jsonify
from werkzeug.security import  generate_password_hash
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from careerdev_package.models import PostModel
import json
from . import db
from .models import User, PostModel

admintop = Blueprint('admintop', __name__)

#  GET ALL ADMIN POSTS
@admintop.route('/84bd27f938b67f470da3231c14b3448f/adminPosts', methods=['GET','POST'])
@login_required
def get_all_posts():
    # , methods=['POST']
    rows_per_page = 5
    # postRecords = PostModel.query.all() 
    if request.method == 'POST':
        post = request.form.get('post-no')

        rows_per_page = post  
        page = request.args.get('page', 1, type=int)
        postRecords = PostModel.query.paginate(page=page, per_page = rows_per_page )
        # postRecords = 
        return render_template('admintopMain.html', postRecords=postRecords, user=current_user)
        
    page = request.args.get('page', 1, type=int)
    postRecords = PostModel.query.paginate(page=page, per_page = rows_per_page )
    # postRecords = PostModel.query.filter_by(post_cat='Scholarship').paginate(page=page, per_page = rows_per_page )
    if not postRecords:
        return render_template('admintopMain.html', user=current_user)
    else:
        return render_template('admintopMain.html', postRecords=postRecords, user=current_user)

# E D I T ALL ADMIN POST RECORDS
@admintop.route("/84bd27f938b67f470da3231c14b3448f/ad_posts/edit/<id>", methods=['GET', 'POST'])
@login_required
def adtEditRecord(id):
    editAdminRecord = PostModel.query.filter_by(id=id)
    # return redirect(request.url)
    return redirect(url_for('admintop.adtUpdateRecord', edit_record=editAdminRecord, user=current_user))

#  U P D A T E ALL ADMIN POSTS
@admintop.route("/84bd27f938b67f470da3231c14b3448f/ad_posts/update/<id>", methods=['POST'])
@login_required
def adtUpdateRecord(id):
    postRecords = PostModel.query.all()
    if request.method == "POST":
        
        if request.form.get('adt-update') == "Update":
            post_cat = request.form.get('adtpost_cat')
            ga = request.form.get('adtga')
            title = request.form.get('adttitle')
            subtitle = request.form.get('adtsubtitle')
            country = request.form.get('adtcountry')
            institution = request.form.get('adtinstitution')
            faculty = request.form.get('adtfaculty')
            department = request.form.get('adtdepartment')
            course = request.form.get('adtcourse')
            level = request.form.get('adtlevel')
            description = request.form.get('adtdescription')
            duration = request.form.get('adtduration')
            appfee = request.form.get('adtappfee')
            app_url = request.form.get('adturl')
            country = request.form.get('adtcountry')
            fund_type = request.form.get('adtfund_type')
            app_sd = request.form.get('adtapp_sd')
            app_ed = request.form.get('adtapp_ed')
            fund_inst = request.form.get('adtfund_inst')

            edit_record = PostModel.query.filter_by(id=id).first()
            edit_record.ga = ga 
            edit_record.title = title
            edit_record.subtitle = subtitle 
            edit_record.country = country
            edit_record.institution = institution 
            edit_record.faculty = faculty
            edit_record.department = department
            edit_record.course = course
            edit_record.level = level
            edit_record.description = description
            edit_record.duration = duration
            edit_record.appfee = appfee
            edit_record.app_url = app_url
            edit_record.fund_type = fund_type
            edit_record.fund_inst = fund_inst
            edit_record.post_cat = post_cat
            edit_record.app_sd = app_sd
            edit_record.app_ed = app_ed
            
            db.session.commit()

            flash("Update successful", category='success')
            return redirect(url_for('admintop.get_all_posts', postRecords=postRecords, user=current_user))

    return render_template('admintopUpdate.html', user=current_user)

# FILTER ALL ADMIN POSTS
@admintop.route('/84bd27f938b67f470da3231c14b3448f/search', methods=['POST'])
@login_required
def adt_search():
    allRecords = PostModel.query.all()
    rows_per_page = 5
    page = request.args.get('page', 1, type=int)
    if request.method == "POST":
        if request.form.get('adt-search') == 'Search':
            searchvalue = request.form.get('adt-search-text').upper()
            search_cat = request.form.get('adt-filter')
            if not searchvalue:
                flash("Search field cannot be empty", category='error')
                return render_template('admintopMain.html', allRecords=allRecords, user=current_user)
            elif searchvalue and search_cat == "App. startdate":
                app_sd_result =PostModel.query.filter_by(app_sd=searchvalue)
                getSDR = app_sd_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getSDR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "App. enddate":
                app_ed_result =PostModel.query.filter_by(app_ed=searchvalue)
                getEDR = app_ed_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getEDR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "App. fee":
                appfee_result =PostModel.query.filter_by(appfee=searchvalue)
                getAR = appfee_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getAR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Category":
                post_cat_result =PostModel.query.filter_by(post_cat=searchvalue)
                getPCR = post_cat_result.paginate(page=page, per_page=rows_per_page)
                return render_template('adminSearch.html', user=current_user, searchResult = getPCR, searchvalue=searchvalue)
            elif searchvalue and search_cat=="Title":
                title_result = PostModel.query.filter_by(title=searchvalue)
                getTR = title_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getTR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Country":
                country_result =PostModel.query.filter_by(country=searchvalue)
                getCR = country_result.paginate(page=page, per_page=rows_per_page)
                return render_template('adminSearch.html', user=current_user, searchResult = getCR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Course":
                course_result =PostModel.query.filter_by(course=searchvalue)
                getCSR = course_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getCSR, searchvalue=searchvalue)    
            elif searchvalue and search_cat == 'Department':
                department_result =PostModel.query.filter_by(department=searchvalue)
                getDR = department_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getDR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Description":
                description_result =PostModel.query.filter_by(description=searchvalue)
                getDCR = description_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getDCR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Duration":
                duration_result =PostModel.query.filter_by(duration=searchvalue)
                getDRT = duration_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getDRT, searchvalue=searchvalue)       
            elif searchvalue and search_cat == "Faculty":
                faculty_result =PostModel.query.filter_by(faculty=searchvalue) 
                getFR = faculty_result.paginate(page=page, per_page=rows_per_page)
                return render_template('adminSearch.html', user=current_user, searchResult = getFR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Entry type":
                level_result =PostModel.query.filter_by(level=searchvalue)
                getLR = level_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getLR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Funding institution":
                fund_inst_result =PostModel.query.filter_by(fund_inst=searchvalue)
                getIT = fund_inst_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getIT, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Funding type":
                fund_type_result =PostModel.query.filter_by(fund_type=searchvalue)
                getFT = fund_type_result.paginate(page=page, per_page=rows_per_page )
                return render_template('adminSearch.html', user=current_user, searchResult = getFT, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Institution":
                institution_result =PostModel.query.filter_by(institution=searchvalue)
                getIR = institution_result.paginate(page=page, per_page=rows_per_page ) 
                return render_template('adminSearch.html', user=current_user, searchResult = getIR, searchvalue=searchvalue)
            elif searchvalue and search_cat == "Subtitle":
                subtitle_result =PostModel.query.filter_by(subtitle=searchvalue)
                getSBT = subtitle_result.paginate(page=page, per_page=rows_per_page ) 
                return render_template('adminSearch.html', user=current_user, searchResult = getSBT, searchvalue=searchvalue)
            elif searchvalue and search_cat == "URL":
                url_result =PostModel.query.filter_by(url=searchvalue)
                getURL = url_result.paginate(page=page, per_page=rows_per_page ) 
                return render_template('adminSearch.html', user=current_user, searchResult = getURL, searchvalue=searchvalue)
            else:
                return render_template('adminSearch.html', user=current_user)
        return render_template('admintopMain.html', user=current_user, allRecords=allRecords)
    return render_template('admintopMain.html', user=current_user, allRecords=allRecords)

# D E L E T E ADMIN POSTS
@admintop.route("/84bd27f938b67f470da3231c14b3448f/ad_posts/delete/<id>")
@login_required
def delete(id):
    deleteUser = PostModel.query.filter_by(id=id).first()
    db.session.delete(deleteUser)
    db.session.commit()
    return render_template('admintopMain.html', user=current_user)

#  GET ALL USER ADMIN  RECORDS
@admintop.route("/84bd27f938b67f470da3231c14b3448f/ad_users")
@login_required
def adtUserRecords():
    rows_per_page = 5
    page = request.args.get('page', 1, type=int)
    admin_records = User.query
    adminRecords = admin_records.paginate(page=page, per_page=rows_per_page )
    
    return render_template('adminUserMain.html', user=current_user, adminRecords=adminRecords)

# Search ALL admin users BY THHEIR USERNAMES
@admintop.route('/84bd27f938b67f470da3231c14b3448f/ad_users/search', methods=['POST'])
@login_required
def adtUserSearch():
    rows_per_page = 10
    page = request.args.get('page', 1, type=int)
    admin_Records = User.query
    adminRecords = admin_Records.paginate(page=page, per_page=rows_per_page )
    
    if request.method == "POST":
        if request.form.get('adtu-search') == 'Search':

            searchvalue = request.form.get('adtu-search-text')
            
            if not searchvalue:
                flash("Search fields cannot be empty", category="error")
                return render_template('adminUserMain.html', adminRecords=adminRecords, user=current_user)
            else:
                searchUsers = User.query.filter_by(
                    username=searchvalue)
                adminRecords = searchUsers.paginate(page=page, per_page=rows_per_page )
                return render_template('adminUserSearch.html', searchUsers=searchUsers, user=current_user)
        return render_template('adminUserMain.html', user=current_user, allRecords=admin_Records)
    return render_template('adminUserMain.html', user=current_user, allRecords=admin_Records)

# E D I T ALL ADMIN USER RECORDS
@admintop.route("/84bd27f938b67f470da3231c14b3448f/ad_users/edit/<id>", methods=['GET', 'POST'])
@login_required
def adtUserEditRecord(id):
    editAdminRecord = User.query.filter_by(id=id)
    # return redirect(request.url)
    return redirect(url_for('admintop.adtUpdateAdminUserRecord',edit_record=editAdminRecord, user=current_user))

#  U P D A T E ALL ADMIN USER RECORDS
@admintop.route("/84bd27f938b67f470da3231c14b3448f/adt_users/update/<id>", methods=['POST'])
@login_required
def adtUpdateAdminUserRecord(id):

    if request.method == "POST":
        postRecords = User.query.all()
        if request.form.get('adtu-update') == "Update":
            useremail = request.form.get('adtu-email')
            username = request.form.get('adtu-name')
            password = request.form.get('adtu-pass')
            cpassword = request.form.get('adtu-cpass')
            if len (useremail) < 4:
                flash("Please, enter your correct email", category='error')
                return render_template('adminRegister.html', user=current_user)
            elif len (username) < 3:
                flash("Please, enter your username (at least 3 chars) ", category='error')
                return render_template('adminRegister.html', user=current_user)
            elif user:
                flash("User already exists",  category='error')
                return render_template('adminRegister.html', user=current_user)
            elif password != cpassword:
                flash('Password does not match!', category='error')
                return render_template('adminRegister.html', user=current_user)
            else:
                #  username and password == cpassword:
                hashedPassword = generate_password_hash(password)

                update_user_record = User.query.filter_by(id=id).first()
                update_user_record.username = username
                update_user_record.useremail = useremail
                update_user_record.password = hashedPassword
                db.session.commit()

                flash("Update successful", category='success')
                return redirect(url_for('admintop.get_all_posts', postRecords=postRecords, user=current_user))
    return render_template('update.html', user=current_user)

# D E L E T E ADMIN USER
@admintop.route("/84bd27f938b67f470da3231c14b3448f/adt_users/delete/<id>")
@login_required
def adtDelete(id):
    deleteUser = User.query.filter_by(id=id).first()
    db.session.delete(deleteUser)
    db.session.commit()
    return render_template('adminUserMain.html', user=current_user)