# PBI Bot

Bot construido em python + Selenium(framework para automação), tendo como objetivo o download, em formato PDF, dos reports publicado no 
Power Bi Service e o envio desses arquivos por e-mail.

### **Configuração**

A parametrização de quais reports e para quem devem ser enviados é feita através do arquivo /src/config/config-dev.yaml.

A aplicação precisa de uma conta de e-mail para fazer o envio. Na categoria **mailer**  estão as credenciais usadas. Podendo ser
o e-mail e senha de uma pessoa especifica, ou criado um apenas para a aplicação. Só é necessário ajustar a opção user e password dessa opção.

#### Reports
A organização é feita por grupos, e eles devem ter o mesmo nome nas 3 categorias: pbiurl, reports e email.
Exemplo:

A categoria **pbiurl** é onde listamos quais relatórios precisam ser acessados e salvos em pdf. No exemplo abaixo, o **grupo1** recebe apenas o acr.
*  **pbiurl:**
    * **grupo1:** 
        * ab: "https:// xxxxxxxxx" 
    * **grupo2:** 
        * ot: "https:// xxxxxxxxx" 

Na categoria **reports** dizemos onde o navegador salvou o arquivo após fazer o download (normalmente na pasta Downloads). Para obter o caminho
exato e o nome do arquivo, faça um teste baixando o arquivo manualmente. O nome do arquivo não mudará, a menos que seja publicado com outro nome.
Portanto, tome cuidado! se alterar o nome, precisará ajustar as configurações. 
Obs.: Ao término de cada exportação, os arquivos são excluídos. 
*   **reports:**
    * **grupo1:** 
        * ab: "C:/Users/xxx/Downloads/xxxxx.pdf"  
    * **grupo2:** 
        * ot: "C:/Users/xxx/Downloads/xxxxx.pdf"   

Na categoria **email** são parametrizados os e-mails que receberão o arquivo, o assunto do e-mail e o conteúdo.

*  email:
    * **grupo1:**
        * email: "xx@xx.com.br, xxxx@xxxx.com"
        * assunto: '[xx] xx'
        * conteudo: "Seguem anexos os reports."
    * **grupo2:**
        * email: "xx@xx.com.br, xxxx@xxxx.com"
        * assunto: '[Reports] xx'
        * conteudo: "Seguem anexos os reports."

Após essas configurações, abrir o arquivo src/main.py e indicar na variável **grupos_envio** quais são os grupos que devem ser executados.
Exemplo:
*   **grupos_envio** = ['grupo1', 'grupo2']

### Agendamento:

A tarefa pode ser executada de maneira manual ou agendada. Uma sugestão, é utilizar o agendador de tarefas do windows:
*   No bloco de notas, criar um arquivo para fazer a chamada do programa programa python:
    * Exemplo: python C:\Git\xx\xx\src\main.py
*   Salvar com o formato .bat (ex.: bot.bat)
*   Iniciar > Agendador de Tarefas > Agendador de Tarefas (Local) > Ação > Criar Tarefa Básica
    * Configure com que frequencia e horário a tarefa será disparada;
    * Como Ação, selecione "Iniciar um Programa" e procure o arquivo .bat criado anteriormente;
    * Cheque se as outras configurações estão ok e pronto! clique em ok
    * Voltando a tela incial, clique em Biblioteca do Agendador;
    * Sua tarefa deverá estar na lista :)

Obs.: O computador deve estar ligado para que o processo execute.
