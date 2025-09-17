import requests
import os
from urllib.parse import urlparse
import uuid



def fetch_image():
    #Asks user for the url
    print("Welcome to the Image Fetcher! Or Finder, whichever you prefer." )
    url = input("Enter the image's url:").strip()

# Creates a folder/directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        # Extract filename from URL, or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename or "." not in filename:  # If no proper filename, generate one
            filename = f"image_{uuid.uuid4().hex}.jpg"

        #Saves the image in binary mode    
        file_path = os.path.join("Fetched_Images", filename)

        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"✅ Image saved successfully as: {file_path}")

    # Error handling for various exceptions
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection or the URL.")
    except requests.exceptions.Timeout:
        print("❌ The request timed out. Try again later.")
    except Exception as err:
        print(f"❌ An unexpected error occurred: {err}")


if __name__ == "__main__":
    fetch_image()