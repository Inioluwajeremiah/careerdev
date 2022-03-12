
from turtle import title
import pymysql
import json
from flask import Blueprint, jsonify, flash, make_response
import pandas as pd
from flask import render_template, request
from flask_login import current_user
from .models import PostModel
from sqlalchemy import create_engine

m_search = Blueprint('m_search', __name__)

@m_search.route('/ssearch_result', methods=["GET", "POST"])
def searchData():
    getPOsts = PostModel.query.filter_by(title='')
    if request.method == "POST":

        # if request.form.get('user-search-btn') == "Search":
        # students_records = json.loads(request.data)
        # userSearch = students_records['textvalue']
        # getJasonData = request.get_json()
        getJasonData = json.loads(request.data)
        userSearch = getJasonData['textvalue']
        if userSearch:
            # userSearch = request.get_json()
            id = []
            user_id = []
            title=[]
            subtitle=[]
            country=[]
            institution=[]
            faculty=[]
            department=[]
            course=[]
            level=[]
            description =[]
            duration=[]
            appfee=[]
            fund_type=[]
            fund_inst=[]
            app_url=[]
            app_short_url=[]
            post_cat=[]
            app_sd=[]
            app_ed=[]
            visits=[]
            date_created=[]
            date_updated=[]

            rows_per_page = 5
            page = request.args.get('page', 1, type=int)

            allPosts = PostModel.query.filter_by(appfee=userSearch)
            allPosts_toPD = PostModel.query
            for post_to_pd in allPosts_toPD:
                id.append(post_to_pd.id)
                user_id.append(post_to_pd.user_id)
                title.append(post_to_pd.title)
                subtitle.append(post_to_pd.subtitle)
                country.append(post_to_pd.country)
                institution.append(post_to_pd.institution)
                faculty.append(post_to_pd.faculty)
                department.append(post_to_pd.department)
                course.append(post_to_pd.course)
                level.append(post_to_pd.description)
                description.append(post_to_pd.description)
                duration.append(post_to_pd.duration)
                appfee.append(post_to_pd.appfee)
                fund_type.append(post_to_pd.fund_type)
                fund_inst.append(post_to_pd.fund_inst)
                app_url.append(post_to_pd.app_url)
                app_short_url.append(post_to_pd.app_short_url)
                post_cat.append(post_to_pd.post_cat)
                app_sd.append(post_to_pd.app_sd)
                app_ed.append(post_to_pd.app_ed)
                visits.append(post_to_pd.visits)
                date_created.append(post_to_pd.date_created)
                date_updated.append(post_to_pd.date_updated)
            
            data_tuples = list(zip(id, user_id,title, subtitle,country, institution, faculty,department, course, level,description,
                    duration, appfee,fund_type,fund_inst,app_url,app_short_url,post_cat,app_sd,app_ed,visits,date_created,date_updated))
            table_its = pd.DataFrame(data_tuples, columns=['id','user_id','title', 'subtitle','country','institution','faculty','department','course','level','description',
                    'duration', 'appfee','fund_type','fund_inst','app_url','app_short_url','post_cat','app_sd','app_ed','visits','date_created','date_updated'])
            table_its.to_csv('carrer_dev.csv', index=False)

            # table_its.astype(str)

            # flash("Data saved successfully", category='success')

            search_result =  table_its[table_its.eq(userSearch).any(1)]
            
            search_result .to_csv('search_result.csv', index=False)
            # search_table = pd.read_csv('search_result.csv')
            
            # search_qu = search_result.values
            # search_query = search_qu.tolist()
            search_to_string = search_result.astype(str)
            search_dict = search_to_string.to_dict()
            search_json = json.dumps(search_dict)

            return make_response (jsonify(search_json))

        rows_per_page = 5
        page = request.args.get('page', 1, type=int)
        getPosts = getPOsts.paginate(page=page, per_page=rows_per_page )

        return render_template('search.html', user=current_user, allSchPosts= getPosts)
    return render_template('search.html', user=current_user)


@m_search.route('/searc', methods=['GET'])
def searchResut():
    # if request.method == "POST":

    #     records = json.loads(request.data)
    #     search_value = records['textvalue']
    #     return render_template('search2.html', user=current_user, search_value=search_value)
    return render_template('search2.html', user=current_user)


