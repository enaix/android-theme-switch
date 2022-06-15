from jnius import autoclass as ac
from jnius import cast
import os

def set_wallpaper(path, is_home):
    PythonActivity = ac('org.kivy.android.PythonActivity')

    try:
        EnvClass = ac("android.os.Environment")
        path_to_env = EnvClass.getExternalStorageDirectory().toString()
    
        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        context = cast('android.content.Context', currentActivity.getApplicationContext())
    
        FileClass = ac('java.io.File')
        file = FileClass(os.path.join(path_to_env, path))

        BitmapFactory = ac('android.graphics.BitmapFactory')
        bitmap = BitmapFactory.decodeFile(file.getAbsolutePath())

        WallpaperManager = ac('android.app.WallpaperManager')
        manager = WallpaperManager.getInstance(context)

        if is_home:
            manager.setBitmap(bitmap, None, False)
        else:
            manager.setBitmap(bitmap, None, False, manager.FLAG_LOCK)
          
    except Exception as e:
        print(e)
