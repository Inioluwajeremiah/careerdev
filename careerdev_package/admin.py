from flask import Blueprint, flash
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from careerdev_package.models import PostModel
from . import db
from .models import User, PostModel

admin = Blueprint('admin', __name__)


# ADMIN ADD NEW POSTS
@admin.route('/59b1a640e436ba17c3454d935f9b6038/postform', methods=['GET', 'POST'])
@login_required
def addNewPosts():
    if request.method == "POST":

        if request.form.get('add__post') == "POST":
            post_cat = request.form.get('post_cat')
            ga = request.form.get('ga')
            title = request.form.get('title')
            subtitle = request.form.get('subtitle')
            country = request.form.get('country')
            institution = request.form.get('institution')
            faculty = request.form.get('faculty')
            department = request.form.get('department')
            course = request.form.get('course')
            level = request.form.get('level')
            description = request.form.get('description')
            duration = request.form.get('duration')
            appfee = request.form.get('appfee')
            app_url = request.form.get('url')
            fund_type = request.form.get('fund_type')
            fund_inst = request.form.get('fund_inst')
            app_sd = request.form.get('app_sd')
            app_ed = request.form.get('app_ed')
            
            if not post_cat:
                flash("Fill Post cat. field appropriately", category='success')
            elif len(title) < 2:
                flash("Fill title field appropriately", category='success')
            elif ga == "":
                flash("Fill GA field appropriately", category='success')
            elif len(subtitle) < 2:
                flash("Fill subtitle field appropriately", category='success')
            elif len(country) < 2:
                flash("Fill country field appropriately", category='success')
            elif len(institution) < 2:
                flash("Fill institution field appropriately", category='success')
            elif len(faculty) < 2:
                flash("Fill faculty field appropriately", category='success')
            elif len(department) < 2:
                flash("Fill department field appropriately", category='success')
            elif len(course) < 2:
                flash("Fill course field appropriately", category='success')
            elif len(level) < 2:
                flash("Fill level field appropriately", category='success')
            elif len(description) < 2:
                flash("Fill description field appropriately", category='success')
            elif len(duration) < 2:
                flash("Fill duration field appropriately", category='success')
            elif appfee == "":
                flash("Fill appfee field appropriately", category='success')
            elif len(app_url) < 2:
                flash("Fill url field appropriately", category='success')
            elif len(fund_type)< 5:
                flash("Fill fund_type field appropriately", category='success')
            elif fund_inst == "":
                flash("Fill funding institution field appropriately", category='success')
            elif not app_sd:
                flash("Fill application start date field appropriately", category='success')
            elif not app_ed:
                flash("Fill application end date field appropriately", category='success')
            else:
               
                newPosts = PostModel(ga=ga, post_cat=post_cat, title=title, subtitle=subtitle, country=country,
                                          institution=institution, faculty=faculty, department=department,
                                          course=course, level=level, description=description, duration=duration,
                                          appfee=appfee, fund_type=fund_type, app_url=app_url,fund_inst=fund_inst, app_sd=app_sd, app_ed=app_ed)
                db.session.add(newPosts)
                db.session.commit()

                flash("Post added successfully", category='success')
                return render_template('postform.html', user=current_user)
        # else:
        return render_template('postform.html', user=current_user, ga=ga, title=title, subtitle=subtitle,
                           institution=institution, faculty=faculty, department=department,
                           course=course, level=level, description=description, duration=duration,
                           appfee=appfee, app_url=app_url, country=country, fund_type=fund_type)

    return render_template('postform.html', user=current_user)

# GET ALL ADMIN POST (IND)
@admin.route('/59b1a640e436ba17c3454d935f9b6038/ad_posts')
@login_required
def  ad_posts():  
    rows_per_page = 5
    if request.method == 'POST':
        post = request.form.get('post-no')

        rows_per_page = post  
        page = request.args.get('page', 1, type=int)
        postRecords = PostModel.query.filter_by(id=current_user.get_id()).paginate(page=page, per_page = rows_per_page )
        return render_template('adminMain.html', postRecords=postRecords, user=current_user)
        
    page = request.args.get('page', 1, type=int)
    postRecords = PostModel.query.filter_by(id=current_user.get_id()).paginate(page=page, per_page = rows_per_page )
    if not postRecords:
        return render_template('adminMain.html', user=current_user)
    else:
        return render_template('adminMain.html', postRecords=postRecords, user=current_user)

