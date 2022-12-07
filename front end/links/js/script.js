//criei uma variavel chamada elemento 
//document acessa o documento html que esta sendo chamado o script
//query selector e um methodo interno do javaScript que nos retorna um elemento html 
var elemento = document.querySelector('h1')
//variavel recebendo inner html para incremento ou alteracao descrtivo
elemento.innerHTML += ' JS';
//variavel elemento recebendo estilizacao de cor 
elemento.style.color = '#red';
//console log e o nosso print retorno variavel
console.log(elemento);

function limpar(event){
    
    event.preventDefault();
    document.querySelector('form').reset();
    console.log('Limpando....');
}

function salvar(event){
    event.preventDefault();
    console.log('salvando....');
    
    var name = document.getElementsByName('nome')[0].value;
    var doc_people = document.getElementsByName('cpf')[0].value;
    var position = document.getElementsByName('cargo')[0].value;
    var monthly_income = document.getElementsByName('salario')[0].value;

    var listaFuncionarios = JSON.parse(localStorage.getItem('Funcionarios'));

    if(listaFuncionarios == null){
        listaFuncionarios = [];
    }
    
    var id = JSON.parse(localStorage.getItem('IdFuncionario'));
    if(listaFuncionarios == null){
        id = 0;
    }
    id = id +1;

    var Funcionario = {
                    'id': id,
                    'nome': name,
                    'cpf': doc_people,
                    'cargo': position,
                    'salario': monthly_income
        };listaFuncionarios.push(Funcionario);

    
    localStorage.setItem('IdFuncionario', JSON.stringify(id));    
    localStorage.setItem('Funcionarios', JSON.stringify(listaFuncionarios));
    limpar(event)
}

document.getElementById('salvar').addEventListener('click', salvar)