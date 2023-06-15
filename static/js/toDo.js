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

        const validate = await ajax(molde,'/ajax/create');
        console.log(validate);

        Read(molde);

        textField.value = '';
    }
}

function Read(DICT){
    const item = document.createElement('div')
    item.className = 'mini-card'
    item.id = '36'

    item.innerHTML = `
        <input type="text" value="${DICT.word}">
        <div>
            <button onclick="Update(1)">U</button>
            <button onclick="Delete(1)">D</button>
        </div>
    `
    document.getElementById('group').appendChild(item)
}

function Delete(id){
    ajax({'id': 36}, '/ajax/delete')
    const element = document.getElementById(``);
    
    element.remove();
}

function Update(id){
    const validate = ajax({'id': 36}, '/ajax/delete')
    const card = document.getElementById(``);
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