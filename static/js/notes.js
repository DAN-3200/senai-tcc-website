// Fetch == AJAX
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

// Meta: CRUD de Notas

// --- Captura
document.getElementById('create-note').addEventListener("click", function() {
    Create();
});

document.getElementById('title').addEventListener("input", function() {
    updateNote();
});

document.getElementById('content').addEventListener('input', function(){
    updateNote();
});

// --- Funções

let id_card, close;

function hidden_card(){
    const element = document.getElementById('card');
    element.classList.toggle('hidden-card');
}

async function getData(id){
    const validate = await ajax({'id': id},'/notes/getData');
    console.log(validate.id);

    if(close != true){
        close = true
        hidden_card()
    }

    id_card = validate.id
    document.getElementById('title').value = validate.title;
    document.getElementById('content').value = validate.content;
    document.getElementById('date-card').textContent = validate.date;

}

async function Create() {
    const validate = await ajax({},'/notes/create');
    //console.log(validate);
    createNote(validate);
    if(id_card == null){
        getData(validate.id)
    }
}

function createNote(DICT){
    const item = document.createElement('div')
    item.className = 'saved-card'
    item.id = `#S${DICT.id}`

    item.innerHTML = `
        <button class="sav-card-show" onclick="getData(${DICT.id})"><span>Sem título...</span></button>
        <button class="excluir" style="font-size: 14px" type="button" onclick="deleteNote(${DICT.id})"><i class="fa-solid fa-trash-can"></i></button>
    `
    document.getElementById('group-card').appendChild(item)
}

function updateNote(){
    const title = document.getElementById('title');
    const content = document.getElementById('content');
    const id = id_card
    //console.log(id)

    const molde = {
        'id': id,
        'title' : title.value,
        'content' : content.value,
    };

    ajax(molde, '/notes/update');

    const newTitle = document.getElementById(`#S${id}`).querySelector('span')
    newTitle.textContent = title.value
}

function deleteNote(id){
    ajax({'id': id}, '/notes/delete')
    const element = document.getElementById(`#S${id}`);
    if(id == id_card){
        id_card = null;
        close = null;
        hidden_card();
    }
    element.remove();
}







