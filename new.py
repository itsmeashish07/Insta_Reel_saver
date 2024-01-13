import instaloader
import os

def clean_filename(filename):
    # Remove characters that are not allowed in filenames
    return ''.join(char for char in filename if char.isalnum() or char in (' ', '_', '-', '.'))

def download_instagram_media(profile_username, save_folder):
    # Create an Instaloader object
    loader = instaloader.Instaloader()

    try:
        # Get profile information for the given username
        profile = instaloader.Profile.from_username(loader.context, profile_username)

        # Create a folder to store the media
        os.makedirs(save_folder, exist_ok=True)

        # Download and save all types of media
        for index, post in enumerate(profile.get_posts()):
            print(f"Downloading Media {index + 1}...")

            # Get the caption and use it in the filename
            caption = clean_filename(post.caption)
            
            # If the caption is empty, use a default filename
            filename = f"{index + 1}_{caption}" if caption else f"{index + 1}_NoCaption"

            # Save the media file with the caption-based filename
            file_path = os.path.join(save_folder, f"{filename}.mp4")
            loader.download_post(post, target=file_path)

        print(f"All media downloaded successfully to '{save_folder}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'target_username' with the username of the public Instagram account
    target_username = 'floby.edit'
    
    # Specify the folder to save the media
     new_save_folder = r'anime'

    download_instagram_media(target_username, new_save_folder)