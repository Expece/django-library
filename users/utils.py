

class DataMixin:
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context