from celery_tasks.sms.yuntongxun.sms import CCP
from celery_tasks.main import celery_app


# 只有用此装饰器装饰过的函数才是celery的任务
@celery_app.task(name='send_sms_code')
def send_sms_code(mobile, sms_code):

    CCP().send_template_sms(mobile, [sms_code, 5], 1)



# send_sms_code.delay(mobile, sms_cdoe)