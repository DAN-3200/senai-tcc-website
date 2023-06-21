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

// Pomodoro
window.onload = function() {
  var divCronometro = document.getElementById("cronometro");
  var btnIniciar = document.getElementById("iniciar");
  var btnParar = document.getElementById("parar");
  var btnZerar = document.getElementById("zerar");
  var intervaloSegundos = document.getElementById("intervaloAlarme");
  new Cronometro(divCronometro, btnIniciar, btnParar, btnZerar);
}

let debounce;
const title = document.getElementById('time-title').textContent
var Cronometro = function(div, btnIniciar, btnParar, btnZerar) {
  var este = this;
  this.estado = null;
  this.hora = 0;
  this.minuto = 29;
  this.segundo = 59;
  this.intervaloAlarmeMinutos = 0;
  this.intervaloAlarmeSegundos = 0;
  this.start = false;

  // criando elemento html5 audio
  this.audio = document.createElement('audio');
  this.sourceAudio = document.createElement('source');
  this.sourceAudio.setAttribute('src', 'http://www.online-clockalarm.com/sounds/sound3.mp3');
  this.sourceAudio.setAttribute('type', 'audio/mp3');
  this.audio.appendChild(this.sourceAudio);

  this.atualizar = function() {
    var str =
      (este.minuto < 10 ? "0" + este.minuto : este.minuto) + " : " +
      (este.segundo < 10 ? "0" + este.segundo : este.segundo);
    div.innerHTML = str;
    document.getElementById('time-title').textContent = str;
  }
  this.iniciar = function() {
    if (!este.start) {
      este.estado = setInterval(function() {
        if(este.segundo == 0){
          este.segundo = 60;
        }
        este.segundo -= 1;
        if (este.segundo % 60 == 0) {
          este.segundo = 0;
          este.minuto -= 1;
        }
        if (este.minuto % 60 == 0 && este.minuto > 0) {
          este.minuto = 0;

        }
        este.atualizar();
        este.verificaAlarme();
      }, 1000);
      este.start = true;
    }
  }
  this.parar = function() {
    clearInterval(este.estado);
    este.start = false;
  }
  this.zerar = function() {
    este.minuto = 29;
    este.segundo = 00;
    este.atualizar();
  }
  this.setIntervaloAlarmeMinutos = function(minutos) {
    este.intervaloAlarmeMinutos = minutos;
  }
  this.setIntervaloAlarmeSegundos = function(segundos) {
    este.intervaloAlarmeSegundos = segundos;
  }
  this.verificaAlarme = function() {
    if (este.intervaloAlarmeMinutos != 0 || este.intervaloAlarmeSegundos != 0) {
      var segundosTotais = este.hora * 3600 + este.minuto * 60 + este.segundo;
      var intervaloAlarmeSegundosTotais = parseInt(este.intervaloAlarmeMinutos * 60) + parseInt(este.intervaloAlarmeSegundos);
      if (segundosTotais % intervaloAlarmeSegundosTotais == 0) {
        este.audio.play();
        este.parar();
        window.alert("Acabou! Descanse um pouco");
      };
    }
  }

  // Adicionando listeners
  if (document.addEventListener) {
    btnIniciar.addEventListener("click", function() {
        if(debounce != true){
            este.iniciar();
            debounce = true;
            btnIniciar.innerHTML = '<i class="fa-solid fa-pause"></i>'
        }else{
             este.parar();
             debounce = null;
             btnIniciar.innerHTML = '<i class="fa-solid fa-play"></i>'
             document.getElementById('time-title').textContent = title
        }
    });

    btnZerar.addEventListener("click", function() {
      este.zerar();
    });

  } else {
    btnIniciar.addAttachEvent("onClick", function() {
      este.iniciar();
    });
    btnParar.addAttachEvent("onClick", function() {
      c.parar();
    });
    btnZerar.addAttachEvent("onClick", function() {
      c.zerar();
    });
  }
};

const tab = document.getElementsByClassName('button-tab');
let current_tab;

console.log(tab);
for(let i = 0; i < tab.length; i++){
  tab[i].addEventListener('click', function(){
      tab[i].classList.add('target-button');

      if(current_tab){
        current_tab.classList.remove('target-button');
      }

      current_tab = tab[i];
  })
}
