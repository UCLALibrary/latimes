from haystack import indexes
from haystack.fields import CharField

from .models import Card

class CardIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(
  document=True, use_template=True,
  template_name='/Users/cliccuser/latimes/webapp/templates/search/indexes/card_text.txt')
  SubjectName = indexes.CharField(model_attr='SubjectName')
  SubjectDescription = indexes.CharField(model_attr="SubjectDescription")
  PhotoDescription = indexes.CharField(model_attr="PhotoDescription")

  def get_model(self):
    return Card
