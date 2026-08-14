
// CREATE EXPENSE FORM
const create_expense_form_div=document.getElementById('create_expense_form_div')
const show_create_expense_form_button=document.getElementById('show_create_expense_form_button')
const create_expense_form_cancel_button=document.getElementById('create_expense_form_cancel_button')

show_create_expense_form_button.addEventListener('click',()=>{
    create_expense_form_div.classList.remove('hide')
    show_create_expense_form_button.classList.add('hide')
})

create_expense_form_cancel_button.addEventListener('click',()=>{
    create_expense_form_div.classList.add('hide')
    show_create_expense_form_button.classList.remove('hide')
})


// CREATE CALENDAR 
const calendar_div=document.getElementById('calendar_div')
const show_calendar_button=document.getElementById('show_calendar_button')
const calendar_cancel_button=document.getElementById('calendar_cancel_button')

show_calendar_button.addEventListener('click',()=>{
    calendar_div.classList.remove('hide')
    show_calendar_button.classList.add('hide')
})

calendar_cancel_button.addEventListener('click',()=>{
    calendar_div.classList.add('hide')
    show_calendar_button.classList.remove('hide')
})


// FIND BY DATE FORM
const find_by_date_form_div=document.getElementById('find_by_date_form_div')
const show_find_by_date_form_button=document.getElementById('show_find_by_date_form_button')
const find_by_date_form_cancel_button=document.getElementById('find_by_date_form_cancel_button')

show_find_by_date_form_button.addEventListener('click',()=>{
    find_by_date_form_div.classList.remove('hide')
    show_find_by_date_form_button.classList.add('hide')
})

find_by_date_form_cancel_button.addEventListener('click',()=>{
    find_by_date_form_div.classList.add('hide')
    show_find_by_date_form_button.classList.remove('hide')
})

// FIND BY DATE FORM
const find_by_month_form_div=document.getElementById('find_by_month_form_div')
const show_find_by_month_form_button=document.getElementById('show_find_by_month_form_button')
const find_by_month_form_cancel_button=document.getElementById('find_by_month_form_cancel_button')

show_find_by_month_form_button.addEventListener('click',()=>{
    find_by_month_form_div.classList.remove('hide')
    show_find_by_month_form_button.classList.add('hide')
})

find_by_month_form_cancel_button.addEventListener('click',()=>{
    find_by_month_form_div.classList.add('hide')
    show_find_by_month_form_button.classList.remove('hide')
})


