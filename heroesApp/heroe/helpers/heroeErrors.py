# Models imports
from heroe.models import Hero

def hayHeroe(pk):
    try:
        heroe = Hero.objects.get(id = pk)
        
        return True, heroe
    except:
        return False