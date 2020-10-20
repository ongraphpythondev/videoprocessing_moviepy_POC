
# django modules
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# project modules
from VideoProcessing.settings import BASE_DIR

# python modules
import json
import os

# moviepy modules
from moviepy.editor import (
                VideoFileClip,AudioFileClip,
                CompositeVideoClip, concatenate_videoclips,
                vfx, clips_array, ImageClip
                )

@csrf_exempt
def add_replace_audio(request):
    files = request.FILES
    video = files['video']
    audio = files['audio']
    with VideoFileClip(video.temporary_file_path()) as vdo, AudioFileClip(audio.temporary_file_path()) as aud:
        vdo.set_audio(aud).write_videofile('media/res.mp4')  # overwrite audio of the video file
    return JsonResponse({'video':f'http://127.0.0.1:8000/media/res.mp4'})

@csrf_exempt
def join_videos(request):
    files = request.FILES
    video = files.getlist('video')
    v1 = video[0]
    v2 = video[1]
    with VideoFileClip(v1.temporary_file_path()) as vdo1, VideoFileClip(v1.temporary_file_path()) as vdo2:
        concatenate_videoclips([vdo1,vdo2]).write_videofile('media/res.mp4') # join 2 video
    return JsonResponse({'video':f'http://127.0.0.1:8000/media/res.mp4'})

@csrf_exempt
def flipx_video(request):
    files = request.FILES
    video = files['video']
    with VideoFileClip(video.temporary_file_path()) as vdo:
        vdo.fx(vfx.mirror_x).write_videofile('media/res.mp4') # filp video on the x axis 
    return JsonResponse({'video':f'http://127.0.0.1:8000/media/res.mp4'})


@csrf_exempt
def flipy_video(request):
    files = request.FILES
    video = files['video']
    with VideoFileClip(video.temporary_file_path()) as vdo:
        vdo.fx(vfx.mirror_y).write_videofile('media/res.mp4') # filp video on the y axis
    return JsonResponse({'video':f'http://127.0.0.1:8000/media/res.mp4'})


@csrf_exempt
def lower_quality(request):
    files = request.FILES
    video = files['video']
    with VideoFileClip(video.temporary_file_path()) as vdo:
        vdo.resize(0.60).write_videofile('media/res.mp4') # reduse the size of video to 60 % of orignal video
    return JsonResponse({'video':f'http://127.0.0.1:8000/media/res.mp4'})

@csrf_exempt
def extract_audio(request):
    files = request.FILES
    video = files['video']
    with VideoFileClip(video.temporary_file_path()) as vdo:
        audio = vdo.audio     # extracts audio of the video vdo
        audio.write_audiofile('media/res.mp3')
    return JsonResponse({'audio':"http://127.0.0.1:8000/media/res.mp3"})


@csrf_exempt
def _clips_array(request):
    files = request.FILES
    tr = files.get('top_right')
    tl = files.get('top_left')
    br = files.get('bottom_right')
    bl = files.get('bottom_left')

    with (VideoFileClip(tr.temporary_file_path() if tr else DEFAULT_MEDIA_ROOT+'/color.mp4') as tr, VideoFileClip(tl.temporary_file_path() if tl else DEFAULT_MEDIA_ROOT+'/color.mp4') as tl,  
          VideoFileClip(br.temporary_file_path() if br else DEFAULT_MEDIA_ROOT+'/color.mp4') as br, VideoFileClip(bl.temporary_file_path() if bl else DEFAULT_MEDIA_ROOT+'/color.mp4') as bl ): 
        vd = clips_array([[tr,tl],[br,bl]]) # play 4 video parallel in a grid
        vd.write_videofile('media/res.mp4')

    return JsonResponse({'video':'http://127.0.0.1:8000/media/res.mp4'})


@csrf_exempt
def water_mark(request):
    files = request.FILES
    vdo = VideoFileClip(files.get('vdo').temporary_file_path())
    logo = ImageClip(files.get('logo').temporary_file_path())


    wm = (logo.set_duration(vdo.duration)
          .resize(height=50) # if you need to resize...
          .margin(right=8, bottom=8, opacity=0) # (optional) logo-border padding
          .set_pos(("right","bottom"))) 

    CompositeVideoClip([vdo, wm]).write_videofile('media/res.mp4')
    return JsonResponse({'video':'http://127.0.0.1:8000/media/res.mp4'})
    