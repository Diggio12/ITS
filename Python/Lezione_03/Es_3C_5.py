my_dict:dict = {'nome': input('Inserire nome: '), 'ruolo': input('Inserire ruolo: '), 'età': int(input('Inserire età: '))}

match my_dict:
    case my_dict if my_dict['ruolo'] == 'admin':
        print('Accesso completo a tutte le funzionalità.')
    case my_dict if my_dict['ruolo'] == 'moderatore':
        print('Può gestire i contenuti ma non modificare le impostazioni.')
    case my_dict if my_dict['età'] >= 18 and my_dict['ruolo'] == 'utente':
        print('Accesso standard a tutti i servizi.')
    case my_dict if my_dict['età'] <= 18 and my_dict['ruolo'] == 'utente':
        print('Accesso limitato! Alcune funzionalità sono bloccate.')
    case my_dict if my_dict['ruolo'] == 'ospite':
        print('Accesso ristetto! Solo visualizzazione dei contenuti.')
    case _:
        print('Attenzione! Ruolo non riconosciuto! Accesso Negato!')
    
    
