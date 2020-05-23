import datetime
import random
import smtplib

global date
date = datetime.datetime.now()

global theLatinAlphabet
theLatinAlphabet = 'abcdefgğhıijklmnoöprstuüvyzxqwABCDEFGĞHIİJKLMNOÖPRSTUÜVYZXQW1234567890“é!^¨+%&/()=?_<>£#$½{[]}\₺|-\*~,;`.:@æ´€ '
global theEncryptedAlphabet
theEncryptedAlphabet = ' +0RB4&%];₺W,C1[~}b6Ğ\£@æ82fiÖF*s€xh)^m-!ı3v#.´<$?=¨zjköorpl>M\İIQOuJY½ğLHTUÜnqwAceyGDPSüVZX79“5é(/|{E:`d_KNgta'

global theEncryptedAlphabet2
theEncryptedAlphabet2 = ' +0RB4&%];₺W,C1[~}b6Ğ\£@æ82fiÖF*s€xh)^m-!ı3v#.´<$?=¨zjköorpl>M\İIQOuJY½ğLHTUÜnqwAceyGDPSüVZX79“5é(/|{E:`d_KNgta'
global theLatinAlphabet2
theLatinAlphabet2 = 'abcdefgğhıijklmnoöprstuüvyzxqwABCDEFGĞHIİJKLMNOÖPRSTUÜVYZXQW1234567890“é!^¨+%&/()=?_<>£#$½{[]}\₺|-\*~,;`.:@æ´€ '

