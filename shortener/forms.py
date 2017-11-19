from django import forms

from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
	
	url = forms.CharField(
            label='', 
            validators=[validate_url],
            widget = forms.TextInput(
                    attrs ={
                        "placeholder": "Paste URL to shorten it!",
                        "class": "form-control"
                        }
                )
            )
'''
	url= forms.CharField(label='Submit Url')


	def clean(self):
		cleaned_data= super(SubmitUrlForm, self).clean()
		url=cleaned_data.get('url')
		url_validator=URLValidator()
		try:
			url_validator(url)
		except:
			raise forms.ValidationError("invalid URL")
		return url
'''
  
	#def clean_url(sef):
		#url=self.cleaned_data['url']
		#print(url)
		#url_validator=URLValidator()
		#try:
		#	url_validator(url)
		#except:
		#	raise forms.ValidationError("invalid URL")
		#return url