# Script de Consulta e Envio de Email

Este script Python realiza consultas em um banco de dados Spanner, formata os resultados em uma tabela HTML e envia esses resultados por email. Ele utiliza a biblioteca `schedule` para agendar a execução periódica da função de consulta e envio de email.

## Funcionamento do Script

1. **Importação de Bibliotecas:**
    - `schedule`: Biblioteca para agendar tarefas.
    - `time`: Módulo para trabalhar com tempo.
    - `smtplib`: Biblioteca para enviar emails.
    - `email.message`: Classe para manipulação de mensagens de email.
    - `google.cloud.spanner`: Cliente para acessar o Spanner.
    - `google.oauth2.service_account`: Módulo para autenticação via conta de serviço.
    - `tabulate`: Biblioteca para formatar os resultados da consulta em uma tabela.

2. **Função `consultar_e_enviar_email()`:**
    - Realiza autenticação no Spanner com as credenciais fornecidas.
    - Executa uma consulta SQL no banco de dados Spanner.
    - Formata os resultados da consulta em uma tabela HTML usando a biblioteca `tabulate`.
    - Configura as informações do email, como assunto, remetente, destinatário e senha.
    - Monta o email com o corpo formatado em HTML.
    - Envia o email usando SMTP.

3. **Consulta SQL:**
    - Realiza uma consulta SQL complexa que envolve várias tabelas do banco de dados.
    - Filtra os resultados com base em critérios específicos, como datas e tipos de entrega.
    - Agrupa os resultados por status.

4. **Agendamento e Execução Periódica:**
    - Utiliza o `schedule` para agendar a execução da função `consultar_e_enviar_email()` a cada 30 minutos.
    - Executa um loop infinito que verifica periodicamente se há tarefas agendadas para execução e as executa.
    - Usa `time.sleep(1)` para evitar uso excessivo da CPU enquanto aguarda a próxima execução agendada.

## Observações
- Certifique-se de substituir as informações de autenticação, como o caminho do arquivo JSON de credenciais do Google Cloud e as informações do email, com suas próprias credenciais.
- O script é configurado para enviar emails usando o servidor SMTP do Gmail. Certifique-se de que as configurações de segurança e permissões estejam corretas em sua conta do Gmail.
- A consulta SQL pode precisar ser ajustada para atender aos requisitos específicos do banco de dados.