def TR():
    def SendMail():
        global mailserver
        global senderMail
        senderMail = input("Gönderici E-Mail Adresini Yazınız :").lower()

        while(senderMail.count("@") != 1 or senderMail.count(".") <= 0 or senderMail.startswith("@") == True or senderMail.endswith("@") == True or senderMail.startswith(".") == True or senderMail.endswith(".") == True or senderMail.count("ü") != 0 or senderMail.count("ı") != 0 or senderMail.count("ö") != 0 or senderMail.count("ş") != 0 or senderMail.count("ç") != 0 or senderMail.count("ğ") != 0):
            print("Geçerli Bir E-Mail Giriniz!")
            senderMail = input("\nGönderici E-Mail Adresini Yazınız :").lower()
        
        global mailPassword
        mailPassword = input("E-Mail Şifrenizi Giriniz :")
        while(mailPassword == ""):
            print("Şifre Boş Olamaz!")
            mailPassword = input("\nE-Mail Şifrenizi Giriniz :")


        global recipientMail
        recipientMail = input("\nAlıcı E-Mail Adresini Yazınız :").lower()
        while(recipientMail.count("@") != 1 or recipientMail.count(".") <= 0 or recipientMail.startswith("@") == True or recipientMail.endswith("@") == True or recipientMail.startswith(".") == True or recipientMail.endswith(".") == True or recipientMail.count("ü") != 0 or recipientMail.count("ı") != 0 or recipientMail.count("ö") != 0 or recipientMail.count("ş") != 0 or recipientMail.count("ç") != 0 or recipientMail.count("ğ") != 0):
            print("Geçerli Bir E-Mail Giriniz!")
            recipientMail = input("\nAlıcı E-Mail Adresini Yazınız :").lower()

        mailserver = smtplib.SMTP("smtp.gmail.com",587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(senderMail, mailPassword)     

    def EnterTR():
        global user
        user = input("Kullanıcı Adınızı Giriniz :")

        global password
        password = input("Şifrenizi Giriniz :")
        
        global randomCode
        randomCode = random.randint(100000,999999)
        print(f"\nDoğrulama Kodu :{randomCode}")
        
        global verificationCode
        verificationCode = input("Doğrulama Kodunu Giriniz :")
        print()
   
    def IncorrectCodeTR():
        print("\nYanlış Kod Girdiniz!\n")       
    
    def IncorrectInfoTR():
        print("Yanlış Bilgi Girdiniz. Sistem Durduruldu!\n")
    
    def EncryptedMessageTR():
        global encryptedMessage
        encryptedMessage = input("\nŞifrelenmesini İstediğiniz Mesajı Giriniz :")
    
    def CrackMessageTR():
        global crackMessage
        crackMessage = input("\nŞifresini Kırmak İstediğiniz Mesajı Giriniz :")      

    EnterTR()   
    counter = 3
    
    while((counter >= 0) and user != "root" or password != "01" or verificationCode != str(randomCode) or verificationCode == ""):    
        counter -= 1
        if(counter == 0):
            IncorrectInfoTR()
            break
        
        else:
            EnterTR()
    
    else:
        print("MY CRYPTOLOGY' E HOŞGELDİNİZ\n")
       
        global chooseMessage
        chooseMessage = "1"
        
        while(chooseMessage != "0"):
            chooseMessage = input("Mesaj Şifrelemek İçin : 1\nMesaj Kırabilmek İçin : 2\nÇıkış İçin : 0\n\nSizin Seçiminiz Hangisi? :")
            
            if(chooseMessage == "1"):
                EncryptedMessageTR()
                openMessage = encryptedMessage.translate(encryptedMessage.maketrans(theLatinAlphabet, theEncryptedAlphabet))
                Array1 = [openMessage]
                print("\n [''] Tek Tırnakların İçindeki İfade Sizin Şifreli Mesajınızdır.\n", Array1)
                with open("TRMessage.txt","a", encoding='utf-8') as file:
                    file.write("Date :" + str(date) + " - " + "Message :")
                    file.writelines(openMessage + "\n")         
    
                wantMail = input("\nŞifrelenmiş Mesajı E-Mail Göndermek İstermisiniz? (E / H) :").upper()
                print()
                if(wantMail == "E"):
                    try:
                        SendMail()
                        mailserver.sendmail(senderMail, recipientMail, openMessage)
                        print("\nE-Mail Gönderildi.\n")
                    except:
                        print("\nE-Mail Gönderilemedi!\n")
                elif(wantMail == "H"):
                    pass
                else:
                    print("Hatalı Seçenek. E-Mail Gönderilmedi!\n")

            elif(chooseMessage == "2"):
                CrackMessageTR()
                openMessage2 = crackMessage.translate(crackMessage.maketrans(theEncryptedAlphabet2, theLatinAlphabet2))
                Array2 = [openMessage2]
                print("\n [''] Tek Tırnakların İçindeki İfade Sizin Kırılmış Mesajınızdır.", "\n", Array2)            
                with open("TRMessageCrack.txt","a", encoding='utf-8') as file:
                    file.write("Date :" + str(date) + " - " + "Message :")
                    file.writelines(openMessage2 + "\n")
                
                wantMail2 = input("\nKırılmış Mesajı E-Mail Göndermek İstermisiniz? (E / H) :").upper()
                print()
                
                if(wantMail2 == "E"):
                    try:
                        SendMail()
                        mailserver.sendmail(senderMail, recipientMail, openMessage2)
                        print("\nE-Mail Gönderildi.\n")
                    except:
                        print("\nE-Mail Gönderilemedi!\n")
                elif(wantMail2 == "H"):
                    pass
                else:
                    print("Hatalı Seçenek. E-Mail Gönderilmedi!\n")
            
            elif (chooseMessage == "0"):
                print("\nÇıkış Sağlandı\n")
            
            else:
                print("\nÇıkış Sağlandı\n")

def ENG():
    def SendMailENG():
        global mailserver
        global senderMail
        senderMail = input("Write the Sender E-Mail Address :").lower()

        while(senderMail.count("@") != 1 or senderMail.count(".") <= 0 or senderMail.startswith("@") == True or senderMail.endswith("@") == True or senderMail.startswith(".") == True or senderMail.endswith(".") == True or senderMail.count("ü") != 0 or senderMail.count("ı") != 0 or senderMail.count("ö") != 0 or senderMail.count("ş") != 0 or senderMail.count("ç") != 0 or senderMail.count("ğ") != 0):
            print("Enter Valid E-mail!")
            senderMail = input("\nWrite the Sender E-Mail Address :").lower()

        global mailPassword
        mailPassword = input("\nEnter Sender E-Mail Password :")
        while(mailPassword == ""):
            print("Password Cannot be Empty!")
            mailPassword = input("\nEnter Sender E-Mail Password :")

        global recipientMail
        recipientMail = input("\nWrite the Recipient E-Mail Address :").lower()
        while(recipientMail.count("@") != 1 or recipientMail.count(".") <= 0 or recipientMail.startswith("@") == True or recipientMail.endswith("@") == True or recipientMail.startswith(".") == True or recipientMail.endswith(".") == True or recipientMail.count("ü") != 0 or recipientMail.count("ı") != 0 or recipientMail.count("ö") != 0 or recipientMail.count("ş") != 0 or recipientMail.count("ç") != 0 or recipientMail.count("ğ") != 0):
            print("Enter Valid E-mail!")
            recipientMail = input("\nWrite the Recipient E-Mail Address :").lower()

        mailserver = smtplib.SMTP("smtp.gmail.com",587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(senderMail, mailPassword)
        
    def EnterENG():
        global user
        user = input("Enter Your User Name :")

        global password
        password = input("Enter Your Password :")
        
        global randomCode
        randomCode = random.randint(100000,999999)
        print(f"\nVerification Code :{randomCode}")
        
        global verificationCode
        verificationCode = input("Enter The Verification Code :")
        print()
   
    def IncorrectCodeENG():
        print("\nIncorrect Code!\n")       
    
    def IncorrectInfoENG():
        print("Incorrect Information. The System Was Shut Down!\n")
    
    def EncryptedMessageENG():
        global encryptedMessage
        encryptedMessage = input("\nEnter The Message You Want To Encrypt :")
    
    def CrackMessageENG():
        global crackMessage
        crackMessage = input("\nEnter The Message You Want To Crack :")
    
    EnterENG()   
    counter = 3
    
    while((counter >= 0) and user != "root" or password != "01" or verificationCode != str(randomCode) or verificationCode == ""):    
        counter -= 1
        if(counter == 0):
            IncorrectInfoENG()
            break
        
        else:
            EnterENG()
    
    else:
        print("WELCOME TO MY CRYPTOLOGY\n")
       
        global chooseMessage
        chooseMessage = "1"
        
        while(chooseMessage != "0"):
            chooseMessage = input("To Encrypt Message : 1\nTo Crack Message   : 2\nTo Quit : 0\n\nWhich Is Your Choose? :")
            
            if(chooseMessage == "1"):
                EncryptedMessageENG()
                openMessage = encryptedMessage.translate(encryptedMessage.maketrans(theLatinAlphabet, theEncryptedAlphabet))
                Array1 = [openMessage]
                print("\n [''] The Expression in Single Quotes is Your Encrypted Message.\n", Array1)
                with open("ENGMessage.txt","a", encoding='utf-8') as file:
                    file.write("Date :" + str(date) + " - " + "Message :")
                    file.writelines(openMessage + "\n")
                
                wantMail = input("\nWould You Like To Send The Encrypted Message By E-Mail? (Y / N) :").upper()
                print()
                
                if(wantMail == "Y"):
                    try:
                        SendMailENG()
                        mailserver.sendmail(senderMail, recipientMail, openMessage)
                        print("\nE-Mail Sent.\n")
                    except:
                        print("\nE-Mail Failed!\n")
                elif(wantMail == "N"):
                    pass
                else:
                    print("Incorrect Option. E-Mail Failed!\n")

            elif(chooseMessage == "2"):
                CrackMessageENG()
                openMessage2 = crackMessage.translate(crackMessage.maketrans(theEncryptedAlphabet2, theLatinAlphabet2))
                Array2 = [openMessage2]

                print("\n [''] The Expression in Single Quotes is Your Broken Message.\n", Array2)               
                
                with open("ENGMessageCrack.txt","a", encoding='utf-8') as file:
                    file.write("Date :" + str(date) + " - " + "Message :")
                    file.writelines(openMessage2 + "\n")

                wantMail2 = input("\nWould You Like To Send The Cracked Message By E-Mail? (Y / N) :").upper()
                print()

                if(wantMail2 == "Y"):
                    try:
                        SendMailENG()
                        mailserver.sendmail(senderMail, recipientMail, openMessage2)
                        print("\nE-Mail Sent.\n")
                    except:
                        print("\nE-Mail Failed!\n")
                elif(wantMail2 == "N"):
                    pass
                else:
                    print("\nIncorretc Option. E-Mail Failed!\n")
                
            elif (chooseMessage == "0"):
                print("\nSigned Out\n")
            
            else:
                print("\nSigned Out\n")

language = input("Türkçe İçin :1\nFor English :2\nDil - Language :")

print()

if(language == "1"):
    TR()

elif(language == "2"):
    ENG()

else:
    print("TR  : Yanlış Seçenek. Sistem Kapatıldı. \nENG : Incorrect Option. System Shut Down.\n")