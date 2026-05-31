def email_builder(domain):
    def email_fun(username):
        return f"{username}@{domain}"
    return email_fun
gmail=email_builder("gamil.com")
yamil=email_builder("yamil.com")
hotmail=email_builder("hotmail.com")
print(gmail("gowtham"))
print(yamil("Rahul"))
print(hotmail("Vicky"))