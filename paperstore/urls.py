from django.urls import path
from .views import *

urlpatterns = [
    path('author/', AuthorListView.as_view(), name='list_author'),
    path('book/', BookListView.as_view(), name='list_book'),
    path('borrow/', BorrowRecordListView.as_view(), name='list_borrow'),
    path('add-author/', AuthorCreateView.as_view(), name='add_author'),
    path('add-book/', BookCreateView.as_view(), name='add_book'),
    path('add-borrow/', BorrowRecordCreateView.as_view(), name='add_borrow'),
    path('exportexcel/', ExportExcelView.as_view(), name='exportexcel'),
]