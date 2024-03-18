import re
import time

def analysis(filename : str):

    while True:
        # Open all necessary txt files
        with open('stopwords_ita.txt') as filesw:
            stopwords = filesw.read().splitlines()
        with open(filename,encoding='utf-8') as fprova:
            text = fprova.read()

        # Raw text become readable
        words = text.split()
        clean_words = [word for word in words if word not in stopwords]
        clean_text = ' '.join(clean_words)

        # Simple research for Mails, easy and complex passwords, ibans, cards, exp dates, CVVs
        with open('txtfiles/mail_pw.txt', 'w') as funito,  open('txtfiles/cardinfo.txt', 'w') as fcarte:
            for line in clean_words:
                line = line.strip()
                emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
                registroiban = re.findall(r"\b[A-Z]{2}\d{2}[A-Z\d]{1,30}\b", line) 
                password = re.findall(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!?b @#/\//€$%^&+=]).*$', line) 
                password2 = re.findall (r'^.*(?=.{8,})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).*$',line) 
                carte = re.findall(r'^[0-9]{16}', line)
                scad = re.findall(r'\d{2}/\d{2}',line)
                cvv = re.findall(r'\d{3}', line)

                # Writing what is found
                if(len(emails) > 0):
                    provamail= emails
                    funito.write(str(provamail)+'\n')
                    print(provamail)

                elif(len(registroiban) > 0):
                    iban= registroiban
                    funito.write(str(iban)+'\n')
                    print(iban)

                elif(len(password)>0):
                    provapassword = password
                    funito.write(str(provapassword)+'\n')
                    print(provapassword)

                elif(len(password2)>0):
                    provapassword2 = password2
                    funito.write(str(provapassword2)+'\n')
                    print(provapassword2)

                elif(len(carte)>0):
                    provacarte = carte
                    fcarte.write(str(provacarte)+'\n')
                    print(provacarte)

                elif(len(scad)>0):
                    provascad = scad
                    fcarte.write(str(provascad)+'\n')
                    print(provascad)

                elif(len(cvv)>0):
                    provacvv = cvv
                    fcarte.write(str(provacvv)+'\n')
                    print(provacvv)    
                    

