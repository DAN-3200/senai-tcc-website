// tá funcionando

function Env(){
    let title = document.getElementById('title');
    let content = document.getElementById('content');

    let molde = {
        Titulo: title.value,
        Conteudo: content.value
    };

    fetch('http://127.0.0.1:5000/ajax', {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(molde),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });

}



