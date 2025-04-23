const list = document.getElementById('target')
const listItems = ['First Item', 'Second Item', 'Third Item']

listItems.forEach(item => {
    let listElement = document.createElement('li')
    listElement.textContent = item
    list.appendChild(listElement)
})

const second = document.getElementsByTagName('li')[1]
second.classList.add('my-item')