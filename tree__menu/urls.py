from django.urls import path
from .views import view_all_menus, view_menu_by_url, templ_tag_1_view , templ_tag_2_view

urlpatterns = [
    path('', view_all_menus, name='all_menus'),
    path('menu/<path:menu_url>/', view_menu_by_url, name='menu_by_url'),
    # Тестовые URL-адреса
    path('test-page/', templ_tag_1_view, name='test_page'),
    path('another-test-page/', templ_tag_2_view, name='another_test_page'),
]
