from pytube import YouTube

def download_audio_from_youtube(url,file_name):
    try:
        # Create a YouTube object
        print(url)
        video = YouTube(url)
        

        # Get the audio stream
        audio_stream = video.streams.filter(only_audio=True).first()
        

         # Specify the file path with the desired file name and type
        file_path = f"{file_name}.{audio_stream.subtype}"

        # Download the audio stream
        audio_stream.download(filename=file_path)

        print("Audio downloaded successfully.")

    except Exception as e:
        print("Error: ", str(e))

# Provide the YouTube URL
youtube_url = input("Enter the YouTube URL: ")

fileName = input("Enter the FileName: ")

# Call the function to download audio
download_audio_from_youtube(youtube_url,fileName)
