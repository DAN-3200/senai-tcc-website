//Note
const create = document.getElementById('create-note')
create.addEventListener("click", function() {
  Create();
});

// CRUD de Notas
async function Create() {
    const validate = await ajax({},'/notes/create');
    console.log(validate);
    createCard(validate);
}

// getData
async function getData(id){
    const validate = await ajax({'id': id},'/notes/create');
    console.log(validate);
}

function update(){
    const title = document.getElementById('title').value
    const content = document.getElementById('content').value

    const molde = {
        'title' : title,
        'content' : content,
    }
}

function createCard(DICT){
    const item = document.createElement('div')
    item.className = 'saved-card'
    item.id = `#${DICT.id}`

    item.innerHTML = `
        <button class="sav-card-show" onclick=""><span>Sem título...</span></button>
        <button class="excluir" style="font-size: 14px " type="button" onclick=""><i class="fa-solid fa-trash-can"></i></button>
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

