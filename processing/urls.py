from django.urls import path
from processing.views import (
        add_replace_audio, join_videos,
        flipx_video,flipy_video,
        extract_audio,_clips_array,
        water_mark
                    )
                    
urlpatterns = [
    path('replace_audio/', add_replace_audio),
    path('join_videos/', join_videos),
    path('flipx_video/', flipx_video),
    path('flipy_video/', flipy_video),
    path('extract_audio/', extract_audio),
    path('clips_array/', _clips_array),
    path('water_mark/', water_mark),
]