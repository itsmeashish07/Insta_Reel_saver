import instaloader
import os

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
            
            # Get the file extension
            extension = post.url[-4:]  # Assuming that the extension is 3 characters long

            # Save the media file without timestamp and extension
            file_name = f"{index + 1}{extension}"
            file_path = os.path.join(save_folder, file_name)
            loader.download_post(post, target=file_path)

        print(f"All media downloaded successfully to '{save_folder}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'target_username' with the username of the public Instagram account
    target_username = 'rebellious_editz'
    
    # Specify the folder to save the media
    new_save_folder = r'anime'

    download_instagram_media(target_username,new_save_folder)
