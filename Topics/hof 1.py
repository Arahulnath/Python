def gmail_email(username,domain="gmail.com"):
    return f"{username}@{domain}"
def yahoo_email(username,domain="yahoo.com"):
    return f"{username}@{domain}"
def firewall_email(username,domain="yahoo.com"):
    return f"{username}@{domain}"

def email_builder(username,email_fun):#email_fun call another funtion 
    return email_fun(username)#gmail_email(gowtham)->it call gmail_email
print(email_builder("gowtham",gmail_email))
print(email_builder("Rahul",yahoo_email))
print(email_builder("vicky",firewall_email) )