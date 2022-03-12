/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className == "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

  window.addEventListener('scroll', function(){
    const header = document.querySelector('header');
    header.classList.toggle("sticky", window.scrollY > 0);
});

function closeAlert() {
   let close_icon = document.getElementById('close-alert')
   let alertDiv = document.getElementById('alert-div')
   alertDiv.style.display = 'none';
   
}

function delRow(id) {
  fetch("/delrow", {
      method: 'POST',
      body: JSON.stringify({row_id: id}),
  
  }).then((_res) => {
      window.location.href = "/";
  }); 
}

function searchPaginate() {
  userSearch = document.getElementById('user-search').value
  if(userSearch != ''){

    let searchText = {
      textvalue: userSearch
    } 

    fetch('/ssearch_result', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(searchText),
      cache: "no-cache",
      headers: new Headers ({
        "content-type": "application/json"
      })
    })
  //   .then((_res) => {
  //     window.location.href = "/search_result";
  // }); 
    .then(function (response) {
      
       return response.json()
    })
    .then(function (data) {
      // Print the greeting as text     
      parsed_data = JSON.parse(data)
      console.log(parsed_data);
      schDIVData = Object.entries(parsed_data)
      console.log("array of parsed data", schDIVData);
     
      console.log(schDIVData);
      section = document.getElementsByClassName('_section')

      var state = {
        'queryset': schDIVData,
        'page': 1,
        'rows': 10,
        'window': 3,
        }
 
        function adminpagination(queryset, page, rows){
          let trimstart = (page - 1) * rows;
          let trimend = (trimstart + rows);
          let trimData = queryset.slice(trimstart, trimend);
      
          let pages = Math.ceil(queryset.length/rows);
      
          return{
              'queryset': trimData,
              'pages':pages,
          }
    
        }  // ends adminpagination
            
        function paginatedButtons(pages){
          let paginationWrapper = document.getElementById('scholarship-pagination');
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
            let deptSection = document.getElementById('search-section');
            deptSection.classList.add('_section');
            let createContent = document.createElement('div');
            createContent.classList.add('content');
            
           var adminpaginatedData =  adminpagination(state.queryset, state.page, state.rows);
           console.log('admin paginated: ' , adminpaginatedData);
           
           let  mylist = adminpaginatedData.queryset;
           console.log('mylist:', mylist);
        
    
            for(var i = 0; i<schDIVData[0].length; i++){
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
    
            // scholarshipHTML += "<img src=" + schDIVData[13][1][i] + ">";
            scholarshipHTML += "<div class='text'>";
            scholarshipHTML += "<h3><span class=btn >" + schDIVData[1][1][i] + "</span>" + "<br>" +
            schDIVData[2][1][i] + "<br>" + "Date: " + schDIVData[10][1][i] + "<br>" +
             "<a href=/details/"+ schDIVData[0][1][i] + " class=view-btn id=" + schDIVData[0][1][i] + "> View details </a></h3> </div> </div> </div>";                      
                           
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
    
      
    })
    .catch(error =>{
    console.log(error);
  })
  console.log(searchText);

  } else {
    alert('enter a serch value')
  }


 
//   fetch('/search')
// .then(data => {
// return data.json();
// })
// .then(post => {
// console.log(post);
// });
// let resp;

// fetch('/search')
//   .then(response => {
//     return JSON.stringify(response) })
//     .then(data => console.log(JSON.parse(data)))
   
// let resp = JSON.stringify(response);
// res = JSON.parse(resp);
  // resp = JSON.stringify(response);
      // // res = JSON.parse(res);
      // console.log(Object.entries(resp));
      // return resp;

// fetch('/search')
//     .then(function (response) {
//         return response.json();
//     }).then(function (data) {
//         console.log('GET response text:');
//         console.log(data); // Print the greeting as text
//     });
}

filterDiv = document.getElementById('filter-div')
function toggleSearch(){
  if(filterDiv.style.display != 'block'){
    filterDiv.style.display = 'block'
  }
  else{
    filterDiv.style.display = 'none'
  }
  
}
// 07038107221
// eldferlycare and orphanage home
// raphael and sons

const srTop = ScrollReveal({
  origin: 'top',
  distance: '30px',
  duration: 1500,
  reset: true
});

srTop.reveal(`.imgBx, .post-details`,  {
  interval: 200

})

const srBottom = ScrollReveal({
  origin: 'left',
  distance: '30px',
  duration: 1500,
  reset: true
});

srBottom.reveal(`.sub-header, .related-post`,  {
  interval: 1500

})