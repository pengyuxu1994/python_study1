import win32com.client

speaker=win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Speak("我是凤姐，我爱死了申领瑞")
speaker.Speak("i am luoyufeng,i love shenlingrui")
speaker.Speak("我是凤姐，我爱死了申领瑞")