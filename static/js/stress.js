var btnAntiStress = document.getElementById("btnAntiStress");
var modal = document.getElementById("modal");
var closeBtn = document.getElementsByClassName("close")[0];

// Variáveis para armazenar a posição inicial do botão
var initialX;
var initialY;
var isDragging = false;
var isClick = false;


// Função para iniciar o arrastamento do botão
function iniciarArrastamento(event) {
  var isClickInsideButton = event.target === btnAntiStress;

  if (isClickInsideButton) {
    initialX = event.clientX - btnAntiStress.offsetLeft;
    initialY = event.clientY - btnAntiStress.offsetTop;
    isDragging = true;
  } else {
    isClick = true;
  }

  document.addEventListener("mousemove", moverBotao);
  document.addEventListener("mouseup", pararArrastamento);
}

// Função para mover o botão enquanto arrasta
function moverBotao(event) {
  if (isDragging) {
    event.preventDefault();

    var newX = event.clientX - initialX;
    var newY = event.clientY - initialY;

    btnAntiStress.style.left = newX + "px";
    btnAntiStress.style.top = newY + "px";
  }
}

// Função para parar o arrastamento do botão
function pararArrastamento() {
  if (isDragging) {
    isDragging = false;
    document.removeEventListener("mousemove", moverBotao);
    document.removeEventListener("mouseup", pararArrastamento);
  } else {
    isClick = false;
  }
}

// Adiciona o evento de iniciar arrastamento ao clicar no botão
btnAntiStress.addEventListener("mousedown", iniciarArrastamento);



  function playMusic(videoId) {
            var iframe = document.createElement('iframe');
            iframe.src = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1';
            iframe.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
            iframe.allowfullscreen = true;

            var modalBody = document.querySelector('.modal-body');
            modalBody.innerHTML = '';
            modalBody.appendChild(iframe);

            var closeBtn = document.createElement('span');
            closeBtn.innerHTML = '&times;';
            closeBtn.className = 'close-video';
            closeBtn.addEventListener('click', function() {
                modalBody.innerHTML = '';
                showOptions();
            });

            modalBody.appendChild(closeBtn);
        }

        // Função para reproduzir a lista de reprodução do YouTube
        function playPlaylist(playlistId) {
            var iframe = document.createElement('iframe');
            iframe.src = 'https://www.youtube.com/embed/videoseries?list=' + playlistId + '&autoplay=1';
            iframe.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
            iframe.allowfullscreen = true;

            var modalBody = document.querySelector('.modal-body');
            modalBody.innerHTML = '';
            modalBody.appendChild(iframe);

            var closeBtn = document.createElement('span');
            closeBtn.innerHTML = '&times;';
            closeBtn.className = 'close-video';
            closeBtn.addEventListener('click', function() {
                modalBody.innerHTML = '';
                showOptions();
            });

            modalBody.appendChild(closeBtn);
        }

        // Função para exibir a modal
        function showModal() {
            var modal = document.getElementById('optionsModal');
            modal.style.display = 'block';
        }

        // Função para ocultar a modal
        function hideModal() {
            var modal = document.getElementById('optionsModal');
            modal.style.display = 'none';
            showOptions();
        }

        // Função para exibir as opções novamente
        function showOptions() {
            var modalBody = document.querySelector('.modal-body');
            modalBody.innerHTML = '<ul><li class="modal-list" onclick="playMusic(\'jfKfPfyJRdk\')">Música</li><li class="modal-list" onclick="playPlaylist(\'PL39t2B92wpzmEd3lfJ8_j9Y_YvwYJjliw\')">Alongamentos</li><li class="modal-list" onclick="playPlaylist(\'PL39t2B92wpzmdEq5cnWzKZajo_dCxSY5D\')">Respiração</li></ul>';
        }