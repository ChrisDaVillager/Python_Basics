animes = ['Ranking of Queens', 'Demon SLayer', 'Tokyo Ghoul']
print(animes)

for x in range(len(animes)):
    if animes[x] == 'Ranking of Queens':
        animes[x] = 'Ranking of Kings'
    elif animes[x] == 'Demon SLayer':
        animes[x] = 'Demon Slayer'
print(animes)

animes.insert(0, 'Spy x Family')
print(animes)

animes.append('Overlord')
print(animes)