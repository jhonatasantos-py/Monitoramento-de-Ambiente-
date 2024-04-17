import schedule
import time
import smtplib
import email.message
from google.cloud import spanner
from google.oauth2 import service_account
from tabulate import tabulate
import os

# Função para executar a consulta SQL e enviar o email
def consultar_e_enviar_email():  
    # Autenticação no Spanner
    credentials = service_account.Credentials.from_service_account_file(
        r"Local do arquivo de autenticação .json",
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    client = spanner.Client(project="br-digitalcomm-prod", credentials=credentials)
    instance = client.instance("br-digitalcomm-prd")
    database = instance.database("order")

    # Consulta SQL
    sql = """
        Sua consulta em SQL
    """

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(sql)

    headers = ["Pedidos_1P", "Status"]
    data = [(row[0], row[1]) for row in results]

    # Formatação da tabela
    table = tabulate(data, headers, tablefmt="html")
    corpo_email = f"<html><body>{table}</body></html>"

    # Configurações do email
    msg = email.message.Message()
    msg['Subject'] = "Pedidos 1P" # Assunto do email
    msg['From'] = 'xxx@gmail.com' # Remetente
    msg['To'] = 'xxxt@carrefour.com' # Destinatário
    password = os.getenv('EMAIL_PASSWORD') # Obtém a senha do email da variável de ambiente

    # Montagem do email
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    # Envio do email
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# Agendar a função para ser executada a cada hora
schedule.every(30).minutes.do(consultar_e_enviar_email)

# Loop para executar o agendamento
while True:
    schedule.run_pending()
    time.sleep(1)
