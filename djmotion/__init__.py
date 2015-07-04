# widget monkeypatch for bootstrap 
from django.forms.widgets import Input

def initInput(self, attrs=None):
    self.attrs = {'class':'form-control'}
    if attrs is not None:
        a = attrs.copy()
        self.attrs.update(a)

Input.__init__ = initInput
