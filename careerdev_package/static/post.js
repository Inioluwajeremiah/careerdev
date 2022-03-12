let titleinput = document.getElementById('title')
let subtitleinput = document.getElementById('subtitle')
let institutioninput = document.getElementById('institution')
let facultyinput = document.getElementById('faculty')
let departmentinput = document.getElementById('department')
let courseinput = document.getElementById('course')
let levelinput = document.getElementById('level')
let descrinput = document.getElementById('descr')
let durationinput = document.getElementById('duration')
let appfeeinput = document.getElementById('appfee')
let urlinput = document.getElementById('url')
let countryinput = document.getElementById('country')
let fundinginst = document.getElementById('fund-inst')

function clearPostField(){
    titleinput.value = ''
    subtitleinput.value = ''
    countryinput.value = ''
    institutioninput.value = ''
    facultyinput.value = ''
    departmentinput.value = ''
    courseinput.value = ''
    levelinput.value = ''
    descrinput.value = ''
    durationinput.value = ''
    appfeeinput.value = ''
    urlinput.value = ''
    tokeninput.value = ''
    fundinginst.value=''
}
function country() {
    countryinput.value = ''
}
function posttitle() {
    titleinput.value = ''
}
function subtitle() {
    subtitleinput.value = ''
}

function institution() {
    institutioninput.value = ''
}

function faculty() {
    facultyinput.value = ''
}

function department() {
    departmentinput.value = ''
}

function course() {
    courseinput.value = ''
}

function level() {
    levelinput.value = ''
}

function descr() {
    descrinput.value = ''
}

function duration() {
    durationinput.value = ''
}

function appfee() {
    appfeeinput.value = ''
}

function url() {
    urlinput.value = ''
}

function token() {
    tokeninput.value = ''
}
function fundInst(params) {
    fundInst.value = ''
}

// function loadSavedInput() {
//     localStorage.setItem('titleinput', titleinput.value)
//     localStorage.setItem('subtitleinput', subtitleinput.value)
//     localStorage.setItem('institutioninput', institutioninput.value)
//     localStorage.setItem('facultyinput', facultyinput.value)
//     localStorage.setItem('departmentinput', departmentinput.value)
//     localStorage.setItem('courseinput', courseinput.value)
//     localStorage.setItem('levelinput', levelinput.value)
//     localStorage.setItem('descrinput', descrinput.value)
//     localStorage.setItem('durationinput', durationinput.value)
//     localStorage.setItem('appfeeinput', appfeeinput.value)
//     localStorage.setItem('urlinput', urlinput.value)
//     localStorage.setItem('tokeninput', tokeninput.value)

//     titleinput.value = localStorage.getItem('titleinput')
//     subtitleinput.value = localStorage.getItem('subtitleinput')
//     institutioninput.value = localStorage.getItem('institutioninput')
//     facultyinput.value = localStorage.getItem('facultyinput')
//     departmentinput.value = localStorage.getItem('departmentinput')
//     courseinput.value = localStorage.getItem('courseinput')
//     levelinput.value = localStorage.getItem('levelinput')
//     descrinput.value = localStorage.getItem('descrinput')
//     durationinput.value = localStorage.getItem('durationinput')
//     appfeeinput.value = localStorage.getItem('appfeeinput')
//     urlinput.value = localStorage.getItem('urlinput')
//     tokeninput.value = localStorage.getItem('tokeninput') 
// }