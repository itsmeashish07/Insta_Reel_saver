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

        # Download and save only mp4 files
        for index, post in enumerate(profile.get_posts()):
            if post.url.endswith('.mp4'):
                print(f"Downloading Media {index + 1}...")
                
                # Save the media file without timestamp and extension
                file_name = f"{index + 1}.mp4"
                file_path = os.path.join(save_folder, file_name)
                loader.download_post(post, target=file_path)

        print(f"All mp4 media downloaded successfully to '{save_folder}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'target_username' with the username of the public Instagram account
    target_username = 'rebellious_editz'
    
    # Specify the folder to save the media
    save_folder = 'E:/instagram_links/mp4_media'

    download_instagram_media(target_username, save_folder)



    code not  working
    