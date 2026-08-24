function theme_checker() {
    let page_theme=localStorage.getItem('theme')
    if (page_theme!=null) {
        if (page_theme=='light') {
            document.getElementById('toggle_to').innerText='Dark';
        }
        else{
            document.getElementById('toggle_to').innerText='Light';
        }
        return page_theme
    }
    else{
        document.getElementById('toggle_to').innerText='Light';
        return null
    }
}

function theme_applicator() {
    const theme_preference=theme_checker()
    if (theme_preference===null) {
        document.documentElement.setAttribute('theme-preference','light')   
    }
    else{
        document.documentElement.setAttribute('theme-preference',theme_preference)
    }
}

function toggle_theme() {
    let toggle_to=document.getElementById('toggle_to')
    if (toggle_to.innerText=='Light'){
        toggle_to.innerText='Dark';
        localStorage.setItem('theme','light')
    }
    else{
        toggle_to.innerText='Light';
        localStorage.setItem('theme','dark')
    }
    theme_applicator()
}

let theme_toggler_button=document.getElementById('theme_toggler_button')
theme_toggler_button.addEventListener('click',()=>{
    toggle_theme()
})

theme_applicator()