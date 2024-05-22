from instagrapi import Client

# Foydalanuvchining ma'lumotlari
username = ''
password = ''

# Post ma'lumotlari
post_image_path = 'qr-data.png'
post_caption = 'Example'

# Client obyekti yaratish
client = Client()

# Foydalanuvchi bilan kirish
client.login(username, password)

# Post joylash
client.photo_upload(path=post_image_path, caption=post_caption)
