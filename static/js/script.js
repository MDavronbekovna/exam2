// document.getElementById('burger-menu-toggle').addEventListener('click', function() {
//     var menu = document.getElementById('burger-menu');
//     menu.classList.toggle('hidden');
// });

// document.addEventListener('DOMContentLoaded', function() {
//     const burgerBtn = document.getElementById('burgerBtn');
//     const mobileMenu = document.getElementById('mobileMenu');

//     burgerBtn.addEventListener('click', function() {
//         mobileMenu.classList.toggle('hidden');
//     });
// });

    document.addEventListener('DOMContentLoaded', function() {
        const burgerBtn = document.getElementById('burgerBtn');
        const closeBtn = document.getElementById('closeBtn');
        const navMenu = document.getElementById('navbarSupportedContent');
        
        burgerBtn.addEventListener('click', function() {
            navMenu.classList.toggle('hidden');
            burgerBtn.classList.add('hidden');
            closeBtn.classList.remove('hidden');
        });

        closeBtn.addEventListener('click', function() {
            navMenu.classList.add('hidden');
            burgerBtn.classList.remove('hidden');
            closeBtn.classList.add('hidden');
        });
    });