#  S E A R C H ADMIN POST (IND)
@admin.route('/59b1a640e436ba17c3454d935f9b6038/search', methods=['POST'])
@login_required
def search():
    rows_per_page = 5
    page = request.args.get('page', 1, type=int)
    allRecords = User.query.all()
    if request.method == "POST":
        if request.form.get('adm-search') == 'Search':
            searchvalue = request.form.get('adm-search-text').upper()
            search_cat = request.form.get('admin-filter')

            if not searchvalue:
                flash('Search field is empty', category='error')
                return redirect(url_for('admin.admin_posts', allRecords=allRecords, user=current_user))
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


                # subtitle_result =PostModel.query.filter_by(subtitletitle=searchvalue)              
                # app_url_result =PostModel.query.filter_by(app_url=searchvalue)
                # getSR = subtitle_result.paginate(page=page, per_page=rows_per_page )
                # getAPR = app_url_result.paginate(page=page, per_page=rows_per_page )
    else:
        return render_template('adminSearch.html', user=current_user)
            
    return redirect(url_for('admin.admin_posts', allRecords=allRecords, user=current_user))

@admin.route("/forbidden", methods=['GET', 'POST'])
@login_required
def protected():
    return redirect(url_for('forbidden.html'))


#   EDIT POST RECORDS (IND)
@admin.route("/59b1a640e436ba17c3454d935f9b6038/edit/<id>")
@login_required
def editRecord(id):
    editRecord = PostModel.query.filter_by(id=id)
    return render_template('adminUpdate.html', edit_record=editRecord, user=current_user)


#  UPDATE ADMIN POST (IND)
@admin.route("/59b1a640e436ba17c3454d935f9b6038/update/<id>", methods=['POST'])
@login_required
def updateRecord(id):

    user_id = current_user.get_id()
    postRecords = PostModel.query.all()
    if request.method == "POST":
        
        if request.form.get('update') == "Update":
            ga = request.form.get('uga')
            title = request.form.get('utitle')
            subtitle = request.form.get('usubtitle')
            country = request.form.get('ucountry')
            institution = request.form.get('uinstitution')
            faculty = request.form.get('ufaculty')
            department = request.form.get('udepartment')
            course = request.form.get('ucourse')
            level = request.form.get('ulevel')
            description = request.form.get('udescription')
            duration = request.form.get('uduration')
            appfee = request.form.get('uappfee')
            fund_type = request.form.get('ufund_type')
            fund_inst = request.form.get('ufund_inst')
            app_url = request.form.get('uurl')
            post_cat = request.form.get('upost_cat')
            app_sd = request.form.get('uapp_sd')
            app_ed = request.form.get('uapp_ed')

            edit_record = PostModel.query.filter_by(id=id).first()
            edit_record.user_id = user_id
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
            edit_record.fund_type = fund_type
            edit_record.fund_inst = fund_inst
            edit_record.app_url = app_url
            edit_record.post_cat = post_cat
            edit_record.app_sd = app_sd
            edit_record.app_ed = app_ed
            
            db.session.commit()

            flash("Update successful", category='success')
            return redirect(url_for('admin.admin_posts', postRecords=postRecords, user=current_user))
            # return redirect(url_for('dataPage'))

    return render_template('adminUpdate.html', user=current_user)


# D E L E T E   ADMIN POST (IND)
@admin.route("/59b1a640e436ba17c3454d935f9b6038/delete/<id>")
@login_required
def admDelete(id):
    deleteUser = PostModel.query.filter_by(id=id).first()
    db.session.delete(deleteUser)
    db.session.commit()
    return redirect(url_for('admin.admin_posts'))
