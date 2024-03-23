/*!
* Start Bootstrap - Heroic Features v5.0.6 (https://startbootstrap.com/template/heroic-features)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-heroic-features/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
const header = document.getElementById('header');
const text = 'RECIPE M[AI]KER'; // Text to be typed out
let index = 0;

function type() {
  if (index < text.length) {
    header.textContent += text.charAt(index);
    index++;
    setTimeout(type, 150); // Delay between typing each character
  }
}

type(); // Start the typing animation