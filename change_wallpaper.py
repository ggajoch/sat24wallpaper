import ctypes


def change_wallpaper(path):
    import os
    import ctypes
    from ctypes import wintypes

    # drive = "c:\\"
    # folder = "test"
    # image = "midi turmes.png"
    # image_path = os.path.join(drive, folder, image)

    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002

    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint
    SystemParametersInfo.restype = wintypes.BOOL
    print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0,
          path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))


if __name__ == '__main__':
    change_wallpaper(r'D:\sat24wallpaper\now.jpg')
