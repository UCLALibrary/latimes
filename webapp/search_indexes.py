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
  BoxNumber = indexes.IntegerField(model_attr="BoxNumber", faceted=True)
  Negative = indexes.IntegerField(model_attr="Negative", faceted=True)
  Year = indexes.IntegerField(model_attr="Year", faceted=True)
  
  suggestions = indexes.FacetCharField()
  
  def get_model(self):
    return Card

