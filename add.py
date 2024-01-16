import requests

# Definisci i dati da inviare nel corpo della richiesta POST
data = {
    'username': 'nuovo_utente',
    'email': 'nuova_email@example.com'
}

# Esegui la richiesta POST al tuo server Flask
response = requests.post('http://127.0.0.1:5000/add_user', data=data)

# Stampa la risposta dal server
print(response.text)
