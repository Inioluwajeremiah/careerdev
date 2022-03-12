@m_search.route('/search', methods=['GET', 'POST'])
def searchData():
    getPOsts = PostModel.query.filter_by(title='')
    if request.method == "POST":
        if request.form.get('user-search-btn') == "Search":
            userSearch = request.form.get('user-search')

            if not userSearch:
                flash('search filed cannot be empty', category='error')
                rows_per_page = 5
                page = request.args.get('page', 1, type=int)
                getPosts = getPOsts.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user,allSchPosts= getPosts)
            else:
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

                return search_json
            # return render_template('search.html', user=current_user)
                
            #     myposts =allPosts.paginate(page=page, per_page=rows_per_page )
            #     if not search_query:
            #         flash("No recent posts", category="error")
            #     else:
            #         return render_template('search.html', user=current_user, allSchPostsquery=allPosts, allSchPosts=myposts, search_query=search_query, userSearch=userSearch,  search_dict= search_dict)

            #     return render_template('search.html', user=current_user,allSchPostsquery=allPosts,allSchPosts=myposts,search_query=search_query, userSearch=userSearch, search_dict= search_dict)
            # return render_template('search.html', user=current_user)
        else:

            rows_per_page = 5
            page = request.args.get('page', 1, type=int)
            getPosts = getPOsts.paginate(page=page, per_page=rows_per_page )

            return render_template('search.html', user=current_user, allSchPosts= getPosts)
    return render_template('search.html', user=current_user)



# @m_search.route('/ssearch', methods=["GET", "POST"])
# def searchData():
#     getPOsts = PostModel.query.filter_by(title='')
#     # if request.method == "POST":

#     # if request.form.get('user-search-btn') == "Search":
#     # students_records = json.loads(request.data)
#     # userSearch = students_records['textvalue']
#     getJasonData = request.get_json()
#     userSearch = getJasonData.get['textvalue']
#     if userSearch:
#         # userSearch = request.get_json()
#         id = []
#         user_id = []
#         title=[]
#         subtitle=[]
#         country=[]
#         institution=[]
#         faculty=[]
#         department=[]
#         course=[]
#         level=[]
#         description =[]
#         duration=[]
#         appfee=[]
#         fund_type=[]
#         fund_inst=[]
#         app_url=[]
#         app_short_url=[]
#         post_cat=[]
#         app_sd=[]
#         app_ed=[]
#         visits=[]
#         date_created=[]
#         date_updated=[]

#         rows_per_page = 5
#         page = request.args.get('page', 1, type=int)

#         allPosts = PostModel.query.filter_by(appfee=userSearch)
#         allPosts_toPD = PostModel.query
#         for post_to_pd in allPosts_toPD:
#             id.append(post_to_pd.id)
#             user_id.append(post_to_pd.user_id)
#             title.append(post_to_pd.title)
#             subtitle.append(post_to_pd.subtitle)
#             country.append(post_to_pd.country)
#             institution.append(post_to_pd.institution)
#             faculty.append(post_to_pd.faculty)
#             department.append(post_to_pd.department)
#             course.append(post_to_pd.course)
#             level.append(post_to_pd.description)
#             description.append(post_to_pd.description)
#             duration.append(post_to_pd.duration)
#             appfee.append(post_to_pd.appfee)
#             fund_type.append(post_to_pd.fund_type)
#             fund_inst.append(post_to_pd.fund_inst)
#             app_url.append(post_to_pd.app_url)
#             app_short_url.append(post_to_pd.app_short_url)
#             post_cat.append(post_to_pd.post_cat)
#             app_sd.append(post_to_pd.app_sd)
#             app_ed.append(post_to_pd.app_ed)
#             visits.append(post_to_pd.visits)
#             date_created.append(post_to_pd.date_created)
#             date_updated.append(post_to_pd.date_updated)
        
#         data_tuples = list(zip(id, user_id,title, subtitle,country, institution, faculty,department, course, level,description,
#                 duration, appfee,fund_type,fund_inst,app_url,app_short_url,post_cat,app_sd,app_ed,visits,date_created,date_updated))
#         table_its = pd.DataFrame(data_tuples, columns=['id','user_id','title', 'subtitle','country','institution','faculty','department','course','level','description',
#                 'duration', 'appfee','fund_type','fund_inst','app_url','app_short_url','post_cat','app_sd','app_ed','visits','date_created','date_updated'])
#         table_its.to_csv('carrer_dev.csv', index=False)

