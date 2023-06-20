const button = document.getElementById('start')
const element = document.getElementById('box')


let debounce = false;
button.addEventListener('click', function(){
    if(debounce != true){
        element.classList = 'box-end'
        debounce = true
    } else {
        element.classList = 'box-start'
        debounce = false
    }
})

const box = document.getElementById('box')

box.addEventListener('transitionend', function(event){
    if(event.elapsedTime = 3){
        element.classList = 'box-start'
    }
})