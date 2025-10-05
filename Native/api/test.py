import requests 

r = requests.get("http://127.0.0.1:8000/title=ABC&description=kdfslfsdjflksjdflksjfldsjflk&languages=Python, Javascript&packages=Flask Ball Call; ABC DJC EIR&guide=ifjodisjfoisdjfoi&plans=None")
print(r.json())