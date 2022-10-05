
//We're allowing user to start the search by pressing 'enter' key on the keyboard...
//...in addition to clicking the search icon
document.addEventListener('DOMContentLoaded', () => {
    let msg  = document.querySelector('#search');
    msg.addEventListener('keyup', event => {
        event.preventDefault();
        if (event.keyCode === 13) {
            document.querySelector('#perform_search').click();
        }
    })
});