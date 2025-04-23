'use strict';
const names = ['John', 'Paul', 'Jones'];
const list = document.getElementById('target')

names.forEach(name => {
    let listElement = document.createElement('li')
    listElement.textContent = name
    list.appendChild(listElement)
})