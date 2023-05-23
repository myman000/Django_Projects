const cameraElement = document.getElementById('camera');
const cameraMenuElement = document.getElementById('camera-menu');
const contactFormElement = document.getElementById('contact-form');
const leftMobileButtonElement = document.querySelector('.left-mobile-button');
const leftButtonIconsMenuElement = document.querySelector('.left-button-icons-menu');


const menuEventHandler = () => {
    if (leftButtonIconsMenuElement.style.display === 'none'){
        leftButtonIconsMenuElement.style.display = 'grid';
    }
    else{
        leftButtonIconsMenuElement.style.display = 'none';
    }
};


const cameraEventHandler = () =>{
    if (cameraMenuElement.style.display === 'none'){
        cameraMenuElement.style.display = 'flex';
        contactFormElement.classList.toggle ('flash');
    }
    else{
        cameraMenuElement.style.display = 'none';
        contactFormElement.classList.toggle ('flash');
    }
};

leftMobileButtonElement.addEventListener('click',menuEventHandler);
cameraElement.addEventListener('click',cameraEventHandler);