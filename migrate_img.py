import os
import re
import shutil

# Directories
posts_root_dir = "D:/DataScience/StatsBlog/blogStats/static/post"  # Where the post folders are located
img_dir = "docs/blog/posts/img"  # Centralized directory for images
os.makedirs(img_dir, exist_ok=True)

# Regex pattern to match image links in Markdown files
image_pattern = re.compile(r"!\[.*?\]\((.*?\.(png|jpg|jpeg|gif|svg))\)")

# Traverse each post folder in posts_root_dir
for post_folder in os.listdir(posts_root_dir):
    post_path = os.path.join(posts_root_dir, post_folder)

    if os.path.isdir(post_path):  # Only process directories
        # Remove "_files" suffix for the Markdown filename
        post_folder_base = post_folder.removesuffix("_files")

        # Find all images in this folder and its subfolders
        for root, _, files in os.walk(post_path):
            for file_name in files:
                if file_name.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".gif", ".svg")
                ):
                    image_path = os.path.join(root, file_name)

                    # Copy the image to the centralized img directory
                    new_image_name = f"{post_folder_base}-{file_name}"  # Prefix with the base folder name
                    new_image_path = os.path.join(img_dir, new_image_name)
                    shutil.copy2(image_path, new_image_path)
                    print(f"Copied {image_path} to {new_image_path}")

        # Update the corresponding Markdown file in docs/blog/posts
        md_file_path = os.path.join("docs/blog/posts", f"{post_folder_base}.md")
        if os.path.exists(md_file_path):
            with open(md_file_path, "r", encoding="utf-8") as md_file:
                content = md_file.read()

            # Update the Markdown file to reference the new image paths
            def replace_image_path(match):
                original_path = match.group(1)
                image_name = os.path.basename(original_path)
                new_image_name = f"{post_folder_base}-{image_name}"  # Match the new naming convention
                return f"![Image](./img/{new_image_name})"

            updated_content = image_pattern.sub(replace_image_path, content)

            with open(md_file_path, "w", encoding="utf-8") as md_file:
                md_file.write(updated_content)
            print(f"Updated image links in {md_file_path}")
        else:
            print(f"Warning: Markdown file not found for {post_folder_base}")

print("All images copied and Markdown files updated.")
