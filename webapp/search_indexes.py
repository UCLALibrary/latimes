from haystack import indexes
from haystack.fields import CharField

from .models import Card

class CardIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(
  document=True, use_template=True,
  template_name='/Users/cliccuser/latimes/webapp/templates/search/indexes/card_text.txt')
  SubjectName = indexes.CharField(model_attr='SubjectName', faceted=True)
  SubjectDescription = indexes.CharField(model_attr="SubjectDescription", faceted=True)
  PhotoDescription = indexes.CharField(model_attr="PhotoDescription", faceted=True)
  Photographer = indexes.CharField(model_attr="Photographer", faceted=True)
  Location = indexes.CharField(model_attr="Location", faceted=True)
  BoxNumber = indexes.IntegerField(model_attr="BoxNumber", faceted=True)
  Negative = indexes.CharField(model_attr="Negative", faceted=True)
  Year = indexes.IntegerField(model_attr="Year", faceted=True)
  Day = indexes.IntegerField(model_attr="Day", faceted=True)
  Month = indexes.IntegerField(model_attr="Month", faceted=True)
  date = indexes.CharField(model_attr="date", faceted=True)
  Quantity = indexes.IntegerField(model_attr="Quantity", faceted=True)
  suggestions = indexes.FacetCharField()
  
  def get_model(self):
    return Card

