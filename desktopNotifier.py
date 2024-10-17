from plyer import notification
import time

if __name__=='__main__':
  while True:  
    notification.notify(
        title="**BOSE VIVEK ARYA PLEASE TAKE A REST",
        message="""Rest is vital for better mental health,
          increased
          concentration and memory, a healthier immune system, reduced stress, improved mood and even a better metabolism.""",
        # app_icon="C:/PYTHON/LEARNING/restv",
        timeout=5)
    time.sleep(60*60)
        