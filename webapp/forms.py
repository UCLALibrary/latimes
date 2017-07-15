from haystack.forms import FacetedSearchForm
from django import forms

class FacetedCardSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.Year = data.get('Year', [])
        self.BoxNumber = data.get('BoxNumber', [])
        self.Negative = data.get('Negative', [])
        super(FacetedCardSearchForm, self).__init__(*args, **kwargs)
        

    def search(self):
        sqs = super(FacetedCardSearchForm, self).search()
        if self.BoxNumber:
            query = None
            for BoxNumber in self.BoxNumber:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(BoxNumber)
            sqs = sqs.narrow(u'BoxNumber_exact:%s' % query)
        if self.Negative:
            query = None
            for Negative in self.Negative:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Negative)
            sqs = sqs.narrow(u'Negative_exact:%s' % query)
        if self.Year:
            query = None
            for Year in self.Year:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Year)
            sqs = sqs.narrow(u'Year_exact:%s' % query)
        return sqs

class FacetedCardAdvancedSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.SubjectName = data.get('SubjectName', [])
        self.BoxNumber = data.get('BoxNumber', [])
        self.SubjectDescription = data.get('SubjectDescription', [])
        super(FacetedCardAdvancedSearchForm, self).__init__(*args, **kwargs)
        

    def search(self):
        sqs = super(FacetedCardAdvancedSearchForm, self).search()
        if self.data['boxnumb']:
        	sqs = sqs.filter(BoxNumber = self.data['boxnumb'])
        if self.data['year']:
        	sqs = sqs.filter(Year = self.data['year'])
        if self.BoxNumber:
            query = None
            for BoxNumber in self.BoxNumber:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(BoxNumber)
            sqs = sqs.narrow(u'BoxNumber_exact:%s' % query)
        if self.SubjectName:
            query = None
            for SubjectName in self.SubjectName:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(SubjectName)
            sqs = sqs.narrow(u'SubjectName_exact:%s' % query)
        if self.SubjectDescription:
            query = None
            for SubjectDescription in self.SubjectDescription:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(SubjectDescription)
            sqs = sqs.narrow(u'SubjectDescription_exact:%s' % query)
        return sqs

class SearchForm(forms.Form):

    q = forms.CharField(label='Keywords')