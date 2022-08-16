input = """In the vein of The Time Traveler’s Wife and Life After Life, 
The Invisible Life of Addie LaRue is New York Times bestselling author V. E. Schwab’s
genre-defying tour de force. A Life No One Will Remember. A Story You Will Never Forget.
France, 1714: in a moment of desperation, a young woman makes a Faustian bargain to live 
forever—and is cursed to be forgotten by everyone she meets. Thus begins the extraordinary 
life of Addie LaRue, and a dazzling adventure that will play out across centuries and continents, 
across history and art, as a young woman learns how far she will go to leave her mark on the world. 
But everything changes when, after nearly 300 years, Addie stumbles across a young man in a hidden 
bookstore and he remembers her name. """

# Problem: Find the # of capitalized words in this paragraph

# TODO: Any improvements to this algo?
# TODO: Anywhere we can do more pythonic code?

# TODO: Put several messages into several different files on disk,
#       then, open them one at a time, and find the secret
#       look at messages/ dir

# TODO: Encrypt the secret message
# TODO: Find how many times each lower case letter starts a word. 
# TODO: Find all the unique words in the string
# TODO: Email secret message to friend, give them the key to decrpyt message

file_paths = ["messages/acleanwelllightedplace.log","messages/punk57.log","messages/thetyger.log"]

def find_new_file(path):
    hold_guts = ""

    for i in path:
        with open(i, 'r') as f:
            input = f.read()
        hold_guts += input
    
    return hold_guts
        

def find_secret_message(secret_file):
  
    words = secret_file.replace('\n',' ') 
    clean_words = words.split(' ')

    counter_upper = 0
    counter_lower = 0
    cap = []

    for word in clean_words:
        if word == '':
            continue
        elif word[0].isupper() == True:
            cap.append(word) 
            counter_upper += 1
        elif word[0].isupper() == False:
            counter_lower += 1

    filtered_cap = []
    [filtered_cap.append(i) for i in cap if i not in filtered_cap]

    #we're joining all the capital words together to find a potential secret message
    secret = ' '.join(filtered_cap)
    
    return secret, counter_upper, counter_lower

content = find_new_file(file_paths)
found_message, num_uppercase, num_lowercase = find_secret_message(content)

print(found_message, f"\nNumber of uppercase words: {num_uppercase}", f"\nNumber of lowercase words: {num_lowercase}")