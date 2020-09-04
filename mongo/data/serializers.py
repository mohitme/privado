from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from data.models import Template, Field, Url

class UrlSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Url
        fields = '__all__'

class FieldSerializer(EmbeddedDocumentSerializer):
    options_url = UrlSerializer(many=False)
    class Meta:
        model = Field
        fields = ('label','data_type','default','field_type','field_type_label','mandatory','options_url','options_list')

class TemplateSerializer(DocumentSerializer):
    fields = FieldSerializer(many=True)
    class Meta:
        model = Template
        fields = ('id','entity','customerId','law','fields')