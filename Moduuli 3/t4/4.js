'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const target = document.getElementById('target')

students.forEach(student => {
  let element = document.createElement('option')
  element.textContent = student.name
  target.appendChild(element)
  element.value = student.id
})

