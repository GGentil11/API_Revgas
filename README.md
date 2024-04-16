Olá!<br />
Este README é destinado a explicar a API de Consulta requisitada.<br />
O código backend e frontend foram feitos utilizando Python e o Web Framework Django, o banco de dados está no MySQL e o deploy foi feito utilizando o Docker.<br />
Para utilizar essa API, será necessário execultar os seguintes passos no terminal:
  - Clone o repositório no diretório desejado utilizando o "git clone https://github.com/GGentil11/API_Revgas/" sem as aspas.
  - Construa a aplicação utilizando "docker-compose up --build" sem as aspas.
Após realizar esses passos, surgirá um link no terminal contendo a URL para o acesso à API


Apesar de estar em produção, deixarei o modo de DEBUG ativado, caso notem algum erro, peço que me enviem para que eu consiga aprender e corrigir.<br />
Erros conhecidos:
  - Ao realizar o "docker-compose up --build", há uma chance do Django carregar antes do MySql, quando isso acontecer, basta esperar o "docker-compose up --build" terminar de carregar, parar o terminal (pode ser com o CRTL + C) e executar "docker-compose up";
  - A página do administrador não está funcionando, peço que evite acessá-la, em breve consiguirei resolver.
