input = """
In the vein of The Time Traveler’s Wife and Life After Life, 
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
 

def find_capitalized_letters():
    
    words = input.replace('\n',' ') 
    
    clean_words = words.split(' ')

    #for i in range(len(clean_words)):
    #    print(clean_words[i])
    counter = 0
    cap = []

    for word in clean_words:
        if word == '':
            continue
        elif word[0].isupper() == True:
            cap.append(word) 
            counter += 1
    
    #we're joining all the capital words together to find a potential secret message
    secret = ' '.join(cap) 
    print(secret)

    return counter

print(find_capitalized_letters())