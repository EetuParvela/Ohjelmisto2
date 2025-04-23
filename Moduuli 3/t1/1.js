const list = document.getElementById('target')
const listItems = '<li>First item</li>\n' +
    '<li>Second item</li>\n' +
    '<li>Third item</li>'

list.classList.add('my-list')
list.innerHTML = listItems;