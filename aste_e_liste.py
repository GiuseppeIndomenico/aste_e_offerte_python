import re

# Si vuole simulare l`andamento di un`asta on line che vuole
# sperimentare una conduzione innovativa; ogni partecipante
# farà una sola offerta ed il pezzo messo all`asta sarà aggiudicato
# al partecipante la cui offerta più si avvicina alla media
# calcolata su tutte le offerte; ogni offerta sarà registrata
# come una coppia [email, offerta_in_euro].
#
# Dovrà essere memorizzata una lista di tutte le offerte pervenute.

# Al termine:
# - dalla lista dovrà essere eliminata l`offerta minima e massima
# - dovrà essere costruita una seconda lista contenente
#   solo le offerte che non discostano più del 10% rispetto alla media
#   calcolata su tutte le offerte rimaste

lista_offerte=[["a@a.com",10], ["b@a.com",15],["c@a.com",55], ["e@a.com",58], ["f@a.com",100], ["d@a.com",150]]
altre_offerte=True

def verificaMail(email, lista_offerte):
    for offerta in lista_offerte:
        if offerta[0] == email:
            return True  # Email trovata
    return False  # Email non trovata

def stampaOfferta(lista_offerte):
    for offerte in lista_offerte:
        print(f"mail offerente: {offerte[0]} - somma offerta: {offerte[1]}€")

    print("-"*50)   
     

def offertaMinima(lista_offerte):
    offerta_minima = lista_offerte[0]  # Inizializza con la prima offerta completa (email e importo)
    for offerta in lista_offerte:
        if offerta[1] < offerta_minima[1]:  # Confronta solo gli importi
            offerta_minima = offerta  # Aggiorna l'intera offerta

    print(f"L'offerta minima dell'asta è stata: {offerta_minima[1]}€")
    print("-" * 50)
    return offerta_minima  # Restituisce l'intera offerta

def offertaMassima(lista_offerte):
    offerta_massima = lista_offerte[0]  # Inizializza con la prima offerta completa (email e importo)
    for offerta in lista_offerte:
        if offerta[1] > offerta_massima[1]:  # Confronta solo gli importi
            offerta_massima = offerta  # Aggiorna l'intera offerta

    print(f"L'offerta massima dell'asta è stata: {offerta_massima[1]}€")
    print("-" * 50)
    return offerta_massima  # Restituisce l'intera offerta



def offertaMedia(lista_offerte):
   somma=0
   for offerta in lista_offerte:
       somma+=offerta[1]
   offerta_media= somma/len(lista_offerte) 
   print(f"l'offerta media è {offerta_media}")    
   print("-"*50)    
   return offerta_media
                


        

while altre_offerte:
    offerta=input("inserisci l'offerta che desideri: (0 per non lasciare un'offerta)   ")
    try:
        offerta=float(offerta)
    except ValueError:
        print("formato non valido, riprova...") 
        continue   
    if offerta==0:
       altre_offerte=False
       continue
    if offerta<0:
       print("non si possono inserire numeri inferiori allo 0!")
       continue
    else:
        email=input("inserisci un email valida a cui assengare l'offerta   ")
    # Regex per validare l'email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Email non valida, riprova.")
            continue
        if verificaMail(email,lista_offerte):
            print("questa mail ha già fatto un'offerta")
        else:
          lista_offerte.append([email,offerta])
          print("l'offerta è stata caricata con successo!")
print("-"*50)
print("ecco le offerte che sono state fatte:")        

stampaOfferta(lista_offerte)

massima=offertaMassima(lista_offerte)
minima=offertaMinima(lista_offerte)    
lista_offerte.remove(massima)
lista_offerte.remove(minima)

media=offertaMedia(lista_offerte)
print("ecco le offerte che sono state fatte rimuovendo la minima e la massima:")        
stampaOfferta(lista_offerte)


tolleranza=media/100*10

print(f"tolleranza del 10% della media delle offerte che sarebbe {media}")

offerte_filtrate=[x for x in lista_offerte if abs(x[1]-media)<= tolleranza]

stampaOfferta(offerte_filtrate)


