from django.db import models
from mongoengine import *
# Create your models here.
class Url(EmbeddedDocument):
    url = StringField(max_length=100)
    request_type = StringField(max_length=10)

class Field(EmbeddedDocument):
    field = StringField(max_length=50)
    label = StringField(max_length=50)
    data_type = StringField(max_length=50)
    default = StringField(max_length=50)
    field_type = StringField(max_length=50)
    field_type_label = StringField(max_length=50)
    is_removable = StringField(max_length=50)
    mandatory = StringField(max_length=50)
    options_url = EmbeddedDocumentField(Url)
    options_list = ListField()


class Template(Document):
    type = StringField(max_length=25)
    entity = StringField(max_length=25)
    customerId = StringField(max_length=10)
    law = StringField(max_length=15)
    fields = ListField(EmbeddedDocumentField(Field))