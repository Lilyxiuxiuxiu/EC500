# API Homework #1

This is the API homework for EC500. This project grabs images from twitter and generates a video containing the images using FFMpeg API and also a json file that uses Google Vision API to recongize products in the images.

### How to use
1. Download HW1API.py
2. Install [Tweepy](https://github.com/tweepy/tweepy)
3. Install FFMpeg using HomeBrew
```
brew ffmpeg
```
4. Install Wget using Pip install
```
pip install wget
```
5. Get your credentials and access token from your twitter account by following steps [here](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/)
6. Put your token information into HW1API.py
7. Get your Google Vision API Credentials following steps [here](https://cloud.google.com/vision/docs/auth)
8. Run in your command line 
```
python2 HW1API.py
```
9. DONE! Check for outputvid.mp4 as the video of the images and labels.json as the decription of your images

Note: This API is developed on macOS10.13.3. If you are using Windows OS, comment line 75 in HW1API.py and uncomment line 74.

--- 
Worked with Ayako Shimuzu on this mini project
#### Thank you! For any questions, feel free to email me at glxlily@bu.edu
