const delete_confirmation_section=document.getElementById('delete_confirmation_section')
const delete_expense_create_button=document.getElementById('delete_expense_create_button')
const main_section=document.getElementById('main_section')
const cancel_expense_delete_button=document.getElementById('cancel_expense_delete_button')

delete_expense_create_button.addEventListener('click',()=>{
    main_section.classList.add('hide')
    delete_confirmation_section.classList.remove('hide')
})

cancel_expense_delete_button.addEventListener('click',()=>{
    main_section.classList.remove('hide')
    delete_confirmation_section.classList.add('hide')

})
