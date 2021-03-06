from string import capwords

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def data_tables_assets(buttons=True):
    """
    Dumps the assets for jQuery Data Tables.This will allow us to upgrade in a single
    spot.

    Usage: {% data_tables_assets %}
    """

    dt_assets = """
        <link rel="stylesheet" href="https://cdn.datatables.net/{dt_version}/css/jquery.dataTables.min.css">
        <script src="https://cdn.datatables.net/{dt_version}/js/jquery.dataTables.min.js"></script>
        <script src="https://cdn.datatables.net/{dt_version}/js/dataTables.bootstrap4.min.js"></script>
    """.format(
        dt_version="1.10.20",
    )

    button_assets = ""

    if buttons:
        button_assets = """
            <link rel="stylesheet" href="https://cdn.datatables.net/buttons/{buttons_version}/css/buttons.dataTables.min.css">
            <script src="https://cdn.datatables.net/buttons/{buttons_version}/js/dataTables.buttons.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/{jszip_version}/jszip.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/{pdfmake_version}/pdfmake.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/{pdfmake_version}/vfs_fonts.js"></script>
            <script src="https://cdn.datatables.net/buttons/{buttons_version}/js/buttons.html5.min.js"></script>
            <script src="https://cdn.datatables.net/buttons/{buttons_version}/js/buttons.print.min.js "></script>
        """.format(
            buttons_version="1.6.1", jszip_version="3.1.3", pdfmake_version="0.1.53",
        )

    return mark_safe(dt_assets.strip() + button_assets.strip())


@register.inclusion_tag("data_tables_tags/data_table.html")
def data_table(data_struct, column_names=None, buttons=True, options=None):
    """
    Dynamically create a data table from a passed data structure.

    The data structure can be a list of dicts or a Django queryset using `values()`.

    Usage: {% data_table my_data_struct "Email,IP Address,Issued,Expiration" %}
    """
    if column_names:
        columns = [column.strip() for column in column_names.split(",")]
    else:
        columns = []

    for row in data_struct:
        if not columns:
            for column in row.keys():
                columns.append(capwords(column.replace("_", " ")))
            break

    return {
        "buttons": buttons,
        "columns": columns,
        "column_count": len(columns),
        "options": options,
        "rows": data_struct,
    }
