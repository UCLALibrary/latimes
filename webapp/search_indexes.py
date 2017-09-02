from haystack import indexes
from haystack.fields import CharField
from django.core.validators import validate_comma_separated_integer_list


from .models import Card

class CardIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(
  document=True, use_template=True,
  template_name='/Users/niqui/latimes/webapp/templates/search/indexes/card_text.txt')
  SubjectName = indexes.CharField(model_attr='SubjectName', faceted=True, null=True)
  SubjectDescription = indexes.CharField(model_attr="SubjectDescription", faceted=True, null=True)
  PhotoDescription = indexes.CharField(model_attr="PhotoDescription", faceted=True, null=True)
  Photographer = indexes.CharField(model_attr="Photographer", faceted=True, null=True)
  Location = indexes.CharField(model_attr="Location", faceted=True, null=True)
  BoxNumber = indexes.CharField(model_attr="BoxNumber", faceted=True, null=True)
  Negative = indexes.CharField(model_attr="Negative", faceted=True, null=True)
  Year = indexes.IntegerField(model_attr="Year", faceted=True, null=True)
  Day = indexes.IntegerField(model_attr="Day", faceted=True, null=True)
  Month = indexes.IntegerField(model_attr="Month", faceted=True, null=True)
  date = indexes.CharField(model_attr="date", faceted=True, null=True)
  Quantity = indexes.IntegerField(model_attr="Quantity", faceted=True, null=True)
  suggestions = indexes.FacetCharField()
  
  def get_model(self):
    return Card

