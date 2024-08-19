#this is the Automated whatsapp messaging program
#it can send a message to unlimited contacts
# soon we will make it able to send emails too........... 
#please check you internet connection and connect o whatsapp web before you run this code 

#importing required libraries
import pywhatkit as kit
import vobject

#Requierd data to send the message
file_path = r"the path of you vcf file"
country_code = "your country code : like  '+123'"
message = "the message you want to send"

#the our when you want to send the message 'in 24 form'
hour = 15

#and the minute too
minute = 00

#a function to read the contacts from a vcf file
def read_vcf(file_path,country_code):
    
    #creat alist to store the contacts
    contacts = []

    #a counter we will need it in a coming loop 
    count = 0  

    #here we open the vcf file 
    with open(file_path, 'r') as file:
        
        #a loop to access to every single contact and store its details 
        for vcard in vobject.readComponents(file):
            contact = {
                'name': '',
                'phone': '',
                'email': ''
            }

            #here we store the phone number and make it acceptable to whatsapp web 
            if 'tel' in vcard.contents:
               phone_no = vcard.contents['tel'][0].value
            
            #add the country code to the phone number
            if not phone_no.startswith(country_code):
                phone_no = country_code + phone_no

            #removing any spaces from the phone number
            for digit in phone_no : 
                if digit == "-" :
                    phone_no = phone_no.replace("-" , "" , count)

                count = count + 1    

            #finally we store the phone number in our dictionary   
            contact['phone'] = phone_no
            
            #we store the email address too because we will need it in the next project
            if 'email' in vcard.contents:
               contact['email'] = vcard.contents['email'][0].value
            
            #here we add the contact to our list of contacts
            contacts.append(contact)
    
    return contacts
    
    
#calling our function
contacts = read_vcf(file_path,country_code)

#thats a delay time between the messages
delay = 2

#a loop to send the message to every single contact from the vcf file
for contact in contacts:
   #these method takes a four parameters (reciver phone number , message to send , the hour in 24 form , and the minute)
   kit.sendwhatmsg(contact['phone'], message , hour , minute + delay)

   