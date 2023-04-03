#Patrcia Silva Ribeiro
#Faculdade CDL
#@patriciasrbr


import instaloader

bot = instaloader.Instaloader()

#TAG a ser pesquisada
top_five = instaloader.TopSearchResults(bot.context, 'chatgpt')

hashtags = top_five.get_hashtags()
profiles = top_five.get_profiles()

#print(hashtags)
list_hashtags = []
for hashtag in hashtags:
    list_hashtags.append(hashtag.name)
print(list_hashtags)
#print(perfis)
for profile in profiles:
    print(profile)
    