#         # table_its.astype(str)

#         # flash("Data saved successfully", category='success')

#         search_result =  table_its[table_its.eq(userSearch).any(1)]
        
#         search_result .to_csv('search_result.csv', index=False)
#         # search_table = pd.read_csv('search_result.csv')
        
#         # search_qu = search_result.values
#         # search_query = search_qu.tolist()
#         search_to_string = search_result.astype(str)
#         search_dict = search_to_string.to_dict()
#         search_json = json.dumps(search_dict)

#         return make_response (jsonify(search_json))
#     else:

#         rows_per_page = 5
#         page = request.args.get('page', 1, type=int)
#         getPosts = getPOsts.paginate(page=page, per_page=rows_per_page )

#         return render_template('search.html', user=current_user, allSchPosts= getPosts)

        
    # else:

    #     rows_per_page = 5
    #     page = request.args.get('page', 1, type=int)
    #     getPosts = getPOsts.paginate(page=page, per_page=rows_per_page )

    #     return render_template('search.html', user=current_user, allSchPosts= getPosts)
    # return render_template('search.html', user=current_user)

@m_search.route('/search_result', methods=['GET','POST'])
def searchResut():
    return render_template('search2.html', user=current_user)


@m_search.route('/search', methods=['GET', 'POST'])
def searchData():
    getPOsts = PostModel.query.filter_by(title='')
    if request.method == "POST":
        if request.form.get('user-search-btn') == "Search":
            userSearch = request.form.get('user-search')

            if not userSearch:
                flash('search filed cannot be empty', category='error')
                rows_per_page = 5
                page = request.args.get('page', 1, type=int)
                getPosts = getPOsts.paginate(page=page, per_page=rows_per_page )
                return render_template('search.html', user=current_user,allSchPosts= getPosts)
            else:
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

                #  C O N V E R T  SEARCH_RESULT  TO SQL


                # search_table = pd.read_csv('search_result.csv')
                
                # search_qu = search_result.values
                # search_query = search_qu.tolist()

                # C O N V E R T  SEARCH_RESULT   TO  J S O N 
                # search_to_string = search_result.astype(str)
                # search_dict = search_to_string.to_dict()
                # search_json = json.dumps(search_dict)
                # return make_response(jsonify(search_json))
            # return render_template('search.html', user=current_user)
                
            #     myposts =allPosts.paginate(page=page, per_page=rows_per_page )
            #     if not search_query:
            #         flash("No recent posts", category="error")
            #     else:
            #         return render_template('search.html', user=current_user, allSchPostsquery=allPosts, allSchPosts=myposts, search_query=search_query, userSearch=userSearch,  search_dict= search_dict)

            #     return render_template('search.html', user=current_user,allSchPostsquery=allPosts,allSchPosts=myposts,search_query=search_query, userSearch=userSearch, search_dict= search_dict)
            # return render_template('search.html', user=current_user)
        else:

            rows_per_page = 5
            page = request.args.get('page', 1, type=int)
            getPosts = getPOsts.paginate(page=page, per_page=rows_per_page )

            return render_template('search.html', user=current_user, allSchPosts= getPosts)
    return render_template('search.html', user=current_user)





<script>
  userSearch = document.getElementById("search_ii").value;
  let searchText = {
    textvalue: userSearch,
  };

  fetch("/ssearch_result", {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(searchText),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
    }),
  })
    //   .then((_res) => {
    //     window.location.href = "/search_result";
    // });
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Print the greeting as text

      console.log(data);
      //     // section = document.getElementsByClassName('_section')
      //     // for (i=0;i<section.length;i++){
      //     //   section[i].innerHTML = data
      //     // }
    })
    .catch((error) => {
      console.log(error);
    });
  console.log(searchText);
</script>
<!-- <script>
  fetch("/ssearch")
    .then(function (response) {
      // resp = JSON.stringify(response);
      // // res = JSON.parse(res);
      // console.log(Object.entries(resp));
      // return resp;
      return response.json();
    })
    .then(function (data) {
      // Print the greeting as text
      console.log(data);
    })
    .catch((error) => {
      console.log(error);
    });
  // .then(function (response) {
  //   resp = JSON.stringify(response);
  //   // res = JSON.parse(res);
  //   console.log(Object.entries(resp));
  //   return resp;
  // })
  // .then(function (data) {
  //   // Print the greeting as text
  //   console.log(Object.entries(data));
  // });
</script> -->