# Casos de Uso Nomenclatura:

**UCP - Casos de Uso Professor**

**UCA - Casos de Uso Aluno**

**UCG - Casos de Uso Geral**

# Casos de Uso Gerais

### UCG-1: Login

**Ator primário:** Usuário (Professor ou Aluno)

**Meta no contexto:** Acessar um registro existente no sistema, se identificando como aluno ou professor.

**Pós-condições:** Um registro existente na tabela de Usuários é puxada do Backend, com as informações do Usuário.

**Disparador:** O Usuário abre o site do TutorIA e clica no botão "Logar"

**Prioridade:** Essencial.

**Cenário:**

1. O Usuário clica no botão "Logar"
2. O sistema exibe uma tela perguntando email, senha e nome do Usuário.
3. O Usuário insere as opções relevantes e dá OK.
4. O Usuário faz sua seleção.
5. O Sistema leva o usuário à página inicial.

**Exceções:**

3a. Se faltar alguma informação de login, o sistema notifica o usuário e o impede de seguir.

### UCG-2: Registrar

**Ator primário:** Usuário (Professor ou Aluno)

**Meta no contexto:** Criar um registro no sistema, se identificando como aluno ou professor.

**Pós-condições:** Um novo registro na tabela de Usuários é criada no backend, com as informações do Usuário.

**Disparador:** O Usuário abre o site do TutorIA e clica no botão "Registrar-se"

**Prioridade:** Essencial.

**Cenário:**

1. O Usuário clica no botão "Registrar-se"
2. O sistema exibe uma tela perguntando email, senha, e nome do Usuário.
3. O Usuário insere as opções relevantes e dá OK.
4. O sistema envia um código de confirmação para o email do usuário e exibe uma tela para o Usuário inserir seu código (ou gerar outro código), mostrando o tempo até a expiração do código.
5. O Usuário preenche seu código de confirmação.
6. O sistema passa para a próxima tela, que pergunta se o Usuário é um Professor ou um Aluno.
7. O Usuário faz sua seleção.
8. O Sistema leva o usuário à página inicial.

**Exceções:**

3a. Se faltar alguma informação de registro, o sistema notifica o usuário e o impede de seguir.

5a. Se o código de confirmação do usuário está errado, o sistema notifica o usuário e o impede de seguir.


# Casos de Uso do Professor

### UCP-1: Adicionar Disciplina

**Ator primário:** Professor

**Meta no contexto:** Criar uma disciplina que irá conter os materiais didáticos a serem referenciados.

**Pré-condições:** O Professor está autenticado no sistema e está registrado como Professor.

**Pós-condições:** Uma nova disciplina é criada e poderá receber materiais didáticos ou ser compartilhada com alunos.

**Disparador:** O Professor clica no botão "adicionar disciplinas" no sistema.

**Prioridade:** Essencial.

**Cenário:**

1. O professor clica no botão "Adicionar Disciplina"
2. O sistema exibe uma tela perguntando Nome da disciplina, se é pública ou não, e dando a opção de adicionar emails de alunos. Também dá a opção de adicionar fontes ao criar (o que pode também ser feito posteriormente)
3. O professor insere as opções relevantes e dá OK.
4. O sistema cria uma nova Disciplina, volta ao menu anterior, e abre a nova disciplina na tela.

**Exceções:**

3a. O professor não adiciona Nome à disciplina: O sistema informa que a disciplina não pode ser registrada sem nome.



### UCP-2: Compartilhar Disciplina

**Ator primário:** Professor

**Meta no contexto:** Compartilha uma disciplina existente que contem os materiais didáticos referenciados pelo professor.

**Pré-condições:** O Professor está autenticado no sistema e está registrado como Professor.

**Pós-condições:** Uma disciplina existente é compartilhada com os alunos.

**Disparador:** O Professor clica no botão "Compartilhar Disciplinas" no sistema.

**Prioridade:** Essencial.

**Cenário:**

1. O Professor clica no botão "Compartilhar Disciplina"
2. O sistema exibe uma tela mostrando todas as Disciplinas definidas/existentes do Professor.
3. O Professor seleciona a Disciplina desejada.
4. O Professor altera á visibilidade da Disciplina para pública, anteriormente privada.
5. O sistema altera á visibilidade da Disciplina, notifica os alunos sobre uma nova Disciplina ter sido compartilhada e o sistema exibe uma tela avisando/notificando ao Professor que a visibilidade da Disciplina foi alterada com sucesso.

**Exceções:**

1a. O Professor não adicionou nenhuma Disciplina: O sistema informa que há nenhuma disciplina existente e pede para o Professor criar uma Disciplina primeiro.

5a. O sistema falha em alterar a visibilidade: O sistema cancela todas as suas funções e exibe uma tela avisando/notificando o Professor sobre um erro na alteração da visibilidade da Disciplina por parte do sistema e pede para tentar novamente.



### UCP-3: Adicionar Alunos à Disciplina

**Ator primário:** Professor

**Meta no contexto:** Adicionar Alunos á Disciplina desejada.

**Pré-condições:** O Professor está autenticado no sistema e está registrado como Professor.

**Pós-condições:** Uma disciplina existente recebe novos alunos.

**Disparador:** O Professor clica no botão "Adicionar Alunos" no sistema.

**Prioridade:** Essencial.

**Cenário:**

1. O Professor clica no botão "Adicionar Alunos"
2. O sistema exibe uma tela exibindo todas as Disciplinas definidas/existentes do Professor.
3. O Professor seleciona a Disciplina desejada.
4. O Professor escreve o e-mail de todos os alunos que deseja adicionar à Disciplina e dá OK.
5. O sistema notifica todos os alunos selecionados que foram adicionados á uma nova Disciplina e o sistema exibe uma tela avisando/notificando ao Professor que os Alunos foram adicionados à  Disciplina com sucesso.

