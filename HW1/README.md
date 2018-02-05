# API Homework

This is the API homework for EC500. This project grabs images from tweet and generate a video containing the images using FFMpeg API and also a json file that uses Google Vision API to recongize products in the images.

### How to use
1. Download tweetDownload.py and vision.py from this folder
2. Install [Tweepy](https://github.com/tweepy/tweepy)
3. Install FFMpeg using
```
brew ffmpeg
```
4. Install Wget using
```
pip wget
```
5. Get your credentials and access token from your twitter account by following steps [here](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/)
6. Put your token information into tweetDownload.py
7. Get your Google Vision API Credentials following steps [here](https://cloud.google.com/vision/docs/auth)
8. Run in your command line 
```
py tweetDownload.py
ffmpeg -y -loop 1 -i %00d.JPG -c:a libfdk_aac -ar 44100 -ac 2 -vf "scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)', pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 output.mp4
py vision.py
```
9. DONE! Check for output.mp4 as the video of the images and labels.json as the decription of your images


Thank you! For any questions, feel free to email me at glxlily@bu.edu
