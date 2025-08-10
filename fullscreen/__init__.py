from IPython.display import HTML

def full_screen(video_id, video_hash):
    """
    Return an HTML object for a Vimeo fullscreen link in Jupyter notebooks.
    """
    return HTML(f'''
    Click the link below to watch in fullscreen:<br><br>
    <a href="https://player.vimeo.com/video/{video_id}?h={video_hash}" target="_blank" style="font-size: 18px;">
    🎬 Open Video in Fullscreen
    </a>
    ''')
