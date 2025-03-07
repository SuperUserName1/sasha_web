fetch('http://localhost:5000/api/get_last_post')
.then(response => response.json())
.then(data => {
    const decodedText = unescape(JSON.parse(`"${data.text}"`));
    document.getElementById('post-text').textContent = decodedText;
    
    const mediaContainer = document.getElementById('post-media');
    mediaContainer.innerHTML = data.media.join('');
})
.catch(error => console.error('Ошибка:', error));