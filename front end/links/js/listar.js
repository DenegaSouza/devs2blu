function carregaDados(){
    return JSON.parse(localStorage.getItem('Funcionarios'))
};

function carregarEditar(event, id){
    console.log('Evento de click', event);
    event.preventdefault();
    carregarEditar(id)

};

function carregar(){
    console.log('Carregando janela');
    var tbody = document.querySelector('tbody');
    tbody.innerHTML = ''

    var funcionarios = localStorage.getItem('Funcionarios');

    funcionarios = JSON.parse(funcionarios);
    
    funcionarios.forEach((e) =>{
    var tr = `<tr>
                    <td>${e['id']}</td>
                    <td>${e['nome']}</td>
                    <td>${e['cpf']}</td>
                    <td>${e['cargo']}</td>
                    <td>R$ ${e['salario']}</td>
                    <td>
                    <button class="bt-editar" href="editar.html?id=${e['id']}">Editar</a>
                    <button class="bt-deletar" href="" onclick="deletar(${e['id']})">Deletar</button>
                    </td>
                </tr>`

        tbody.innerHTML += tr
    });
}
function deletar(id){
    var lista = carregaDados();
    var novalista = [];
    lista.forEach(e => {
        if(e['id'] != id){
            novalista.push(e)
        }
    });
    localStorage.setItem('Funcionarios', JSON.stringify(novalista));
    carregar();
}

window.onload = carregar