from instagrapi import Client

# Foydalanuvchining ma'lumotlari
username = ''
password = ''

# Hikoya ma'lumotlari
story_image_path = 'qr-data.png'
story_caption = 'Example story'

# Client obyekti yaratish
client = Client()

# Foydalanuvchi bilan kirish
client.login(username, password)

# Hikoyaga rasm yuklash
print(client.photo_upload_to_story(path=story_image_path, caption=story_caption))
# Rasm yuklash
client.photo_upload(path=story_image_path, caption=story_caption)
