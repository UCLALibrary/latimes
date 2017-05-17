from haystack.forms import FacetedSearchForm
from django import forms

class FacetedProductSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.SubjectName = data.get('SubjectName', [])
        self.SubjectDescription = data.get('SubjectDescription', [])
        super(FacetedProductSearchForm, self).__init__(*args, **kwargs)

    def search(self):
        sqs = super(FacetedProductSearchForm, self).search()
        if self.SubjectDescription:
            query = None
            for SubjectDescription in self.SubjectDescription:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(SubjectDescription)
            sqs = sqs.narrow(u'category_exact:%s' % query)
        if self.SubjectName:
            query = None
            for SubjectName in self.SubjectName:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(SubjectName)
            sqs = sqs.narrow(u'brand_exact:%s' % query)
        return sqs
