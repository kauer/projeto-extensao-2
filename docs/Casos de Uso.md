# Casos de Uso do Professor

### UC-1: Adicionar Disciplina

Ator primário: Professor

Meta no contexto: Criar uma disciplina que irá conter os materiais didáticos a serem referenciados.

Pré-condições: O Professor está autenticado no sistema e está registrado como Professor.

Pós-condições: Uma nova disciplina é criada e poderá receber materiais didáticos ou ser compartilhada com alunos.

Disparador: O Professor clica no botão "adicionar disciplinas" no sistema.

Prioridade: Essencial.

Cenário:

	1. O professor clica no botão "Adicionar Disciplina"
	2. O sistema exibe uma tela perguntando Nome da disciplina, se é pública ou não, e dando a opção de adicionar emails de alunos. Também dá a opção de adicionar fontes ao criar (o que pode também ser feito posteriormente)
	3. O professor insere as opções relevantes e dá OK.
	4. O sistema cria uma nova Disciplina, volta ao menu anterior, e abre a nova disciplina na tela.

Exceções:

	3a. O professor não adiciona Nome à disciplina: O sistema informa que a disciplina não pode ser registrada sem nome.


# Casos de Uso do Aluno

### UC-2: Perguntar ao TutorIA

Ator primário: Aluno

Meta no contexto: Permitir que o aluno tenha acesso ão TutorAI para pedir ajuda nas suas dúvidas de um conteúdo.

Pré-condições: O Aluno está logado, acessou a Disciplina do Professor, e tem permissão pra acessar a Disciplina.

Pós-condições: O TutorIA ajuda o aluno a responder à sua dúvida ou a esclarecer o conteúdo onde o mesmo estava em dúvida.

Disparador: O aluno pede ajuda em um conteúdo ao TutorAI.

Cenário:

  	1.  O aluno acessa o link fornecido pelo professor.
	
	2.  O aluno escreve a sua dúvida no chatbot do TutorAI.
	
	3.  O TutorAI gera uma resposta sobre a matéria.
	
	4.  O TutorAI explica sobre a matéria baseando sua resposta á dúvida do aluno, provendo citações das fontes usadas.
	

Exceções:

  	1a.   Se o aluno não tiver logado/registrado: O sistema avisa o aluno e pede para logar/registrar login.
	
	3a.   Se o TutorAI não tiver acesso à matéria: O sistema avisa ao aluno que o professor não colocou fontes para essa disciplina no seu Banco de Dados ainda e pede para informar ao seu professor sobre isso.
	
	4a.  Se o TutorAI der uma resposta insatisfatoria: O aluno define que o TutorAI deu uma resposta insatisfatoria, o sistema agradece pela sua opinião e tentará não repetir o mesmo tipo de resposta.
