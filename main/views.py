import json

from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from main.models import AutoMark, AutoPartCategory, AutoPart
from orders.models import Order, OrderAutoPart


class IndexView(View):
    def get(self, request):
        return render(request, 'main/index.html')


class ServicesView(View):
    def get(self, request):
        return render(request, 'main/service.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class MarketView(View):

    @staticmethod
    def get_selected_marks(request: HttpRequest):
        marks_ids = []
        for key, name in request.GET.items():
            if key.startswith('mark_'):
                marks_ids.append(
                    int(key.replace('mark_', ''))
                )
        return marks_ids

    @staticmethod
    def get_selected_categories(request: HttpRequest):
        category_ids = []
        for key, name in request.GET.items():
            if key.startswith('auto_part_category_'):
                category_ids.append(
                    int(key.replace('auto_part_category_', ''))
                )
        return category_ids

    def get(self, request):
        auto_parts = AutoPart.objects
        selected_marks = self.get_selected_marks(request)
        selected_categories = self.get_selected_categories(request)

        if len(selected_marks):
            auto_parts = auto_parts.filter(auto_mark_id__in=selected_marks)

        if len(selected_categories):
            auto_parts = auto_parts.filter(auto_part_category_id__in=selected_categories)

        auto_parts = auto_parts.all()

        context = {
            'auto_marks': AutoMark.objects.all(),
            'auto_part_categories': AutoPartCategory.objects.all(),
            'selected_marks': selected_marks,
            'selected_categories': selected_categories,
            'auto_parts': auto_parts
        }
        return render(request, 'main/market.html', context)


class OrderView(View):
    def get(self, request):
        auto_parts = AutoPart.objects.all()
        return render(request, 'main/order.html', context={
            'auto_parts': auto_parts
        })

    def post(self, request):
        print(request.POST)
        new_order = Order(
            name=request.POST.get('name'),
            service=request.POST.get('service'),
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),
            comment=request.POST.get('name'),
        )
        new_order.save()

        selected_auto_parts = {}
        try:
            selected_auto_parts = json.loads(request.POST.get('selected_auto_parts'))
        except Exception as ex:
            print("ex")

        for key, val in selected_auto_parts.items():
            if val > 0:
                ap = AutoPart.objects.get(id=key)
                if ap:
                    new_order_auto_part = OrderAutoPart(
                        order=new_order,
                        auto_part=ap,
                        quantity=val
                    )
                    new_order_auto_part.save()

        auto_parts = AutoPart.objects.all()
        return render(request, 'main/order.html', context={
            'show_thanks': True,
            'do_clear_localStorage': True,
            'auto_parts': auto_parts
        })


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html')
