from haystack import indexes
from haystack.fields import CharField

from .models import Card, BoxNumb

class CardIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(
  document=True, use_template=True)
  SubjectName = indexes.CharField(model_attr='SubjectName', faceted=True, null=True)
  SubjectDescription = indexes.CharField(model_attr="SubjectDescription", faceted=True, null=True)
  PhotoDescription = indexes.CharField(model_attr="PhotoDescription", faceted=True, null=True)
  Photographer = indexes.CharField(model_attr="Photographer", faceted=True, null=True)
  Location = indexes.CharField(model_attr="Location", faceted=True, null=True)
  BoxNumber = indexes.MultiValueField(indexed=True, stored=True)
  Negative = indexes.CharField(model_attr="Negative", faceted=True, null=True)
  Year = indexes.IntegerField(model_attr="Year", faceted=True, null=True)
  Day = indexes.IntegerField(model_attr="Day", faceted=True, null=True)
  Month = indexes.IntegerField(model_attr="Month", faceted=True, null=True)
  date = indexes.CharField(model_attr="date", faceted=True, null=True)
  Quantity = indexes.IntegerField(model_attr="Quantity", faceted=True, null=True)
  DateCombine = indexes.DateField(model_attr="DateCombine", faceted=True, null=True)
  suggestions = indexes.FacetCharField()
  
  def get_model(self):
    return Card
  def prepare_BoxNumber(self, object):
  	return [BoxNumber.box for BoxNumber in object.BoxNumber.all()]

