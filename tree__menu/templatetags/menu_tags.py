from django import template
from django.template.loader import render_to_string
from tree__menu.models import MenuItem, MenuDisplayPage  # Исправьте your_app_name на имя вашего приложения

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    # Пытаемся найти меню, которое должно быть показано на текущей странице
    current_url = request.path
    menu_to_display = MenuItem.objects.filter(name=menu_name, parent__isnull=True, display_on_pages__url=current_url).first()

    if menu_to_display:
        children = menu_to_display.children.all()
        return render_to_string('menu_template.html', {'menu_item': menu_to_display, 'children': children})
    return ''