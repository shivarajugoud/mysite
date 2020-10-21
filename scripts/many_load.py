import csv
from unesco.models import Category,Region,Site,Iso,State
"""
Format
name, description ,justification, year, longitude,
latitude, area, category, states, region, iso

"""

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)
    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    for row in reader:
        print(row)
        si = row[0]
        des = row[1]
        jus = row[2]
        cat, created =Category.objects.get_or_create(name=row[7])
        stat, created =State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        io, created = Iso.objects.get_or_create(name = row[10])
        try:
            y = int(row[3])
        except:
            y = None
        try:
            l = float(row[4])
        except:
            l = None
        try:
            la = float(row[5])
        except:
            la = None
        try:
            a = float(row[6])
        except:
            a = None

        site = Site(name = si,description=des,justification=jus,year=y,longitude=l,latitude=la,area_hectares=a,
        category=cat, states=stat, region=reg, iso=io)
        site.save()
