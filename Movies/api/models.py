from mongoengine import *
connect('Cinema', host='mongodb', port=27017)


class Movies(Document):
    Title = StringField(require=True,max_length=30)
    Runtime = FloatField()
    Format = StringField()
    Plot = StringField()
    ReleaseYear = FloatField()
    ReleaseMonth = FloatField()
    ReleaseDay = FloatField()

# Create your models here.
