from django.shortcuts import render
from .models import MenuItem, MenuDisplayPage
from django.core.exceptions import MultipleObjectsReturned

def view_all_menus(request):
    parent_menus = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'all_menus.html', {'parent_menus': parent_menus})



def view_menu_by_url(request, menu_url):
    try:
        menu_item = MenuItem.objects.get(url=menu_url)
        children = menu_item.children.all()
        return render(request, 'menu_detail.html', {'menu_item': menu_item, 'children': children})
    except MenuItem.DoesNotExist:
        # Обработка случая, когда объект не найден
        return render(request, 'errors/404.html', status=404)
    except MultipleObjectsReturned:
        # Обработка ситуации, когда найдено больше одного объекта
        return render(request, 'errors/500.html', {'error_message': 'Найдено более одного объекта с указанным URL.'}, status=500)
    

def get_menu_items_for_page(request_url):
    try:
        display_page = MenuDisplayPage.objects.get(url=request_url)
        menu_items = MenuItem.objects.filter(display_on_pages=display_page)
        return menu_items
    except MenuDisplayPage.DoesNotExist:
        return MenuItem.objects.none()

def templ_tag_1_view(request):
    menu_items = get_menu_items_for_page(request.path)
    return render(request, 'test_template_tag_1.html', {'menu_items': menu_items})

def templ_tag_2_view(request):
    menu_items = get_menu_items_for_page(request.path)
    return render(request, 'test_template_tag_1.html', {'menu_items': menu_items})


