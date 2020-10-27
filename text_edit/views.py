from django.views.generic.edit import FormView
from . import forms


class Index(FormView):
    form_class = forms.TextForm
    #  form_class = forms.PostForm pythonが自動で生成したフォーム
    template_name = "index.html"

    def form_valid(self, form):
        data = form.cleaned_data
        text = data["text"]
        search = data["search"]
        replace = data["replace"]

        new_text = text.replace(search, replace)

        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_respone(ctxt)