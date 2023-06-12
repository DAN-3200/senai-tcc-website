// Fazer um CRUD de Item

function Create() {
    const textField = document.getElementById('field')

    if(textField.value.length <= 0){
        alert('Não tem nada')
        return;
    }else{
        let molde = {
            'word' : textField.value
        };

        const back = ajax(molde,'/ajax/create');
        console.log(back);
        Read(molde);

        textField.value = '';
    }
}

function Read(DICT){
    const item = document.createElement('div')
    item.className = 'mini-card'
    item.id = '1'

    item.innerHTML = `
        <input type="text" value="${DICT.result}">
        <div>
            <button onclick="Update(1)">U</button>
            <button onclick="Delete(1)">D</button>
        </div>
    `
    document.getElementById('group').appendChild(item)
}

function Delete(i){
    delete BOX[i];
    const element = document.getElementById(`#${i}`);
    
    element.remove();
    console.log(BOX);
}

function Update(i){
    const card = document.getElementById(`#${i}`);

    BOX[i] = card.querySelector('input').value;
    console.log(BOX)
}

function ajax(dict, url){
    // "AJAX" --> fetch('url',{...}).then(function(response){});
    fetch( url, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(dict),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function(response) {
        if (response.status != 200){
            console.log('unstable status!');
            return;
        }
        response.json().then(function(newData){
            // pega informação
            console.log(newData)
            return newData
        })
    });

};