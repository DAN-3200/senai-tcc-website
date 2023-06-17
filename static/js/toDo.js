// Fazer um CRUD de Item

async function Create() {
    const text = document.getElementById('field')

    if(text.length <= 0){
        alert('Não tem nada')
        return;
    }else{
         const molde = {
            'content' : text.value,
        }
        const validate = await ajax(molde,'/ajax/create');
        console.log(validate);

        Read(validate);
        text.value = '';
    }
}

function Read(DICT){
    const item = document.createElement('div')
    item.className = 'mini-card'
    item.id = `#${DICT.id}`

    item.innerHTML = `
        <input name="check" type="checkbox">
        <input class="texto" type="text" value="${DICT.content}">
        <div>
            <button onclick="Update(${DICT.id})">U</button>
            <button onclick="Delete(${DICT.id})">D</button>
        </div>
    `
    document.getElementById('group').appendChild(item)
}

function Delete(id){
    ajax({'id': id}, '/ajax/delete')
    const element = document.getElementById(`#${id}`);
    
    element.remove();
}

function Update(id){
    const ent = document.getElementById(`#${id}`).childNodes
    //console.log(ent[3])
    ajax({'id': id , 'content': ent[3].value }, '/ajax/update')
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
