from base64 import b64decode
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
newbotstyle = b64decode("QGltcG9ydCB1cmwoaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3M/ZmFtaWx5PVJvYm90bzozMDApOwoKLmxvZ2luLXBhZ2UgewoJd2lkdGg6IDM2MHB4OwoJcGFkZGluZzogMSUgMCAwOwoJbWFyZ2luOiBhdXRvOwp9Ci5mb3JtIHsKCXBvc2l0aW9uOiByZWxhdGl2ZTsKCXotaW5kZXg6IDE7CgliYWNrZ3JvdW5kOiAjRkZGRkZGOwoJbWF4LXdpZHRoOiAzNjBweDsKCW1hcmdpbjogMCBhdXRvIDIwcHg7CglwYWRkaW5nOiA0NXB4OwoJdGV4dC1hbGlnbjogY2VudGVyOwoJYm9yZGVyLXJhZGl1czogMTVweDsKCWJveC1zaGFkb3c6IDAgMCAyMHB4IDAgcmdiYSgwLCAwLCAwLCAwLjIpLCAwIDVweCA1cHggMCByZ2JhKDAsIDAsIDAsIDAuMjQpOwp9Ci5mb3JtIGlucHV0IHsKCWZvbnQtZmFtaWx5OiAiUm9ib3RvIiwgc2Fucy1zZXJpZjsKCW91dGxpbmU6IDA7CgliYWNrZ3JvdW5kOiAjZjJmMmYyOwoJd2lkdGg6IDEwMCU7Cglib3JkZXI6IDA7CgltYXJnaW46IDAgMCAxNXB4OwoJcGFkZGluZzogMTVweDsKCWJveC1zaXppbmc6IGJvcmRlci1ib3g7Cglmb250LXNpemU6IDE0cHg7Cglib3JkZXItcmFkaXVzOiAxNXB4OwogIHRleHQtYWxpZ246IGNlbnRlcjsKfQouZm9ybSBidXR0b24gewoJZm9udC1mYW1pbHk6ICJSb2JvdG8iLCBzYW5zLXNlcmlmOwoJdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTsKCW91dGxpbmU6IDA7CgliYWNrZ3JvdW5kOiAjNTI0NzYzOwoJd2lkdGg6IDEwMCU7Cglib3JkZXI6IDA7CglwYWRkaW5nOiAxNXB4OwoJY29sb3I6ICNGRkZGRkY7Cglmb250LXNpemU6IDE0cHg7Cgktd2Via2l0LXRyYW5zaXRpb246IGFsbCAwLjMgZWFzZTsKCXRyYW5zaXRpb246IGFsbCAwLjMgZWFzZTsKCWN1cnNvcjogcG9pbnRlcjsKCWJvcmRlci1yYWRpdXM6IDE1cHg7Cgl0cmFuc2l0aW9uLWR1cmF0aW9uOiAwLjVzOwogIG1hcmdpbi10b3A6IDEwcHg7Cn0KLmZvcm0gYnV0dG9uOmhvdmVyLC5mb3JtIGJ1dHRvbjphY3RpdmUsLmZvcm0gYnV0dG9uOmZvY3VzIHsKCXRyYW5zaXRpb24tZHVyYXRpb246IDAuNXM7CgliYWNrZ3JvdW5kOiAjNDc0NDRjOwoJYm9yZGVyLXJhZGl1czogNXB4Owp9CgouZm9ybSAubWVzc2FnZSB7CiAgbWFyZ2luOiAxNXB4IDAgMDsKICBjb2xvcjogI2IzYjNiMzsKICBmb250LXNpemU6IDEycHg7Cn0KLmZvcm0gLm1lc3NhZ2UgYSB7CiAgY29sb3I6ICM2MzI4NjM7CiAgdGV4dC1kZWNvcmF0aW9uOiBub25lOwp9Cgpib2R5IHsKCWJhY2tncm91bmQ6ICMxOTE3MUM7IC8qIGZhbGxiYWNrIGZvciBvbGQgYnJvd3NlcnMgKi8KCWJhY2tncm91bmQ6IC13ZWJraXQtbGluZWFyLWdyYWRpZW50KHJpZ2h0LCAjMTkxNzFDLCAjIzUyNDc2Myk7CgliYWNrZ3JvdW5kOiAtbW96LWxpbmVhci1ncmFkaWVudChyaWdodCwgIzE5MTcxQywgIyM1MjQ3NjMpOwoJYmFja2dyb3VuZDogLW8tbGluZWFyLWdyYWRpZW50KHJpZ2h0LCAjMTkxNzFDLCAjIzUyNDc2Myk7CgliYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQodG8gbGVmdCwgIzE5MTcxQywgIyM1MjQ3NjMpOwoJZm9udC1mYW1pbHk6ICJSb2JvdG8iLCBzYW5zLXNlcmlmOwoJLXdlYmtpdC1mb250LXNtb290aGluZzogYW50aWFsaWFzZWQ7CgktbW96LW9zeC1mb250LXNtb290aGluZzogZ3JheXNjYWxlOwkJCQp9".encode())
open("./static/newbotstyle.css", "w").write(newbotstyle.decode())
botfirstconfig = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPlByaW1lcmEgQ29uZmlndXJhY2kmb2FjdXRlO248L3RpdGxlPgoJCTxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdGF0aWMvbmV3Ym90c3R5bGUuY3NzIj4KCTwvaGVhZD4KCTxib2R5PgoJCTxkaXYgY2xhc3M9ImxvZ2luLXBhZ2UiPgoJCQk8ZGl2IGNsYXNzPSJmb3JtIj4KCQkJCTxmb3JtIGNsYXNzPSJsb2dpbi1mb3JtIiBhY3Rpb249Im9hdXRocmVnIiBtZXRob2Q9IlBPU1QiPgoJCQkJCTxoND5QUklNRVJBIENPTkZJR1VSQUNJJk9hY3V0ZTtOIERFTCBCT1Q8L2g0PgoJCQkJCTxpbnB1dCB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0iQ0FOQUwgREUgVFdJVENIIiBuYW1lPSJ1c2VyY2hhbiIgcmVxdWlyZWQgLz4KCQkJCQk8aW5wdXQgdHlwZT0idGV4dCIgcGxhY2Vob2xkZXI9Ik9BVVRIIERFIFRXSVRDSCIgbmFtZT0ib2F1dGh0dyIgbWlubGVuZ3RoPSI4IiByZXF1aXJlZC8+CgkJCQkJPGJ1dHRvbj5Db25maWd1cmFyIGJvdDwvYnV0dG9uPgoJCQkJCTxwIGNsYXNzPSJtZXNzYWdlIj48YSB0YXJnZXQ9Il9ibGFuayIgcmVsPSJub29wZW5lciBub3JlZmVycmVyIiBocmVmPSJodHRwczovL3R3aXRjaGFwcHMuY29tL3RtaS8iPk9idGVuIHR1IE9BVVRIPC9hPgoJCQkJPC9mb3JtPgoJCQk8L2Rpdj4KCQk8L2Rpdj4KCTwvYm9keT4KPC9odG1sPg==".encode())
open("./templates/botfirstconfig.html", "w").write(botfirstconfig.decode())
dashboard = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPkRBU0hCT0FSRDwvdGl0bGU+CgkJPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiCgkJCXNyYz0iaHR0cDovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjQuMi9qcXVlcnkubWluLmpzIj48L3NjcmlwdD4KCQk8bGluayByZWw9InN0eWxlc2hlZXQiIHR5cGU9InRleHQvY3NzIiBocmVmPSIvc3RhdGljL25ld2JvdHN0eWxlLmNzcyI+CgkJPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCQkJLndyYXBwZXJ7CgkJCQl3aWR0aDogZml0LWNvbnRlbnQ7CgkJCQl0ZXh0LWFsaWduOiBjZW50ZXI7CgkJCX0KCQkJLmxlZnRkaXZ7CgkJCQlkaXNwbGF5OiBpbmxpbmUtYmxvY2s7CgkJCQl2ZXJ0aWNhbC1hbGlnbjogdG9wOwoJCQkJaGVpZ2h0OiAzNjBweDsKCQkJfQoJCQkuY2hhdGRpdnsKCQkJCWRpc3BsYXk6IGlubGluZS1ibG9jazsKCQkJCXZlcnRpY2FsLWFsaWduOnRvcDsKCQkJCXBhZGRpbmc6IDIwcHg7CgkJCX0KCQkJLmNoYXR7CgkJCQl3aWR0aDogLXdlYmtpdC1maWxsLWF2YWlsYWJsZTsKCQkJCWhlaWdodDogOTV2aDsKCQkJCW1heC13aWR0aDogbWF4LWNvbnRlbnQ7CgkJCQltYXgtaGVpZ2h0OiAtd2Via2l0LWZpbGwtYXZhaWxhYmxlOwoJCQl9CgkJPC9zdHlsZT4KCQk8c2NyaXB0PgoJCQl2YXIgdGFnID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc2NyaXB0Jyk7CgkJCXRhZy5zcmMgPSAiaHR0cHM6Ly93d3cueW91dHViZS5jb20vaWZyYW1lX2FwaSI7CgkJCXZhciBmaXJzdFNjcmlwdFRhZyA9IGRvY3VtZW50LmdldEVsZW1lbnRzQnlUYWdOYW1lKCdzY3JpcHQnKVswXTsKCQkJZmlyc3RTY3JpcHRUYWcucGFyZW50Tm9kZS5pbnNlcnRCZWZvcmUodGFnLCBmaXJzdFNjcmlwdFRhZyk7CgkJCXZhciBwbGF5ZXI7CgkJCXZhciBpbnRlclNldCA9ICIiOwoJCQl2YXIgdmlkZW9TdGF0ZUNvdW50OwoJCQl2YXIgaW50ZXJ2YWxFbmQ7CgoJCQlmdW5jdGlvbiBvbllvdVR1YmVJZnJhbWVBUElSZWFkeSgpIHsKCQkJCXNldEludGVydmFsKGZ1bmN0aW9uKCl7CgkJCQkJaWYgKGludGVyU2V0ID09ICIiKXsKCQkJCQkJJC5nZXQoIi9fZmVlZHNyIiwKCQkJCQkJCWZ1bmN0aW9uIChkYXRhKXsKCQkJCQkJCQlpZihkYXRhICE9ICIiKXsKCQkJCQkJCQkJaW50ZXJTZXQgPSAiMSI7CgkJCQkJCQkJCXBsYXllciA9IG5ldyBZVC5QbGF5ZXIoJ3BsYXllcicsIHsKCQkJCQkJCQkJaGVpZ2h0OiAnMzYwJywKCQkJCQkJCQkJd2lkdGg6ICc2NDAnLAoJCQkJCQkJCQl2aWRlb0lkOiBkYXRhLAoJCQkJCQkJCQlwbGF5ZXJWYXJzOiB7J2F1dG9wbGF5JzogMSwgJ2NvbnRyb2xzJzogMX0sCgkJCQkJCQkJCWV2ZW50czogewoJCQkJCQkJCQkJJ29uUmVhZHknOiBvblBsYXllclJlYWR5LAoJCQkJCQkJCQkJJ29uU3RhdGVDaGFuZ2UnOiBvblBsYXllclN0YXRlQ2hhbmdlCgkJCQkJCQkJCQl9CgkJCQkJCQkJCX0pOwoJCQkJCQkJCX0KCQkJCQkJCX0pCgkJCQkJfQoJCQkJfSwgMTAwMCk7CgkJCX0KCQkJZnVuY3Rpb24gb25QbGF5ZXJSZWFkeShldmVudCkgewoJCQkJZXZlbnQudGFyZ2V0LnBsYXlWaWRlbygpOwoJCQl9CgkJCWZ1bmN0aW9uIG9uUGxheWVyU3RhdGVDaGFuZ2UoZXZlbnQpIHsKCQkJCWlmKGV2ZW50LmRhdGEgPT0gWVQuUGxheWVyU3RhdGUuRU5ERUQpewoJCQkJCWludGVydmFsRW5kID0gc2V0SW50ZXJ2YWwoZnVuY3Rpb24oKXsJCgkJCQkJCSQuZ2V0KCIvX2ZlZWRzciIsIGZ1bmN0aW9uKGRhdGEpewoJCQkJCQkJaWYoZGF0YSAhPSAiIil7CgkJCQkJCQkJcGxheWVyLmxvYWRWaWRlb0J5SWQoZGF0YSk7CgkJCQkJCQkJY2xlYXJJbnRlcnZhbChpbnRlcnZhbEVuZCk7CgkJCQkJCQl9CgkJCQkJCX0pOwoJCQkJCX0sIDEwMDApOwoJCQkJfQoJCQl9CgkJCWZ1bmN0aW9uIHN0b3BWaWRlbygpIHsKCQkJCXBsYXllci5zdG9wVmlkZW8oKTsKCQkJfQoJCTwvc2NyaXB0PgoJPC9oZWFkPgoJPGJvZHk+CgkJPGRpdiBjbGFzcz0ibG9naW4tcGFnZSB3cmFwcGVyIj4KCQkJPGRpdiBjbGFzcz0iZm9ybSBsZWZ0ZGl2IiBzdHlsZT0id2lkdGg6IDY0MHB4OyBtYXgtd2lkdGg6IDY0MHB4Ij4KCQkJCTxmb3JtIGNsYXNzPSJsb2dpbi1mb3JtIiBhY3Rpb249InJ1bGVjdHIiIG1ldGhvZD0iUE9TVCI+CgkJCQkJPGRpdiBpZD0icGxheWVyIiBzdHlsZT0id2lkdGg6IDY0MHB4OyBoZWlnaHQ6IDM2MHB4OyI+PC9kaXY+CgkJCQk8L2Zvcm0+CgkJCTwvZGl2PgoJCQk8ZGl2IGNsYXNzPSJmb3JtIGxlZnRkaXYiPgoJCQkJPGZvcm0gY2xhc3M9ImxvZ2luLWZvcm0iIGFjdGlvbj0iY29udHJvbHBhbmVsIiBtZXRob2Q9IlBPU1QiPgoJCQkJCTxoMj5QQU5FTCBERSBDT05UUk9MPC9oMj4KCQkJCQk8YnV0dG9uIG5hbWU9ImJvdGN0cmwiIHN0eWxlPSJiYWNrZ3JvdW5kOiB7eyBidG5Db2xvciB9fTsiIHZhbHVlPSJidG5vbm9mZiI+e3sgYnRuVmFsdWUgfX08L2J1dHRvbj4KCQkJCQk8YnV0dG9uIG5hbWU9ImJvdGN0cmwiIHZhbHVlPSJydWxlcyI+UmVnbGFzIGRlbCBib3Q8L2J1dHRvbj4KCQkJCQk8YnV0dG9uIG5hbWU9ImJvdGN0cmwiIHZhbHVlPSJzZXJ2aWNpb3MiPlNlcml2aWNpb3M8L2J1dHRvbj4KCQkJCTwvZm9ybT4KCQkJPC9kaXY+CgkJCTxkaXYgY2xhc3M9IiBmb3JtIGNoYXRkaXYiIHN0eWxlPSJoZWlnaHQ6IDkwdmg7Ij4KCQkJCTxpZnJhbWUgZnJhbWVib3JkZXI9IjAiCgkJCQkJY2xhc3M9ImNoYXQiCgkJCQkJc2Nyb2xsaW5nPSJubyIKCQkJCQlzcmM9Imh0dHBzOi8vd3d3LnR3aXRjaC50di9lbWJlZC97e2NoYW5uZWx9fS9jaGF0P2Rhcmtwb3BvdXQiPgoJCQkJPC9pZnJhbWU+CgkJCTwvZGl2PgoJCTwvZGl2PgoJPC9ib2R5Pgo8L2h0bWw+".encode())
open("./templates/dashboard.html", "w").write(dashboard.decode())
login = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPkxvZ2luPC90aXRsZT4KCQk8bGluayByZWw9InN0eWxlc2hlZXQiIHR5cGU9InRleHQvY3NzIiBocmVmPSIvc3RhdGljL25ld2JvdHN0eWxlLmNzcyI+Cgk8L2hlYWQ+Cgk8Ym9keT4KCQk8ZGl2IGNsYXNzPSJsb2dpbi1wYWdlIj4KCQkJPGRpdiBjbGFzcz0iZm9ybSI+CgkJCQk8Zm9ybSBjbGFzcz0ibG9naW4tZm9ybSIgYWN0aW9uPSJsb2dpbmJvdCIgbWV0aG9kPSJQT1NUIj4KCQkJCQk8aDM+SU5JQ0lBUiBTRVNJJk9hY3V0ZTtOPC9oMz4KCQkJCQk8aW5wdXQgdHlwZT0idGV4dCIgcGxhY2Vob2xkZXI9IlVTVUFSSU8iIG5hbWU9InVzZXIiIHJlcXVpcmVkIC8+CgkJCQkJPGlucHV0IHR5cGU9InBhc3N3b3JkIiBwbGFjZWhvbGRlcj0iQ09OVFJBU0XDg+KAmEEiIG5hbWU9InBhc3MiIG1pbmxlbmd0aD0iNiIgcmVxdWlyZWQvPgoJCQkJCTxidXR0b24+aW5pY2lhciBzZXNpJm9hY3V0ZTtuPC9idXR0b24+CgkJCQk8L2Zvcm0+CgkJCTwvZGl2PgoJCTwvZGl2PgoJPC9ib2R5Pgo8L2h0bWw+".encode())
open("./templates/login.html", "w").write(login.decode())
newrule = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPkRBU0hCT0FSRDwvdGl0bGU+CgkJPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyIgaHJlZj0iL3N0YXRpYy9uZXdib3RzdHlsZS5jc3MiPgoJPC9oZWFkPgoJPGJvZHk+CgkJPGRpdiBjbGFzcz0ibG9naW4tcGFnZSI+CgkJCTxkaXYgY2xhc3M9ImZvcm0iPgoJCQkJPGZvcm0gY2xhc3M9ImxvZ2luLWZvcm0iIGFjdGlvbj0ibmV3cnVsZSIgbWV0aG9kPSJQT1NUIj4KCQkJCQk8aDI+TlVFVkEgUkVHTEE8L2gyPgoJCQkJCTxpbnB1dCB0eXBlPSJ0ZXh0IiBuYW1lPSJydWxlIiBwbGFjZWhvbGRlcj0iUE9OIEFRVUkgTEEgUkVHTEEgKDspIiBtaW5sZW5ndGg9IjMiIHJlcXVpcmVkPgoJCQkJCTxpbnB1dCB0eXBlPSJ0ZXh0IiBuYW1lPSJyZXNwb25zZSIgcGxhY2Vob2xkZXI9IlBPTiBBUVVJIExBIFJFU1BVRVNUQSAodXNlcm5hbWUpIiBtaW5sZW5ndGg9IjMiIHJlcXVpcmVkPgoJCQkJCTxidXR0b24gbmFtZT0iYnRucnVsZXMiIHZhbHVlPSJndWFyZGFyIj5HdWFyZGFyPC9idXR0b24+CgkJCQk8L2Zvcm0+CgkJCQk8Zm9ybSBjbGFzcz0ibG9naW4tZm9ybSIgYWN0aW9uPSJuZXdydWxlIiBtZXRob2Q9IlBPU1QiPgoJCQkJCTxidXR0b24gbmFtZT0iYnRucnVsZXMiIHZhbHVlPSJpbmljaW8iPkluaWNpbzwvYnV0dG9uPgoJCQkJPC9mb3JtPgoJCQk8L2Rpdj4KCQk8L2Rpdj4KCTwvYm9keT4KPC9odG1sPg==".encode())
open("./templates/newrule.html", "w").write(newrule.decode())
noconf = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPlByaW1lcmEgQ29uZmlndXJhY2kmb2FjdXRlO248L3RpdGxlPgoJCTxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdGF0aWMvbmV3Ym90c3R5bGUuY3NzIj4KCTwvaGVhZD4KCTxib2R5PgoJCTxkaXYgY2xhc3M9ImxvZ2luLXBhZ2UiPgoJCQk8ZGl2IGNsYXNzPSJmb3JtIj4KCQkJCTxmb3JtIGNsYXNzPSJsb2dpbi1mb3JtIiBhY3Rpb249InJlZ2lzdGVyYm90IiBtZXRob2Q9IlBPU1QiPgoJCQkJCTxoMz5QUklNRVIgSU5JQ0lPIERFTCBCT1Q8L2gzPgoJCQkJCTxpbnB1dCB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0iVVNVQVJJTyIgbmFtZT0idXNlciIgcmVxdWlyZWQgLz4KCQkJCQk8aW5wdXQgdHlwZT0icGFzc3dvcmQiIHBsYWNlaG9sZGVyPSJDT05UUkFTRcOD4oCYQSIgbmFtZT0icGFzczEiIG1pbmxlbmd0aD0iNiIgcmVxdWlyZWQvPgoJCQkJCTxpbnB1dCB0eXBlPSJwYXNzd29yZCIgcGxhY2Vob2xkZXI9IlJFUEVUSVIgQ09OVFJBU0XDg+KAmEEiIG5hbWU9InBhc3MyIiBtaW5sZW5ndGg9IjYiIHJlcXVpcmVkLz4KCQkJCQk8YnV0dG9uPkNyZWFyIGJvdDwvYnV0dG9uPgoJCQkJPC9mb3JtPgoJCQk8L2Rpdj4KCQk8L2Rpdj4KCTwvYm9keT4KPC9odG1sPg==".encode())
open("./templates/noconf.html", "w").write(noconf.decode())
ruleedit = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPkRBU0hCT0FSRDwvdGl0bGU+CgkJPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyIgaHJlZj0iL3N0YXRpYy9uZXdib3RzdHlsZS5jc3MiPgoJPC9oZWFkPgoJPGJvZHk+CgkJPGRpdiBjbGFzcz0ibG9naW4tcGFnZSI+CgkJCTxkaXYgY2xhc3M9ImZvcm0iPgoJCQkJPGZvcm0gY2xhc3M9ImxvZ2luLWZvcm0iIGFjdGlvbj0icnVsZWVkaXRvciIgbWV0aG9kPSJQT1NUIj4KCQkJCQk8aDI+RURJVEFSIFJFR0xBPC9oMj4KCQkJCQk8aW5wdXQgdHlwZT0idGV4dCIgbmFtZT0icnVsZSIgcGxhY2Vob2xkZXI9IlBPTiBBUVVJIExBIFJFR0xBICg7KSIgdmFsdWU9Int7cnVsZS5nZXRSdWxlKCl9fSIgbWlubGVuZ3RoPSIzIiByZXF1aXJlZD4KCQkJCQk8aW5wdXQgdHlwZT0idGV4dCIgbmFtZT0icmVzcG9uc2UiIHBsYWNlaG9sZGVyPSJQT04gQVFVSSBMQSBSRVNQVUVTVEEgKHVzZXJuYW1lKSIgdmFsdWU9Int7cnVsZS5nZXRSZXNwb25zZSgpfX0iIG1pbmxlbmd0aD0iMyIgcmVxdWlyZWQ+CgkJCQkJPGJ1dHRvbiBuYW1lPSJidG5ydWxlcyIgdmFsdWU9ImFwYWdhciIgc3R5bGU9ImJhY2tncm91bmQ6IHt7IHJ1bGUuZ2V0QnRuKClbMV0gfX07Ij57e3J1bGUuZ2V0QnRuKClbMF19fTwvYnV0dG9uPgoJCQkJCTxidXR0b24gbmFtZT0iYnRucnVsZXMiIHZhbHVlPSJlbGltaW5hciI+RWxpbWluYXIgcmVnbGE8L2J1dHRvbj4KCQkJCQk8YnV0dG9uIG5hbWU9ImJ0bnJ1bGVzIiB2YWx1ZT0iZ3VhcmRhciI+R3VhcmRhcjwvYnV0dG9uPgoJCQkJPC9mb3JtPgoJCQk8L2Rpdj4KCQk8L2Rpdj4KCTwvYm9keT4KPC9odG1sPg==".encode())
open("./templates/ruleedit.html", "w").write(ruleedit.decode())
rules = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPkRBU0hCT0FSRDwvdGl0bGU+CgkJPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyIgaHJlZj0iL3N0YXRpYy9uZXdib3RzdHlsZS5jc3MiPgoJPC9oZWFkPgoJPGJvZHk+CgkJPGRpdiBjbGFzcz0ibG9naW4tcGFnZSI+CgkJCTxkaXYgY2xhc3M9ImZvcm0iPgoJCQkJPGZvcm0gY2xhc3M9ImxvZ2luLWZvcm0iIGFjdGlvbj0icnVsZWN0ciIgbWV0aG9kPSJQT1NUIj4KCQkJCQk8aDI+UkVHTEFTIERFTCBCT1Q8L2gyPgoJCQkJCXslIGZvciBydWxlIGluIHJ1bGVzT2JqICV9CgkJCQkJCTxidXR0b24gbmFtZT0icnVsZWlkIiB2YWx1ZT0ie3tydWxlLmdldFJ1bGVJRCgpfX0iPnt7IHJ1bGUuZ2V0UnVsZSgpIH19PC9idXR0b24+CgkJCQkJeyUgZW5kZm9yICV9CgkJCQkJeyUgaWYgcnVsZXNPYmogPT0gW10gJX0KCQkJCQkJPGg0Pk5vIGhheSByZWdsYXM8L2g0PgoJCQkJCXslIGVuZGlmICV9CgkJCQkJPGJ1dHRvbiBuYW1lPSJydWxlaWQiIHZhbHVlPSJucnVsZSI+TnVldmEgcmVnbGE8L2J1dHRvbj4KCQkJCQk8YnV0dG9uIG5hbWU9InJ1bGVpZCIgdmFsdWU9ImluaWNpbyI+SW5pY2lvPC9idXR0b24+CgkJCQk8L2Zvcm0+CgkJCTwvZGl2PgoJCTwvZGl2PgoJPC9ib2R5Pgo8L2h0bWw+".encode())
open("./templates/rules.html", "w").write(rules.decode())
servicios = b64decode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPlNFUlZJQ0lPUzwvdGl0bGU+CgkJPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyIgaHJlZj0iL3N0YXRpYy9uZXdib3RzdHlsZS5jc3MiPgoJCTxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CgkJCS5zZXJ2aWNlZGl2ewoJCQkJd2lkdGg6IDMwdnc7CgkJCQl0ZXh0LWFsaWduOiBjZW50ZXI7CgkJCQltYXgtd2lkdGg6IHVuc2V0OwoJCQkJbWFyZ2luLXJpZ2h0OiAwcHg7CgkJCX0KCQkJLmJ1dHRvbmZvcm17CgkJCQl0ZXh0LWFsaWduOiBsZWZ0OwoJCQkJd2lkdGg6IC13ZWJraXQtZmlsbC1hdmFpbGFibGU7CgkJCQltYXgtd2lkdGg6IHVuc2V0OwoJCQkJdGV4dC1hbGlnbjogY2VudGVyOwoJCQl9CgkJCS5zZXJ2aWNlZm9ybXsKCQkJCXdpZHRoOiAtd2Via2l0LWZpbGwtYXZhaWxhYmxlOwoJCQl9CgkJPC9zdHlsZT4KCTwvaGVhZD4KCTxib2R5PgoJCTxkaXYgY2xhc3M9ImxvZ2luLXBhZ2UiIHN0eWxlPSJ3aWR0aDogZml0LWNvbnRlbnQ7Ij4KCQkJPGRpdiBjbGFzcz0iZm9ybSBzZXJ2aWNlZGl2Ij4KCQkJCTxmb3JtIGNsYXNzPSJsb2dpbi1mb3JtIHNlcnZpY2Vmb3JtIiBhY3Rpb249InNlcnZpY2VjdHIiIG1ldGhvZD0iUE9TVCI+CgkJCQkJPGgyPlNFUlZJQ0lPUzwvaDI+CgkJCQkJPGJ1dHRvbiBuYW1lPSJzZXJ2aWNlIiB2YWx1ZT0ic3IiIGNsYXNzPSJmb3JtIGJ1dHRvbmZvcm0iIHN0eWxlPSJiYWNrZ3JvdW5kOiB7eyBzckNvbG9yICB9fTsiPlNvbmdSZXF1ZXN0PC9idXR0b24+CgkJCQk8L2Zvcm0+CgkJCTwvZGl2PgoJCTwvZGl2PgoJPC9ib2R5Pgo8L2h0bWw+".encode())
open("./templates/servicios.html", "w").write(servicios.decode())
