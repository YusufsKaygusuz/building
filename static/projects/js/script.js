let searchForm = document.querySelector('header .search-form');

document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
}

window.onscroll = () =>{
    searchForm.classList.remove('active')
}