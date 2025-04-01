fetch('http://localhost:8000/')
.then(response => response.json())
.then(data => {
  document.getElementById('dados').innerText = JSON.stringify(data);
})
.catch(error => console.error('Erro ao buscar dados:', error));