@m_search.route('/search', methods=['GET','POST'])
def search_result():
    rows_per_page = 5
    page = request.args.get('page', 1, type=int)
    if request.method == "POST":
        if request.form.get('user-search-btn') == 'Search':
            search_cat = request.form.get('search-by')
            searchText = request.form.get('user-search')
            if not searchText and not search_cat:
                flash('Enter a valid search arguement', category='error')
                return render_template('search.html', user=current_user, searchText='')
            elif searchText and not search_cat:
                title_result = PostModel.query.filter_by(title=searchText)
                getTR = title_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getTR, searchText=searchText)
            elif searchText and search_cat == "App. startdate":
                app_sd_result =PostModel.query.filter_by(app_sd=searchText)
                getSDR = app_sd_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getSDR, searchText=searchText)
            elif searchText and search_cat == "App. enddate":
                app_ed_result =PostModel.query.filter_by(app_ed=searchText)
                getEDR = app_ed_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getEDR, searchText=searchText)
            elif searchText and search_cat == "App. fee":
                appfee_result =PostModel.query.filter_by(appfee=searchText)
                getAR = appfee_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getAR, searchText=searchText)
            elif searchText and search_cat == "Category":
                post_cat_result =PostModel.query.filter_by(post_cat=searchText)
                getPCR = post_cat_result.paginate(page=page, per_page=rows_per_page)
                return render_template('search.html', user=current_user, searchResult = getPCR, searchText=searchText)

            elif searchText and search_cat=="Title":
                title_result = PostModel.query.filter_by(title=searchText)
                getTR = title_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getTR, searchText=searchText)
            elif searchText and search_cat == "Country":
                country_result =PostModel.query.filter_by(country=searchText)
                getCR = country_result.paginate(page=page, per_page=rows_per_page)
                return render_template('search.html', user=current_user, searchResult = getCR, searchText=searchText)
            elif searchText and search_cat == "Course":
                course_result =PostModel.query.filter_by(course=searchText)
                getCSR = course_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getCSR, searchText=searchText)    
            elif searchText and search_cat == 'Department':
                department_result =PostModel.query.filter_by(department=searchText)
                getDR = department_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getDR, searchText=searchText)
            elif searchText and search_cat == "Description":
                description_result =PostModel.query.filter_by(description=searchText)
                getDCR = description_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getDCR, searchText=searchText)
            elif searchText and search_cat == "Duration":
                duration_result =PostModel.query.filter_by(duration=searchText)
                getDRT = duration_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getDRT, searchText=searchText)       
            elif searchText and search_cat == "Faculty":
                faculty_result =PostModel.query.filter_by(faculty=searchText) 
                getFR = faculty_result.paginate(page=page, per_page=rows_per_page)
                return render_template('search.html', user=current_user, searchResult = getFR, searchText=searchText)
            elif searchText and search_cat == "Entry type":
                level_result =PostModel.query.filter_by(level=searchText)
                getLR = level_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getLR, searchText=searchText)
            elif searchText and search_cat == "Funding institution":
                fund_inst_result =PostModel.query.filter_by(fund_inst=searchText)
                getIT = fund_inst_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getIT, searchText=searchText)
            elif searchText and search_cat == "Funding type":
                fund_type_result =PostModel.query.filter_by(fund_type=searchText)
                getFT = fund_type_result.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user, searchResult = getFT, searchText=searchText)
            elif searchText and search_cat == "Institution":
                institution_result =PostModel.query.filter_by(institution=searchText)
                getIR = institution_result.paginate(page=page, per_page=rows_per_page ) 
                return render_template('search.html', user=current_user, searchResult = getIR, searchText=searchText)
            else:
                return render_template('search.html', user=current_user)


                # subtitle_result =PostModel.query.filter_by(subtitletitle=searchText)              
                # app_url_result =PostModel.query.filter_by(app_url=searchText)
                # getSR = subtitle_result.paginate(page=page, per_page=rows_per_page )
                # getAPR = app_url_result.paginate(page=page, per_page=rows_per_page )
        else:
            return render_template('search.html', user=current_user)
    else:

        return render_template('search.html', user=current_user)
