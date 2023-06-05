function obterMensagem() {
    fetch('/api/mensagem')
        .then(response => response.json())
        .then(mensagem => {
            const mensagemDiv = document.getElementById('mensagem');
            mensagemDiv.innerHTML = '';

            if (mensagem.tópico) {
                const mensagemElement = document.createElement('div');
                mensagemElement.classList.add('mensagem');
                mensagemElement.innerHTML = `
                    <p><strong>Tópico:</strong> ${mensagem.tópico}</p>
                    <p><strong>Partição:</strong> ${mensagem.partição}</p>
                    <p><strong>Offset:</strong> ${mensagem.offset}</p>
                    <p><strong>Valor:</strong> ${mensagem.valor}</p>
                `;

                mensagemDiv.appendChild(mensagemElement);
            } else {
                mensagemDiv.textContent = 'Nenhuma mensagem disponível';
            }
        });
}

// Obter e remover uma mensagem a cada 500 milissegundos
setInterval(obterMensagem, 500);
