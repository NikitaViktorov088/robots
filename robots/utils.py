import pandas as pd
from datetime import datetime, timedelta
from django.db.models import Count
from robots.models import Robot


def generate_report_robots():
    week_ago = datetime.now() - timedelta(days=7)
    robots = Robot.objects.filter(created__gte=week_ago).values('model', 'version').annotate(count=Count('id'))

    models = set([item['model'] for item in robots])

    with pd.ExcelWriter('robots.xlsx', engine='openpyxl') as writer:
        for model in models:
            model_data = [data for data in robots if data['model'] == model]
            df = pd.DataFrame(model_data)
            df_pivot = df.pivot_table(index='version', values='count', aggfunc='sum')
            df_pivot.reset_index(inplace=True)
            df_pivot.columns = ['Версия', 'Количество за неделю']
            df_pivot.to_excel(writer, sheet_name=model, index=False)
    return 'robot.xlsx'
