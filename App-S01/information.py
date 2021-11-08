import model
import math
import config as cf
import csv
assert cf

artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
input_file_artists = csv.DictReader(open(artistsfile, encoding='utf-8'))
input_file_artworks = csv.DictReader(open(artworksfile, encoding='utf-8'))

num_artists = 0
num_artworks = 0
departments_list = []
birth_years_list = []
nationalities_list = []
adquistion_years_list = []

for artist in input_file_artists:
    birth_year = artist['BeginDate']
    nationality = artist['Nationality']
    if birth_year not in birth_years_list:
        birth_years_list.append(birth_year)
    if nationality not in nationalities_list:
        nationalities_list.append(nationality)
    num_artists += 1

for artwork in input_file_artworks:
    adquistion_year = model.getAdquisitionYear(artwork['DateAcquired'])
    department = artwork['Department']
    if adquistion_year not in adquistion_years_list:
        adquistion_years_list.append(adquistion_year)
    if department not in departments_list:
        departments_list.append(department)
    num_artworks += 1

def isPrime(n):
    if n <= 1:
         return False
    if n <= 3:
         return True
    if n % 2 == 0 or n % 3 == 0:
        return False  
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False 
    return True
 
def nextPrime(N):
    if N <= 1:
        return 2
    prime = N
    found = False
    while not found:
        prime = prime + 1
 
        if isPrime(prime) == True:
            found = True
    return prime

print('Número de artistas:', num_artists)
print('Número de obras de arte:', num_artworks)
print('Número de años de nacimiento:', len(birth_years_list))
print('Número de años de adquisición:', len(adquistion_years_list))
print('Número de nacionalidades:', len(nationalities_list))
print('Número de departamentos:', len(departments_list))
print('''Número de elementos iniciales de catalog['artists_Ids'] y catalog['artists_names']:''', nextPrime(num_artists*2))
print('''Número de elementos iniciales de catalog['artworks']:''', nextPrime(num_artworks*2))
print('''Número de elementos iniciales de catalog ['birth_years']:''', nextPrime(len(birth_years_list)*2))
print('''Número de elementos iniciales de catalog['adquisition_years']:''', nextPrime(len(adquistion_years_list)*2))
print('''Número de elementos iniciales de catalog['nationalities']:''', nextPrime(len(nationalities_list)*2))
print('''Número de elementos iniciales de catalog['departments']:''', nextPrime(len(departments_list)*2))