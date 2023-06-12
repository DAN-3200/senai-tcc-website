// test de AJAX
let box;

function Env(){
    // pega os campos
    let title = document.getElementById('title');
    let content = document.getElementById('content');

    // Moldar a informação em array
    let molde = {
        Titulo: title.value,
        Conteudo: content.value
    };

    // console.log(molde);


    // "AJAX" --> fetch('url',{...}).then(function(response){});
    fetch('/ajax', {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(molde),
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
            console.log(newData);
            alert(newData['Email']);
            box = newData;
        })
    });
};


