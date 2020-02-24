# Django DataTables Tags

This repository provides Django template tags for use with jQuery DataTables.

## Installation

```bash
pip install git+https://github.com/wharton/django-data-tables-tags.git
```

We'd like to partner with an existing Django DataTables package rather than publish our own to PyPI.

## Usage Example

First, create a view with a queryset in the context.

```python
class MyView(TemplateView):
    template_name = "my_app/my_template.html"

    def get_context_data(self, **kwargs):
        context = self.get_context_data(**kwargs)

        context["users"] = User.objects.all().values(
            "username", "first_name", "last_name", "email", "date_joined",
        ).order_by("-date_joined",)

        return context
```

Then, use the template tags to render the data table in your template with the queryset from the context (`my_app/my_template.html`):

```HTML+Django
{% import data_tables %}
<html>
<head>
    {% data_tables_assets %}
</head>
<body>
    {% data_table users %}
</body>
</html>
```

You can also suppress the export buttons and pass a custom list of headers for the table:

```HTML+Django
{% import data_tables %}
<html>
<head>
    {% data_tables_assets buttons=False %}
</head>
<body>
    {% data_table users column_names="username, First, Last, Email, Joined" buttons=False %}
</body>
</html>
```
