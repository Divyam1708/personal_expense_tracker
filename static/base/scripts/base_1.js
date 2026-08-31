const toggle_to=document.getElementById('toggle_to');
const theme_toggle_image=document.getElementById('theme_toggle_image');
const theme_toggler_button=document.getElementById('theme_toggler_button');

function theme_image_setter_light_preference() {
    toggle_to.innerText='Dark';
    theme_toggler_button.style.backgroundImage="url('/static/base/images/moon.png')";
}

function theme_image_setter_dark_preference() {
    toggle_to.innerText='Light';
    theme_toggler_button.style.backgroundImage="url('/static/base/images/sun.png')";
}


function theme_checker() {
    let page_theme=localStorage.getItem('theme')
    if (page_theme!=null) {
        if (page_theme=='light') {
            theme_image_setter_light_preference();
        }
        else{
            theme_image_setter_dark_preference();
        }
        return page_theme
    }
    else{
        theme_image_setter_light_preference()
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
    if (toggle_to.innerText=='Light'){
        theme_image_setter_light_preference()
        localStorage.setItem('theme','light')
    }
    else{
        theme_image_setter_dark_preference()
        localStorage.setItem('theme','dark')
    }
    theme_applicator()
}

theme_toggler_button.addEventListener('click',()=>{
    toggle_theme()
})

theme_applicator()