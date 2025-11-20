# py_drawer

Script simples em Python para sortear nomes


## Requisitos

- python3 ou superior


## Como usar?

Há duas maneiras de utilizar o py_drawer, uma pelo script `main.py` e outra pelo `drawer_send_mail.py`. Ambos os scripts irá sortear nomes, porém há complexidades diferentes.


### Sobre o `main.py`

Script extremamente simples, que sorteia nomes baseado numa lista de input.


### Sobre o `drawer_send_mail.py`

O script `drawer_send_mail.py` tem como objetivo sortear nomes e enviar via e-mail, pensando naquele sorteio de final de ano onde amigos querem realizar um amigo secreto. Para o seu fucionamento, precisamos seguir algumas etapas, que são elas:

1. Adicionar no arquivo `user_map.py` os nomes e e-mails das pessoas participantes
2. Adicionar um e-mail, dentro do script `drawer_send_mail.py`, que será o remetente do sorteio
  * lembre-se que para enviar e-mail a partir de um app, como esse, é preciso criar uma senha de app no gmail
3. Criar uma mensagem que será enviada no e-mail dos destinatários e adicioná-la na variável `html` dentro do script `drawer_send_mail.py`
4. Executar o `drawer_send_mail.py`

... e não se preocupe, o `drawer_send_mail.py` garante que ninguém tire ela mesma!!


> OBS.: O script conta com comentários dentro do código que ajudarão a preencher o que é necessário

**Limitações do `drawer_send_mail.py`**
* O envio de e-mails é feita somente por um remetente gmail

### Exemplo de execução do script

```bash
$ python3 main.py

# ou #

$ python3 drawer_send_mail.py
```
