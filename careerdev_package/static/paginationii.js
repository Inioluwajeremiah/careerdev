var state = {
    'queryset': schDIVData,
    'page': 1,
    'rows': 8,
    'window': 5,
    }
    let currentPage = 1; 
    let rows = 6;

    function adminpagination(queryset, page, rows){
    let trimstart = (page -1) * rows;
    let trimend = (trimstart + rows);
    let trimData = queryset.slice(trimstart, trimend);

    let pages = Math.ceil(queryset.length/rows);

    return{
        'queryset': trimData,
        'pages':pages,
    }

    }  // ends adminpagination

    let paginationWrapper = document.getElementById('scholarship-pagination');
    function paginatedButtons(pages){
    paginationWrapper.innerHTML = "";

    let maxLeft = (state.page - Math.floor(state.window / 2));
    let maxRight = (state.page + Math.floor(state.window / 2));

    if(maxLeft < 1){
        maxLeft = 1
        maxRight = state.window
    }
    if(maxRight > pages){
        maxLeft = pages - (state.window - 1);
        maxRight = pages;

        if(maxLeft < 1) {
        maxLeft = 1;
        }
    }


    for(let page = maxLeft; page <= maxRight; page++) {
        paginationWrapper.innerHTML += `<button value=${page} class="pagination-buttons">${page} </button>`;
    }

    if(state.page != 1) {
        paginationWrapper.innerHTML = `<button value=${1} class="pagination-buttons">&#171 First </button>`+ paginationWrapper.innerHTML;
    }

    if(state.page != pages) {
        paginationWrapper.innerHTML += `<button value=${pages} class="pagination-buttons">Last &#187</button>`;
    }

    $('.pagination-buttons').on('click', function(){
        $('.content').empty();
        state.page = Number($(this).val());
        buildDIV();
    }); // end spagination .onclick function

    }   // ends  paginatedButtons

    buildDIV();
    function buildDIV() {
        let deptSection = document.getElementById('department-section');
        deptSection.classList.add('courses');
        let createContent = document.createElement('div');
        createContent.classList.add('content');
        
       var adminpaginatedData =  adminpagination(state.queryset, state.page, state.rows);
       console.log('admin paginated: ' , adminpaginatedData);
       
       let  mylist = adminpaginatedData.queryset;
       console.log('mylist:', mylist);
    

        for(var i = 0; i<mylist.length; i++){
        let itemschDIVData = schDIVData[i];
        let createBox = document.createElement('div');
        createBox.classList.add('box');
        let createImgBox = document.createElement('div');
        createImgBox.classList.add('imgBx');
        let createText = document.createElement('div');
        createText.classList.add('text');
       //  let createH3= document.createElement('h3');
       //  let createSpan = document.createElement('span');
       //  createText.classList.add('view-btn');
        let scholarshipHTML = "";

        scholarshipHTML += "<img src=" + itemschDIVData[1].imageUrl + ">";
        scholarshipHTML += "<div class='text'>";
        scholarshipHTML += "<h3><span class=btn >" + itemschDIVData[1].department + "</span>" + "<br>" +
        itemschDIVData[1].details + "<br>" + "Date: " + itemschDIVData[1].date + "<a href=# class=view-btn id=" + itemschDIVData[1].id + "> View details </a></h3> </div> </div> </div>";                      
           
       //  createText.innerHTML = scholarshipHTML;
       createImgBox.innerHTML = scholarshipHTML;
        createImgBox.appendChild(createText);
        createBox.appendChild(createImgBox);
        createContent.appendChild(createBox);
        //list_element.appendChild(createContent);
        deptSection.appendChild(createContent);


    }   // E N D S     for loop

    paginatedButtons(adminpaginatedData.pages);

}  // ends buildTable
