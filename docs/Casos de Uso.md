# Exemplo de Caso de Uso: Professor

Caso de Uso:   Registrar Pedido de Compra

Ator primário:    Cliente

Meta no contexto:   Permitir que o cliente registre um pedido com um ou mais produtos disponíveis no catálogo.

Pré-condições:   O cliente está autenticado no sistema.

Pós-condições:   Um novo pedido é criado e armazenado com seus itens e valor total.

Disparador:   O cliente decide realizar uma compra.

Cenário:

  1. O cliente acessa a funcionalidade de “Novo Pedido”.
  2. O sistema exibe o catálogo de produtos disponíveis.
  3. O cliente seleciona os produtos desejados e informa as quantidades.
  4. O sistema calcula o valor parcial de cada item com base na quantidade e no preço do produto.
  5. O cliente confirma o pedido.
  6. O sistema calcula o valor total do pedido e armazena o pedido com data, valor e
produtos associados.

Exceções:

  3a. O cliente não seleciona nenhum produto: O sistema informa que o pedido não pode ser registrado sem produtos.

Prioridade:   Essencial.

Quando disponível:   Primeira versão.

Frequência de uso:   Várias vezes por dia.

Canal com o ator:   Interface web ou aplicativo móvel.

Atores secundários:   Não há.

Canais com atores secundários:   Não há.

Questões em aberto:   Não há.


# Exemplo de Caso de Uso: Aluno

Caso de Uso:    Pedir Conteúdo

Ator primário:    Aluno

Meta no contexto:   Permitir que o aluno tenha acesso ão TutorAI para pedir ajuda nas suas dúvidas de um conteúdo.

Pré-condições:   O Aluno acessou o TutorAI via link do Professor.

Pós-condições:   O TutorAI ajuda o aluno á responder á sua dúvida ou á esclarecer o conteúdo onde o mesmo estava em dúvida.

Disparador:   O aluno pede ajuda em um conteúdo ao TutorAI.

Cenário:

  1.  O aluno acessa o link fornecido pelo professor.
	2.  O aluno escreve a sua dúvida ão TutorAI.
	3.  O TutorAI procura sobre a matéria.
	4.  O TutorAI explica sobre a matéria baseando sua resposta á dúvida do aluno.

Exceções:

  1a.   Se o aluno não tiver logado/registrado: O sistema avisa o aluno e pede para logar/registrar login.
	3a.   Se o TutorAI não tiver acesso á matéria: O sistema avisa ão aluno que o professor não colocou essa matéria no seu Banco de Dados ainda e pede para informar ao seu professor sobre isso.
	4a.  Se o TutorAI der uma resposta insatisfatoria: O aluno define que o TutorAI deu uma resposta insatisfatoria, o sistema agradece pela sua opinião e tentara não repetir o mesmo tipo de resposta.

Prioridade:   Essencial.

Quando disponível:   Primeira versão.

Frequência de uso:   Várias vezes por dia.

Canal com o ator:   Interface web ou aplicativo móvel.

Atores secundários:   Não há.

Canais com atores secundários:   Não há.

Questões em aberto:   Não há.
