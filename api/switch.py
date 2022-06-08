from jnius import autoclass, cast
import os

def set_wallpaper(home_path, lock_path):
    PythonActivity = autoclass('org.kivy.android.PythonActivity')

    try:
        EnvClass = autoclass("android.os.Environment")
        path_to_env = EnvClass.getExternalStorageDirectory().toString()
    
        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        context = cast('android.content.Context', currentActivity.getApplicationContext())
    
        FileClass = autoclass('java.io.File')
        if home_path != "":
            hfile = FileClass(os.path.join(path_to_env, home_path))
        if lock_path != "":
            lfile = FileClass(os.path.join(path_to_env, lock_path))

        BitmapFactory = autoclass('android.graphics.BitmapFactory')
        if home_path != "":
            hbitmap = BitmapFactory.decodeFile(hfile.getAbsolutePath())
        if home_path != "":
            lbitmap = BitmapFactory.decodeFile(lfile.getAbsolutePath())

        WallpaperManager = autoclass('android.app.WallpaperManager')
        manager = WallpaperManager.getInstance(context)

        if home_path != "":
            manager.setBitmap(hbitmap, None, False)
        if home_path != "":
            manager.setBitmap(lbitmap, None, False, manager.FLAG_LOCK)
          
    except Exception as e:
        print(e)
