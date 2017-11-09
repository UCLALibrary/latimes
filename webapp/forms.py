from haystack.forms import FacetedSearchForm
from django import forms

class FacetedCardSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.Year = data.get('Year', [])
        self.BoxNumber = data.get('BoxNumber', [])
        self.SubjectName = data.get('SubjectName', [])
        self.SubjectDescription = data.get('SubjectDescription', [])
        self.Photographer = data.get('Photographer', [])
        self.Location = data.get('Location', [])
        self.date = data.get('date', [])
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
            sqs = sqs.narrow(u'BoxNumber:%s' % query)
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
        if self.Year:
            query = None
            for Year in self.Year:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Year)
            sqs = sqs.narrow(u'Year_exact:%s' % query)
        if self.Photographer:
            query = None
            for Photographer in self.Photographer:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Photographer)
            sqs = sqs.narrow(u'Photographer_exact:%s' % query)
        if self.Location:
            query = None
            for Location in self.Location:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Location)
            sqs = sqs.narrow(u'Location_exact:%s' % query)
            
        return sqs

class FacetedCardAdvancedSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.SubjectName = data.get('SubjectName', [])
        self.Negative = data.get('Negative', [])
        self.SubjectDescription = data.get('SubjectDescription', [])
        self.Photographer = data.get('Photographer', [])
        self.Location = data.get('Location', [])
        self.Year = data.get('Year', [])
        self.BoxNumber = data.get('BoxNumber', [])
        super(FacetedCardAdvancedSearchForm, self).__init__(*args, **kwargs)
        

    def search(self):
        sqs = super(FacetedCardAdvancedSearchForm, self).search()
        if self.data['boxnumb']:
        	sqs = sqs.filter(BoxNumber = self.data['boxnumb'])
        if self.data['year']:
        	sqs = sqs.filter(Year = self.data['year'])
        if self.Negative:
            query = None
            for Negative in self.Negative:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Negative)
            sqs = sqs.narrow(u'Negative_exact:%s' % query)
            print(sqs.count())
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
        if self.Photographer:
            query = None
            for Photographer in self.Photographer:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Photographer)
            sqs = sqs.narrow(u'Photographer_exact:%s' % query)
        if self.Location:
            query = None
            for Location in self.Location:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Location)
            sqs = sqs.narrow(u'Location_exact:%s' % query)
        if self.Year:
            query = None
            for Year in self.Year:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(Year)
        if self.BoxNumber:
            query = None
            for BoxNumber in self.BoxNumber:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(BoxNumber)
            sqs = sqs.narrow(u'BoxNumber:%s' % query)
        return sqs

class SearchForm(forms.Form):

    q = forms.CharField(label='Keywords')