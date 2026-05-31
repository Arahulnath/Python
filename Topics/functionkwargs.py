def user_profile(**kwargs):
    print("User profile")
    for key,value in kwargs.items():
       print (f"{key}:{value}")

user_profile(name="Rahul", age="18",job="Data engineering")