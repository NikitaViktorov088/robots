from django.http import JsonResponse
from django.views import View
from robots.forms import RobotForm


class RobotView(View):

    @staticmethod
    def post(request, *args, **kwargs):
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok', 'message': 'Робот добавлен!'})
        return JsonResponse({'status': 'error'})