**Exceções:**

1a. Não existe nenhum aluno no registrado no sistema: O sistema informa que há nenhum aluno existente e pede para o Professor pedir para os Alunos se registrarem primeiro.

2a. O Professor não adicionou nenhuma Disciplina: O sistema informa que há nenhuma disciplina existente e pede para o Professor criar uma Disciplina primeiro.

3a. Todos os alunos já estão registrados na Disciplina: O sistema informa que há nenhum aluno para ser adicionado, já que todos já foram adicionados á essa Disciplina.

4a. O aluno já está adicionado à Disciplina: O sistema informa que esse email já está adicionado á essa Disciplina.

5a. O sistema falha em adicionar os alunos: O sistema cancela todas as suas funções e exibe uma tela avisando/notificando o Professor sobre um erro no adicionamento dos alunos à Disciplina por parte do sistema e pede para tentar novamente.



### UCP-4: Recebe Feedback

**Ator primário:** Professor

**Meta no contexto:** Acessar um Feedback enviado por um aluno sobre o comportamento/resposta do TutorIA.

**Pós-condições:** Um aluno ter enviado um Feedback sobre o comportamento/resposta do TutorIA.

**Disparador:** O Professor receber uma notificação de um novo Feedback.

**Prioridade:** Essencial.

**Cenário:**

1. O Professor clica no botão “Feedback”
2. O sistema exibe uma tela mostrando os Feedback’s mais recentes, de qual aluno, qual turma, a mensagem enviada pelo TutorIA e uma própria mensagem do aluno detalhando o problema.
3. O Professor seleciona e verifica um Feedback.
4. O Professor sugere uma resposta alternativa ão TutorIA para arrumar os problemas conforme apontados pelo Feedback e dá OK.
5. O sistema recebe e aplica as sugestões, enviando ao aluno á resposta do Professor esclarecida ser do Professor.

**Exceções:**

3a. Se a informação apresentada pelo TutorIA estiver correta e o aluno insistir em estár errada, o professor notificara o aluno sobre o problema não ser parte do TutorIA.

# Casos de Uso do Aluno

### UCA-1: Perguntar ao TutorAI

**Ator primário:** Aluno

**Meta no contexto:** Permitir que o aluno tenha acesso ão TutorAI para pedir ajuda nas suas dúvidas de um conteúdo.

**Pré-condições:** O Aluno está logado, acessou a Disciplina do Professor, e tem permissão pra acessar a Disciplina.

**Pós-condições:** O TutorIA ajuda o aluno a responder à sua dúvida ou a esclarecer o conteúdo onde o mesmo estava em dúvida.

**Disparador:** O aluno pede ajuda em um conteúdo ao TutorAI.

**Prioridade:** Essencial.

**Cenário:**

1. O aluno acessa o link fornecido pelo professor.
2. O aluno escreve a sua dúvida no chatbot do TutorAI.
3. O TutorAI gera uma resposta sobre a matéria.
4. O TutorAI explica sobre a matéria baseando sua resposta á dúvida do aluno, provendo citações das fontes usadas.
	
**Exceções:**

1a. Se o aluno não tiver logado/registrado: O sistema avisa o aluno e pede para logar/registrar login.

3a. Se o TutorAI não tiver acesso à matéria: O sistema avisa ao aluno que o professor não colocou fontes para essa disciplina no seu Banco de Dados ainda e pede para informar ao seu professor sobre isso.

4a. Se o TutorAI der uma resposta insatisfatoria: O aluno define que o TutorAI deu uma resposta insatisfatoria, escolhe se decide opinar sobre a resposta do TutorAI, explica o por que é insatisfatorio e enviado ao professor essa opinião.



### UCA-2: Envia Feedback

**Ator primário:** Aluno

**Meta no contexto:** Permitir ao aluno, caso o chatbot dê uma resposta inadequada, notificar o professor e enviar o contexto do chat e um comentário.

**Pré-condições:** O Aluno está logado, acessou a Disciplina do Professor, e tem permissão pra acessar a Disciplina.

**Pós-condições:** Uma notificação é enviada ao professor para avaliação.

**Disparador:** O aluno clica no botão de "enviar feedback" em uma resposta do chatbot.

**Prioridade:** Importante.

**Cenário:**

1. O aluno acessa o link fornecido pelo professor.
2. O aluno escreve a sua dúvida no chatbot do TutorIA.
3. O TutorIA gera uma resposta sobre a matéria.
4. O aluno clica no botão de "enviar feedback" em uma resposta do TutorIA.
5. O sistema abre uma tela em que o aluno possa escrever uma justificativa para o feedback, além de classificar o problema (erro no chatbot, resposta inadequada, resposta ofensiva, idioma errado, etc.)
6. O aluno preenche o feedback e escolhe uma classificação para o problema, e clica em ok.
7. O sistema agradece pelo feedback e envia a notificação para o professor da disciplina.
	
**Exceções:**

1a. Se o aluno não tiver logado/registrado: O sistema avisa o aluno e pede para logar/registrar login.

3a. Se o TutorIA não tiver acesso aos conteúdos: O sistema avisa ao aluno que o professor não colocou fontes para essa disciplina no seu Banco de Dados ainda e pede para informar ao seu professor sobre isso.

6a. Se o aluno não classificar o problema, o sistema o impede de seguir e indica em vermelho o campo necessário. A descrição textual é opcional, exceto em caso da classificação ser "Outros".

7a. Caso haja um problema no envio da notificação, o sistema notifica o Aluno e pede-o para tentar novamente. 


### UCA-3: Acessar Disciplina
