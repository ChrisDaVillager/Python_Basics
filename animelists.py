animes = ['Ranking of Queens', 'Demon SLayer', 'Tokyo Ghoul']
print(animes)
# Output: ['Ranking of Queens', 'Demon SLayer', 'Tokyo Ghoul']

for x in range(len(animes)):
    if animes[x] == 'Ranking of Queens':
        animes[x] = 'Ranking of Kings'
    elif animes[x] == 'Demon SLayer':
        animes[x] = 'Demon Slayer'
print(animes)
# Output: ['Ranking of Kings', 'Demon Slayer', 'Tokyo Ghoul']

animes.insert(0, 'Spy x Family')
print(animes)
# Output: ['Spy x Family', 'Ranking of Kings', 'Demon Slayer', 'Tokyo Ghoul']

animes.append('Overlord')
print(animes)
# Output: ['Spy x Family', 'Ranking of Kings', 'Demon Slayer', 'Tokyo Ghoul', 'Overlord']

print(animes[3])
# Output: Tokyo Ghoul
