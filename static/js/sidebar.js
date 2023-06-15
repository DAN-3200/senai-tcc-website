const body = document.querySelector('body')
const nav = body.querySelector('nav')

const hidden = document.getElementById('hidden')

hidden.addEventListener('click', () =>{
    nav.classList.toggle('close')
})