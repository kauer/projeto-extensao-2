## Descrição geral do sistema
A ideia é um sistema de RAG (Retrieval-Assisted Generation) para servir como um assistente virtual de aprendizado, respondendo dúvidas dos alunos e referenciando o material didático das disciplinas.

O sistema consistirá em um site separado do SIGAA, aonde o aluno seleciona seu Curso e Disciplina desejado. A interface será parecida com um chatbot IA normal (chatGPT, DeepSeek, etc.). Para responder as perguntas do aluno, a LLM fará a pesquisa nos materiais didáticos da Disciplina selecionada e em suas respostas trará referências para de onde foi buscada a informação.


## Requisitos Funcionais
Os requisitos funcionais (RF) descrevem as funcionalidades do sistema, e devem servir de guia para montar o backlog do projeto.

Código - Descrição

RF01 - Fazer o webscraping dos conteúdos didáticos de uma disciplina
RF02 - Montar a base de dados para fazer o retrieval
RF03 - Responder perguntas do usuário
RF04 - Navegar entre diferentes disciplinas/contextos

## Requisitos Não-Funcionais
Os requisitos não-funcionais (RNF) descrevem características do sistema que não
entregam funcionalidades aos usuários, mas descrevem como as funcionalidades devem
ser implementadas. Eles devem refletir nas técnicas utilizadas para implementar os RFs e
guiar o processo de teste e aceitação das entregas do sistema.

Código - Tipo - Descrição

RNF01 - Flexibilidade - Suporte multimodal (pdf, slides, etc) 

RNF02 - Custo - Deve ser o mais baixo possível. Devemos upar o app na infra do IFSC.

RNF03 - Responsividade - Sistema deve ser utilizável em dispositivos móveis com adequação do layout.

RNF04 - Referências - Nas respostas, o sistema deve referenciar com links clicáveis o material didático.
