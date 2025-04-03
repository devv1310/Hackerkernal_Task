from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
import openpyxl
from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowRecordForm


class AuthorListView(ListView):
    model = Author
    template_name = 'list_author.html'
    context_object_name = 'author'
    paginate_by = 10

class BookListView(ListView):
    model = Book
    template_name = 'list_book.html'
    context_object_name = 'book'
    paginate_by = 10

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'list_borrow.html'
    context_object_name = 'borrow_records'
    paginate_by = 10


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'
    success_url = reverse_lazy('list_author')

    def form_valid(self, form):
        messages.success(self.request, "Author added successfully!")
        return super().form_valid(form)

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('list_book')

    def form_valid(self, form):
        messages.success(self.request, "Book added successfully!")
        return super().form_valid(form)

class BorrowRecordCreateView(CreateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'add_borrow_record.html'
    success_url = reverse_lazy('list_borrow')

    def form_valid(self, form):
        messages.success(self.request, "Borrow record added successfully!")
        return super().form_valid(form)


class ExportExcelView(TemplateView):
    def get(self, request, *args, **kwargs):
        wb = openpyxl.Workbook()
        data = {
            "Authors": (["ID", "Name", "Email", "Bio"], Author.objects.values_list("id", "name", "email", "bio")),
            "Books": (["ID", "Title", "Genre", "Published Date", "Author"], 
                      Book.objects.values_list("id", "title", "genre", "public_date", "author__name")),
            "Borrow Records": (["ID", "User Name", "Book", "Borrow Date", "Return Date"], 
                               BorrowRecord.objects.values_list("id", "user_name", "book__title", "borrow_date", "return_date")),
        }

        for sheet_name, (headers, records) in data.items():
            ws = wb.create_sheet(title=sheet_name) if sheet_name != "Authors" else wb.active
            ws.title = sheet_name
            ws.append(headers)
            for record in records:
                ws.append(record)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=library_data.xlsx'
        wb.save(response)
        return response