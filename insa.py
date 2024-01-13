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
            loader.download_post(post, target=save_folder)

        print(f"All media downloaded successfully to '{save_folder}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'target_username' with the username of the public Instagram account
    target_username = 'rebellious_editz'
    
    # Specify the folder to save the media
    save_folder = 'E:/instagram_links/all_media'

    download_instagram_media(target_username, save_folder)