const showMenuElement = document.querySelector('.show-menus');
const taskMenuItemsElement = document.querySelector('.task-menus-items');

function showMenu(){
    if (taskMenuItemsElement.style.display === 'none'){
        taskMenuItemsElement.style.display = 'flex';
    }
    else{
        taskMenuItemsElement.style.display = 'none';
    }
}

showMenuElement.addEventListener('click',showMenu);