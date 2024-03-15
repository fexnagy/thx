from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.label_suffix = " *"


class ViewRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ViewRoomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["readonly"] = True
            field.widget.attrs["disabled"] = True
