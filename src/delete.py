import os
import datetime

def delete_old_recorded_videos(directory, max_age_hours=48):
    current_time = datetime.datetime.now()

    for filename in os.listdir(directory):
        if filename.startswith("recorded_video_") and filename.endswith(".avi"):
            file_path = os.path.join(directory, filename)

            # Get the file creation time
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

            # Calculate the age of the file in hours
            age_hours = (current_time - creation_time).total_seconds() / 3600

            # Delete the file if it's older than the specified threshold
            if age_hours > max_age_hours:
                os.remove(file_path)
                print(f"Deleted {filename}, which is {age_hours:.2f} hours old.")

if __name__ == "__main__":
    # Specify the directory where recorded videos are stored
    video_directory = "/mnt/media"

    # Specify the maximum age for videos in hours
    max_age_hours = 48

    # Run the deletion function
    delete_old_recorded_videos(video_directory, max_age_hours)