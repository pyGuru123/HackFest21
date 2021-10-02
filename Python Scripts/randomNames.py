#pip install names
import names
male = "m"
female = "f"

get = input("Enter m for male name and f for female name: ")


if get == 'm':
    m_name = names.get_full_name(gender= male)
    print(m_name)
elif  get == 'f':
        f_name = names.get_full_name(gender= female)
        print(f_name)
else:
    print("Error you gave wrong input")
   
