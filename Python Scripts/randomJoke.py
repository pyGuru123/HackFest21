
#Python Program to Generate Random Jokes


# Import the necessary package
import pyjokes

# Fetch the joke
joke1 = pyjokes.get_joke(language="en", category="all")

# Display the joke
print(joke1,"\n")

# Different category
joke2 = pyjokes.get_joke(language="en", category="neutral")

# Display the joke
print(joke2,"\n")

# Fetch multiple jokes
jokes = pyjokes.get_jokes(language="en", category="neutral")

# for loop till 5
for i in range(5):
    print(i+1,".",jokes[i],"\n")

# Output
# How many programmers does it take to kill a cockroach? Two: one holds, the other installs Windows on it. 

# What's the object-oriented way to become wealthy? Inheritance. 

# 1 . Complaining about the lack of smoking shelters, the nicotine addicted Python programmers said there ought to be 'spaces for tabs'. 

# 2 . Ubuntu users are apt to get this joke. 

# 3 . Obfuscated Reality Mappers (ORMs) can be useful database tools. 

# 4 . Asked to explain Unicode during an interview, Geoff went into detail about his final year university project. He was not hired. 

# 5 . Triumphantly, Beth removed Python 2.7 from her server in 2030. 'Finally!' she said with glee, only to see the announcement for Python 4.4. 