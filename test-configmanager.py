import configmanager
#
#   get email from file (not versioned)
#
with open("config/email.txt") as mailfile:
    EMAIL = mailfile.readline().strip()
    print(f"EMAIL: {EMAIL}")
#
#   test configmanager with email
#
print(f"get_config({EMAIL}):", configmanager.get_config(EMAIL))
print(f"get_config_pretty({EMAIL}):", configmanager.get_config_pretty(EMAIL))
print(f"get_password({EMAIL}):", configmanager.get_password(EMAIL))
#
#   test configmanager without email (using the first mail as default)
#
print(f"get_email():", configmanager.get_email())
print(f"get_config():", configmanager.get_config())
print(f"get_config_pretty():", configmanager.get_config_pretty())
print(f"get_password():", configmanager.get_password())
