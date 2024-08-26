## Download

### HLS playlist `HTTP Live Streaming`

without header :

```shell
ffmpeg -i "playlist_URL.m3u8" -c copy output_video.mp4
```

with header :

```shell
ffmpeg -headers "User-Agent: Mozilla/5.0\r\nAuthorization: Bearer your_access_token\r\n" -i "playlist_URL.m3u8" -c copy output_video.mp4
```

###### https://stackoverflow.com/questions/33718810/ffmpeg-how-to-pass-http-headers

## Post download

### Subtitle

> [!TIP]
> Make sure the subtitle file is in the correct format and synchronised with the video.

#### Burning subtitles in video

If you want to burn subtitles into the video, i.e. make them permanently visible (rather than optional)

```shell
ffmpeg -i input_video.mp4 -vf subtitles=subtitles.srt output_video.mp4
```

#### add an optional subtitle file to the video

Example with a .srt file

```shell
ffmpeg -i input_video.mp4 -i subtitles.srt -c copy -c:s mov_text output_video.mp4
```

### video/audio combiner

Combine video and audio, keeping only the video of one and only the audio of the other.

```shell
ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 output.mp4
```

and keeping one video track and two audio tracks example with English and French audio tracks

```shell
ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a copy -map 0:v:0 -map 0:a:0 -map 1:a:0 \
-metadata:s:a:0 language=eng -metadata:s:a:0 title="English" \
-metadata:s:a:1 language=fra -metadata:s:a:1 title="French" \
output.mp4
```

### Renaming

> Renaming a file in a function of its type

run :

```bash
./rename.sh file_name.tmp
```
