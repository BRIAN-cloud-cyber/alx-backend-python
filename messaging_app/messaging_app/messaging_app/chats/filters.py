import django_filters
from.models import message

class MessageFilter(django_filters.Filter):
    # filter message sent after/before certain dates 

    start_date= django_filters.DateTimeFilter(field_name="time stamp",lookup_expr='gte')
    end_date=django_filters.DateTimeFilter(field_name="time stamp",lookup_expr='lte')

    class Meta:
        models=message
        fields=['sender','receiver','start_date','end_date']