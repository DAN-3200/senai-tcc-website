//Note
const create = document.getElementById('create-note')
create.addEventListener("click", function() {
  Create();
});

async function Create() {
    const title = document.getElementById('title').value
    const content = document.getElementById('content').value

    if(title.length <= 0){
        alert('Não tem nada')
        return;
    }else{
        const molde = {
            'title' : title,
            'content' : content,
        }

        const validate = await ajax(molde,'/notes/create');
        console.log(validate);
        Read(validate);

    }
}

function Read(DICT){
    const item = document.createElement('div')
    item.className = 'saved-card'
    item.id = `#${DICT.id}`

    item.innerHTML = `
        <a class="sav-card-show" href="/home/update/${DICT.id}"><span>${DICT.title}</span></a>
        <a class="excluir" style="font-size: 14px " type="button" href="/home/delete/${DICT.id}"><i class="fa-solid fa-trash-can"></i></a>
    `
    document.getElementById('group-card').appendChild(item)
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

