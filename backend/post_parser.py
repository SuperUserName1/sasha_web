import requests
from bs4 import BeautifulSoup

def get_last_post(web_link):
    # Извлекаем username из ссылки
    username = web_link.split("@")[-1].split("/")[0]  # 'akyur0'
    url = f"https://t.me/s/{username}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все посты и берем последний
    posts = soup.find_all('div', class_='tgme_widget_message')
    if not posts:
        return "Канал не найден или приватный"
    last_post = posts[-1]
    
    # Текст поста
    text = last_post.find('div', class_='tgme_widget_message_text')
    text_content = text.text.strip() if text else "Текст отсутствует"
    
    # Медиа (фото/видео)
    media_content = []
    if last_post.find('a', class_='tgme_widget_message_photo'):
        photo_style = last_post.find('a', class_='tgme_widget_message_photo')['style']
        photo_url = photo_style.split("url('")[1].split("')")[0]
        media_content.append(f'<img src="{photo_url}" style="max-width: 300px;">')
    
    if last_post.find('video'):
        video_url = last_post.find('video')['src']
        media_content.append(f'<video controls><source src="{video_url}" type="video/mp4"></video>')
    
    return {'text': text_content, 'media': media_content}

# Пример использования
web_link = "https://web.telegram.org/k/#@akyur0"
last_post = get_last_post(web_link)
print(last_post)