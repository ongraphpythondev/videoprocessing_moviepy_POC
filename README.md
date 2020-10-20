# videoprocessing_moviepy_POC

<br><h1>Prerequisites:</h1><br><br>
You will need the following programmes properly installed on your computer.<br>
Python 3.7+ <br>
django 2.2+ <br>
Virtual Environment
To install virtual environment on your system use:

pip install virtualenv <br>

or<br>

pip3 install virtualenv #if using linux(for python 3 and above) <br>

<br><h1>Installation and Running :</h1><br><br>
git clone https://github.com/ongraphpythondev/LoggingPOC.git <br>
cd LoggingPOC<br>

virtualenv venv or virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows or source venv/bin/activate # for linux

<br><h1>install required packages for the project to run</h1>
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

<h1>Test Url at local system</h1>
http://127.0.0.1:8000/vdo/


<h1>Testing apis :</h1>

1) replaceing audio of a video file:

    curl --location --request POST "http://127.0.0.1:8000/vdo/replace_audio/" \
    --form "video=@/path/to/file" \
    --form "audio=@/path/to/file"


2) join 2 videos:

    curl --location --request POST "http://127.0.0.1:8000/vdo/join_videos/" \
    --form "video=@/path/to/file" \
    --form "video=@/path/to/file"


3) flip video on x axis:

    curl --location --request POST "http://127.0.0.1:8000/vdo/flipx_video/" \
    --form "video=@/path/to/file"


4) flip video on y axis:

    curl --location --request POST "http://127.0.0.1:8000/vdo/flipy_video/" \
    --form "video=@/path/to/file"


5) reduce video quality:

    curl --location --request POST "http://127.0.0.1:8000/vdo/lower_quality/" \
    --form "video=@/path/to/file"


6) extract audio from video :

    curl --location --request POST "http://127.0.0.1:8000/vdo/extract_audio/" \
    --form "video=@/path/to/file"


6) join upto 4 videos so that the play in parallel :

    curl --location --request POST "http://127.0.0.1:8000/vdo/clips_array/" \
    --form "top_right=@/path/to/file" \
    --form "top_left=@/path/to/file" \
    --form "bottom_right=@/path/to/file" \
    --form "bottom_left=@/path/to/file"

7) add a watermark to a video :

    curl --location --request POST "http://127.0.0.1:8000/vdo/water_mark/" \
    --form "vdo=@/path/to/file" \
    --form "logo=@/path/to/file"

