
let scholarshipDIVHTML = "";

let schDIVData =Object.entries(snapshot.val());
console.log(schDIVData);

let list_element = document.getElementById('tutorials');
list_element.classList.add('testimonials');
let createContent = document.createElement('div');
createContent.classList.add('content');
let currentPage = 1; 
let rows = 6;

function displaylist(items, wrapper, rowsPerPage, page) {
    //wrapper.innerHTML = "";
    page--;

    let start = rowsPerPage * page; 
    let end =  start + rowsPerPage;
    let paginatedItem =items.slice(start, end);
    console.log(paginatedItem);
    
    for (let i = 0; i < paginatedItem.length; i++) {
        //  const element = listitemssss[i];
        console.log(schDIVData[i]);
        let itemschDIVData = schDIVData[i];
             let createBox = document.createElement('div');
             createBox.classList.add('box');
             let createImgBox = document.createElement('div');
             createImgBox.classList.add('imgBx');
             let createText = document.createElement('div');
             createText.classList.add('text');
             let scholarshipHTML = "";

            
             scholarshipHTML += "<img src=" + itemschDIVData[1].imageUrl + ">";
             scholarshipHTML += "<div class='text'>";
             scholarshipHTML += "<h3><span class=view-btn >" + itemschDIVData[1].department + "</span>" + "<br>" +
              itemschDIVData[1].details + "<br>" + "Date: " + itemschDIVData[1].date +
               "<a href=# class=viewDept-btn id=" + itemschDIVData[1].id + "> View details </a></h3> </div> </div> </div>";                      
            createImgBox.innerHTML = scholarshipHTML;
             createImgBox.appendChild(createText);
             createBox.appendChild(createImgBox);
             createContent.appendChild(createBox);
             wrapper.appendChild(createContent);


         }   // E N D S     for loop
}
displaylist(schDIVData, list_element, rows, currentPage);