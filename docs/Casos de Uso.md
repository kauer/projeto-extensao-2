# Exemplo de Caso de Uso

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
