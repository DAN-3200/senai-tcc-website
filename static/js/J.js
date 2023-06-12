// Fazer um CRUD de Item

async function Create() {
    const textField = document.getElementById('field')

    if(textField.value.length <= 0){
        alert('Não tem nada')
        return;
    }else{
        let molde = {
            'word' : textField.value
        };

        const back = await ajax(molde,'/ajax/create');
        console.log(back.status);

        Read(molde);

        textField.value = '';
    }
}

function Read(DICT){
    const item = document.createElement('div')
    item.className = 'mini-card'
    item.id = '1'

    item.innerHTML = `
        <input type="text" value="${DICT.word}">
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
    return new Promise((resolve, reject) =>
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
            return response.json();
        }).then(function(newData) {
            // Manipula os dados recebidos
            resolve(newData);
        })
        .catch(function(error) {
            // Lida com erros da requisição
            reject(error);
        })
    )

}