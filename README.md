# Django DataTables Tags

This repository provides Django template tags for use with jQuery DataTables.

* `data_tables_assets`: loads the JavaScript and CSS assets for jQuery DataTables.
    * `buttons` (optional boolean, default True): include assets for the buttons plugin, for export functions.
* `data_table`: takes a Django queryset or list of dictionaries and creates a jQuery DataTable.
    * `data_struct` (required queryset or list of dicts): the data to include in the DataTable.
    * `buttons` (optional boolean, default True): include the buttons bar above the datatable.
    * `column_names` (optional string, default None): a comma delimited list of column header names to use instead of the keys from the first row of the queryset or dict.

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

        context["my_groups"] = [
            {"name": "Baseball Fans", "member_count": 20, "leader": "Russ N."},
            {"name": "Hockey Fans", "member_count": 47, "leader": "Tim A."},
            {"name": "Football Fans", "member_count": 42, "leader": "Bob Z."}
        ]

        return context
```

** If you are using a queryset, you MUST use the `values()` parameter to explicitly list which fields you wish to include. **

Then, use the template tags to render the data table in your template with the queryset from the context (`my_app/my_template.html`):

```HTML+Django
{% import data_tables %}
<html>
<head>
    {% data_tables_assets %}
</head>
<body>
    {% data_table users %}
    {% data_table my_groups %}
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
