// let navigation = document.getElementById("navigation");
// window.addEventListener("scroll", function () {
//     if (window.pageYOffset > 50) {
//         navigation.classList.add("active");
//     }
//     else {
//         navigation.classList.remove("active");
//     }
// })

let hamburger = document.querySelector('.hamburger');
hamburger.addEventListener('click', function () {
    hamburger.classList.toggle('open');
    // document.body.classList.toggle('menu-open');
})

let nav = document.querySelector('.hide-button');
nav.addEventListener('click', function () {
    nav.classList.toggle('aside');
    document.body.classList.toggle('nav-hidden');
})

// AOS.init();