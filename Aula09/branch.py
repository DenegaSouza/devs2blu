"""
Branch é uma linha temporal. 
A principal é 'main'.
homolog: é a parte de confirmação do código de produção. Está em testes, juntar códigos.
dev: validação que trabalha com o que estava sendo feito. A parte do código já está funcionando

"""

# CRIAR BRANCH chamada 'homolog'
-> git checkout -b homolog

# ENVIAR BRANCH 'homolog' PARA GITHUB
-> git push -u origin homolog

# VERIFICAR BRANCH
-> git branch

# MUDAR PARA A BRANCH 'main'
-> git checkout main

# DELETAR BRANCH 'teste'
-> git branch -D teste

# RENOMEAR BRANCH
-> git branch -m novo_nome