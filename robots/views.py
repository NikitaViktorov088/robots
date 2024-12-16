from django.http import JsonResponse, HttpResponse
from django.views import View
from robots.forms import RobotForm
from robots.utils import generate_report_robots


class RobotView(View):

    @staticmethod
    def post(request, *args, **kwargs):
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok', 'message': 'Робот добавлен!'})
        return JsonResponse({'status': 'error'})

class DownloadReportView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        file_path = generate_report_robots()
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="robot.xlsx"'
            return response
