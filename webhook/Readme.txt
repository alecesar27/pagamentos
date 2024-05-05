 !!!!!!!!!!!!!!!!!ATENÇÂO!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!LEIA!!!!!!!!!!!!!!!!!!!!!!

Segui todos os requisitos abaixo. O sistema já está totalmente operante e
com a base de dados com todas as informações. Para limpar o banco e carregar
as informações  favor acessar o arquivo testes.py e executar as informações
Parti do princípio que o portal da Hastag foi acessado por um cliente que cadastrou
o seu email, selecionou um curso desejado e realizaou o pagamento.
Criei 20 webhooks com diferentes retornos: Aprovado, Recusado e Reembolsado. A função pode
ser disparada de tempos em tempos no caso 1 minuto para a coleta  e tratramento  das informações.
O sistema além de realizar o print envia um email para o cliente informando está totalmente funcional
testei com a minha conta e token gerados no portal da Google para o Gmail. Por questões de segurança
não coloquei. Além disso o sistema gera relatórios de clientes com as respectivas situações e dos pagamentos
Além disso também gera relatórios em csv tanto para cliente quanto para pagamento. Pensei em mais
funcionalidades como relatório dos clientes com os respctivos cursos. Inclusive alimentei a tabela
de Cliente_Curso. Porém surgiram alguns imprevistos e não pude concluir então priorizei o que foi pedido.
Atenciosamente,

Alex






Sua API deve ser construída usando Flask

Simulador dos webhooks:
https://simuladorwebhook-production.up.railway.app/

- A gente precisa criar um sistema que recebe um webhook do sistema de pagamento e decida como vamos tratar o cliente

- se o cliente tem o pagamento aprovado, então devemos:
	- liberar o acesso dele ao curso
	- enviar mensagem de boas vindas
- se o cliente tem o pagamento recusado
	- enviar mensagem de pagamento recusado
- se o cliente tem o status reembolsado
	- tirar o acesso dele ao curso
- Precisamos ter registrado (para poder consultar quando precisarmos) todos os webhooks que chegaram e todas as "tratativas" que o sistema fez.
	Ex: se o sistema mandou liberar o acesso ao curso e enviou mensagem, tem que ter um registro que o sistema fez isso (no banco de dados mesmo)
- o sistema precisa ter autenticação de login para só poder entrar usuários autorizados. A criação de conta só pode ser feita por usuários que tenham o token: uhdfaAADF123 que deve ser enviado junto do formulário de criação de conta
- os usuários devem ter 1 tela onde possam ver todas as tratativas que o sistema fez para cada usuário e que seja possível pesquisar por um usuário e ver o que rolou com ele

As funcionalidades de enviar mensagem, tirar acesso e liberar acesso não precisam "fazer nada", só precisam "printar o que seria feito", do tipo:
print("Liberar acesso do e-mail: fulano@email.com")
ou então
print("Enviar mensagem de boas vindas para o email: fulano@email.com")