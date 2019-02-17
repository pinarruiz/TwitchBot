import base64
from os import makedirs, remove
folders = ['./static', './templates', '.']
for folder in folders:
	if folder != ".":
		try:
			remove(folder)
		except:
			pass
		try:
			makedirs(folder)
		except:
			pass
newbotstyle = base64.b64decode("QGltcG9ydCB1cmwoaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3M/ZmFtaWx5PVJvYm90bzozMDApOwoKLmxvZ2luLXBhZ2UgewoJd2lkdGg6IDM2MHB4OwoJcGFkZGluZzogOCUgMCAwOwoJbWFyZ2luOiBhdXRvOwp9Ci5mb3JtIHsKCXBvc2l0aW9uOiByZWxhdGl2ZTsKCXotaW5kZXg6IDE7CgliYWNrZ3JvdW5kOiAjRkZGRkZGOwoJbWF4LXdpZHRoOiAzNjBweDsKCW1hcmdpbjogMCBhdXRvIDEwMHB4OwoJcGFkZGluZzogNDVweDsKCXRleHQtYWxpZ246IGNlbnRlcjsKCWJvcmRlci1yYWRpdXM6IDE1cHg7Cglib3gtc2hhZG93OiAwIDAgMjBweCAwIHJnYmEoMCwgMCwgMCwgMC4yKSwgMCA1cHggNXB4IDAgcmdiYSgwLCAwLCAwLCAwLjI0KTsKfQouZm9ybSBpbnB1dCB7Cglmb250LWZhbWlseTogIlJvYm90byIsIHNhbnMtc2VyaWY7CglvdXRsaW5lOiAwOwoJYmFja2dyb3VuZDogI2YyZjJmMjsKCXdpZHRoOiAxMDAlOwoJYm9yZGVyOiAwOwoJbWFyZ2luOiAwIDAgMTVweDsKCXBhZGRpbmc6IDE1cHg7Cglib3gtc2l6aW5nOiBib3JkZXItYm94OwoJZm9udC1zaXplOiAxNHB4OwoJYm9yZGVyLXJhZGl1czogMTVweDsKICB0ZXh0LWFsaWduOiBjZW50ZXI7Cn0KLmZvcm0gYnV0dG9uIHsKCWZvbnQtZmFtaWx5OiAiUm9ib3RvIiwgc2Fucy1zZXJpZjsKCXRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CglvdXRsaW5lOiAwOwoJYmFja2dyb3VuZDogIzUyNDc2MzsKCXdpZHRoOiAxMDAlOwoJYm9yZGVyOiAwOwoJcGFkZGluZzogMTVweDsKCWNvbG9yOiAjRkZGRkZGOwoJZm9udC1zaXplOiAxNHB4OwoJLXdlYmtpdC10cmFuc2l0aW9uOiBhbGwgMC4zIGVhc2U7Cgl0cmFuc2l0aW9uOiBhbGwgMC4zIGVhc2U7CgljdXJzb3I6IHBvaW50ZXI7Cglib3JkZXItcmFkaXVzOiAxNXB4OwoJdHJhbnNpdGlvbi1kdXJhdGlvbjogMC41czsKfQouZm9ybSBidXR0b246aG92ZXIsLmZvcm0gYnV0dG9uOmFjdGl2ZSwuZm9ybSBidXR0b246Zm9jdXMgewoJdHJhbnNpdGlvbi1kdXJhdGlvbjogMC41czsKCWJhY2tncm91bmQ6ICM0NzQ0NGM7Cglib3JkZXItcmFkaXVzOiA1cHg7Cn0KCi5mb3JtIC5tZXNzYWdlIHsKICBtYXJnaW46IDE1cHggMCAwOwogIGNvbG9yOiAjYjNiM2IzOwogIGZvbnQtc2l6ZTogMTJweDsKfQouZm9ybSAubWVzc2FnZSBhIHsKICBjb2xvcjogIzRDQUY1MDsKICB0ZXh0LWRlY29yYXRpb246IG5vbmU7Cn0KCmJvZHkgewoJYmFja2dyb3VuZDogIzE5MTcxQzsgLyogZmFsbGJhY2sgZm9yIG9sZCBicm93c2VycyAqLwoJYmFja2dyb3VuZDogLXdlYmtpdC1saW5lYXItZ3JhZGllbnQocmlnaHQsICMxOTE3MUMsICMjNTI0NzYzKTsKCWJhY2tncm91bmQ6IC1tb3otbGluZWFyLWdyYWRpZW50KHJpZ2h0LCAjMTkxNzFDLCAjIzUyNDc2Myk7CgliYWNrZ3JvdW5kOiAtby1saW5lYXItZ3JhZGllbnQocmlnaHQsICMxOTE3MUMsICMjNTI0NzYzKTsKCWJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCh0byBsZWZ0LCAjMTkxNzFDLCAjIzUyNDc2Myk7Cglmb250LWZhbWlseTogIlJvYm90byIsIHNhbnMtc2VyaWY7Cgktd2Via2l0LWZvbnQtc21vb3RoaW5nOiBhbnRpYWxpYXNlZDsKCS1tb3otb3N4LWZvbnQtc21vb3RoaW5nOiBncmF5c2NhbGU7CQkJCn0=".encode())
open("./static/newbotstyle.css", "w").write(newbotstyle.decode())
botfirstconfig = base64.b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPlByaW1lcmEgQ29uZmlndXJhY2kmb2FjdXRlO248L3RpdGxlPgoJCTxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdGF0aWMvbmV3Ym90c3R5bGUuY3NzIj4KCTwvaGVhZD4KCTxib2R5PgoJCTxkaXYgY2xhc3M9ImxvZ2luLXBhZ2UiPgoJCQk8ZGl2IGNsYXNzPSJmb3JtIj4KCQkJCTxmb3JtIGNsYXNzPSJsb2dpbi1mb3JtIiBhY3Rpb249Im9hdXRocmVnIiBtZXRob2Q9IlBPU1QiPgoJCQkJCTxoND5QUklNRVJBIENPTkZJR1VSQUNJJk9hY3V0ZTtOIERFTCBCT1Q8L2g0PgoJCQkJCTxpbnB1dCB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0iQ0FOQUwgREUgVFdJVENIIiBuYW1lPSJ1c2VyY2hhbiIgcmVxdWlyZWQgLz4KCQkJCQk8aW5wdXQgdHlwZT0idGV4dCIgcGxhY2Vob2xkZXI9Ik9BVVRIIERFIFRXSVRDSCIgbmFtZT0ib2F1dGh0dyIgbWlubGVuZ3RoPSI4IiByZXF1aXJlZC8+CgkJCQkJPGJ1dHRvbj5Db25maWd1cmFyIGJvdDwvYnV0dG9uPgoJCQkJCTxwIGNsYXNzPSJtZXNzYWdlIj48YSB0YXJnZXQ9Il9ibGFuayIgcmVsPSJub29wZW5lciBub3JlZmVycmVyIiBocmVmPSJodHRwczovL3R3aXRjaGFwcHMuY29tL3RtaS8iPk9idGVuIHR1IE9BVVRIPC9hPgoJCQkJPC9mb3JtPgoJCQk8L2Rpdj4KCQk8L2Rpdj4KCTwvYm9keT4KPC9odG1sPg==".encode())
open("./templates/botfirstconfig.html", "w").write(botfirstconfig.decode())
dashboard = base64.b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPkRBU0hCT0FSRDwvdGl0bGU+CgkJPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyIgaHJlZj0iL3N0YXRpYy9uZXdib3RzdHlsZS5jc3MiPgoJPC9oZWFkPgoJPGJvZHk+CgkJPGRpdiBjbGFzcz0ibG9naW4tcGFnZSI+CgkJCTxkaXYgY2xhc3M9ImZvcm0iPgoJCQkJPGZvcm0gY2xhc3M9ImxvZ2luLWZvcm0iIGFjdGlvbj0iY29udHJvbHBhbmVsIiBtZXRob2Q9IlBPU1QiPgoJCQkJCTxoMj5QQU5FTCBERSBDT05UUk9MPC9oMj4KCQkJCQk8YnV0dG9uIG5hbWU9ImJvdGN0cmwiIHN0eWxlPSJiYWNrZ3JvdW5kOiB7eyBidG5Db2xvciB9fTsiIHZhbHVlPSJidG5vbm9mZiI+e3sgYnRuVmFsdWUgfX08L2J1dHRvbj4KCQkJCTwvZm9ybT4KCQkJPC9kaXY+CgkJPC9kaXY+Cgk8L2JvZHk+CjwvaHRtbD4=".encode())
open("./templates/dashboard.html", "w").write(dashboard.decode())
login = base64.b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPkxvZ2luPC90aXRsZT4KCQk8bGluayByZWw9InN0eWxlc2hlZXQiIHR5cGU9InRleHQvY3NzIiBocmVmPSIvc3RhdGljL25ld2JvdHN0eWxlLmNzcyI+Cgk8L2hlYWQ+Cgk8Ym9keT4KCQk8ZGl2IGNsYXNzPSJsb2dpbi1wYWdlIj4KCQkJPGRpdiBjbGFzcz0iZm9ybSI+CgkJCQk8Zm9ybSBjbGFzcz0ibG9naW4tZm9ybSIgYWN0aW9uPSJsb2dpbmJvdCIgbWV0aG9kPSJQT1NUIj4KCQkJCQk8aDM+SU5JQ0lBUiBTRVNJJk9hY3V0ZTtOPC9oMz4KCQkJCQk8aW5wdXQgdHlwZT0idGV4dCIgcGxhY2Vob2xkZXI9IlVTVUFSSU8iIG5hbWU9InVzZXIiIHJlcXVpcmVkIC8+CgkJCQkJPGlucHV0IHR5cGU9InBhc3N3b3JkIiBwbGFjZWhvbGRlcj0iQ09OVFJBU0XDg+KAmEEiIG5hbWU9InBhc3MiIG1pbmxlbmd0aD0iNiIgcmVxdWlyZWQvPgoJCQkJCTxidXR0b24+aW5pY2lhciBzZXNpJm9hY3V0ZTtuPC9idXR0b24+CgkJCQk8L2Zvcm0+CgkJCTwvZGl2PgoJCTwvZGl2PgoJPC9ib2R5Pgo8L2h0bWw+".encode())
open("./templates/login.html", "w").write(login.decode())
noconf = base64.b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPlByaW1lcmEgQ29uZmlndXJhY2kmb2FjdXRlO248L3RpdGxlPgoJCTxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdGF0aWMvbmV3Ym90c3R5bGUuY3NzIj4KCTwvaGVhZD4KCTxib2R5PgoJCTxkaXYgY2xhc3M9ImxvZ2luLXBhZ2UiPgoJCQk8ZGl2IGNsYXNzPSJmb3JtIj4KCQkJCTxmb3JtIGNsYXNzPSJsb2dpbi1mb3JtIiBhY3Rpb249InJlZ2lzdGVyYm90IiBtZXRob2Q9IlBPU1QiPgoJCQkJCTxoMz5QUklNRVIgSU5JQ0lPIERFTCBCT1Q8L2gzPgoJCQkJCTxpbnB1dCB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0iVVNVQVJJTyIgbmFtZT0idXNlciIgcmVxdWlyZWQgLz4KCQkJCQk8aW5wdXQgdHlwZT0icGFzc3dvcmQiIHBsYWNlaG9sZGVyPSJDT05UUkFTRcOD4oCYQSIgbmFtZT0icGFzczEiIG1pbmxlbmd0aD0iNiIgcmVxdWlyZWQvPgoJCQkJCTxpbnB1dCB0eXBlPSJwYXNzd29yZCIgcGxhY2Vob2xkZXI9IlJFUEVUSVIgQ09OVFJBU0XDg+KAmEEiIG5hbWU9InBhc3MyIiBtaW5sZW5ndGg9IjYiIHJlcXVpcmVkLz4KCQkJCQk8YnV0dG9uPkNyZWFyIGJvdDwvYnV0dG9uPgoJCQkJPC9mb3JtPgoJCQk8L2Rpdj4KCQk8L2Rpdj4KCTwvYm9keT4KPC9odG1sPg==".encode())
open("./templates/noconf.html", "w").write(noconf.decode())
