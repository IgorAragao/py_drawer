import random
import smtplib
from email.message import EmailMessage


# variavel que acomoda os emails para envio dos nomes
emails_destinatarios = input("Insira os emails (gmail) destinatarios separados por espaço: ").split()


# variavel que acomoda os emails que ja foram enviados
emails_ja_enviados = []


# variavel que acomoda os nomes a serem sorteados
names_input = input("Digite os nomes a serem sorteados separados por espaço: ").split()


# variavel que acomoda os nomes que ja foram sorteados
names_drawn = []


def conn_mail():
    try:
        servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_email.starttls()
        servidor_email.login('<add_email>', 'add_password_app') # adicionar email gmail
        return servidor_email
    except Exception as err:
        print(f"[ERROR] ❌ {err}")
        return None


def conn_close(conexao):
    if conexao is None:
        print("[ERROR] ❌ Conexão de email não estabelecida!")
    else:
        print("[INFO] Conexão encerrada!")
        conexao.quit()


def send_mail(servidor_email, dest, name):

    msg = EmailMessage()
    msg['Subject'] = '<add_assunto>'
    msg['From'] = '<add_email_remetente>'
    msg['To'] = dest

    msg.set_content(
        f'<Add_message>\n'
        f'Seu amigo secreto é: {name}' # Linha com o nome do amigo secreto sorteado
    )

    servidor_email.sendmail(msg['From'], [dest], msg.as_string())


def drawer():
    conexao = conn_mail()

    try:
        if conexao is not None:

            while len(names_input) > 0:
                start = input('Sortear? (Sim ou Não): ')

                if start.lower() == 'sim':

                    num_name = random.randrange(0, len(names_input))
                    name = names_input[num_name]

                    names_drawn.append(name)

                    num_mail =  random.randrange(0, len(emails_destinatarios))
                    email = emails_destinatarios[num_mail]
                    send_mail(conexao, email, name)
                    emails_ja_enviados.append(email)


                    emails_destinatarios.remove(email)
                    names_input.remove(name)

                    print(f'Nome sorteado: {name}')
                    print(f'Nomes já sorteados: {names_drawn}')
                    print(f'Nomes faltantes: {names_input}')

                    print(f'email enviado: {email}')
                    print(f'email já enviado: {emails_ja_enviados}')
                    print(f'email faltantes: {emails_destinatarios}')


                else:
                    print('py_drawer encerrado!')
                    exit()

        else:
            exit()

    except Exception as err:
        print(f"[ERROR] ❌ Falha ao enviar o email: {err}")

    finally:
        conn_close(conexao)


def main():
    drawer()


if __name__ == "__main__":
    main()
