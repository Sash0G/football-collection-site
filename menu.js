function importContent() {
    fetch('menu.html')
        .then(response => {if (!response.ok) {
            throw new Error('Failed to fetch source.html');
        }
        return response.text();})
        .then(html => {
            document.getElementById('menuPlaceholder').innerHTML = html;
        })
};
window.onload = importContent;