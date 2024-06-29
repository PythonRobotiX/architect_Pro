// JavaScript for handling language switch and dynamic content loading
const lang = new URLSearchParams(window.location.search).get('lang') || 'en';

document.addEventListener('DOMContentLoaded', () => {
    loadContent(lang);
    showSection('biography'); // Show biography by default
});

function loadContent(language) {
    // Load content based on selected language
    // This can be expanded to load content dynamically from a CMS or API
    if (language === 'fa') {
        document.querySelector('.sidebar.left ul li a[href="#biography"]').innerText = 'بیوگرافی آریا';
        document.querySelector('.sidebar.left ul li a[href="#research"]').innerText = 'تحقیقات و توسعه (R&D)';
        document.querySelector('.sidebar.left ul li a[href="#portfolio"]').innerText = 'نمونه کارهای آریا';
        document.querySelector('.sidebar.left ul li a[href="#creator"]').innerText = 'سازنده نمونه کارهای معمار';
        document.querySelector('.sidebar.left ul li a[href="#projects"]').innerText = 'ما پروژه ها را می پذیریم';
        document.querySelector('.sidebar.left ul li a[href="#contact"]').innerText = 'تماس با ما';
        document.querySelector('.sidebar.left ul li a[href="#about"]').innerText = 'درباره ما';
        document.querySelector('#biography h1').innerText = 'بیوگرافی آریا';
        document.querySelector('#research h1').innerText = 'تحقیقات و توسعه (R&D)';
        document.querySelector('#portfolio h1').innerText = 'نمونه کارهای آریا';
        document.querySelector('#creator h1').innerText = 'سازنده نمونه کارهای معمار';
        document.querySelector('#projects h1').innerText = 'ما پروژه ها را می پذیریم';
        document.querySelector('#contact h1').innerText = 'تماس با ما';
        document.querySelector('#about h1').innerText = 'درباره ما';
        document.querySelector('#about-content').style.display = 'block';
    } else {
        document.querySelector('.sidebar.left ul li a[href="#biography"]').innerText = 'Arya\'s Biography';
        document.querySelector('.sidebar.left ul li a[href="#research"]').innerText = 'Research & Development (R&D)';
        document.querySelector('.sidebar.left ul li a[href="#portfolio"]').innerText = 'Arya\'s Portfolio';
        document.querySelector('.sidebar.left ul li a[href="#creator"]').innerText = 'Architect\'s Portfolio Creator';
        document.querySelector('.sidebar.left ul li a[href="#projects"]').innerText = 'We Accept Orders and Projects';
        document.querySelector('.sidebar.left ul li a[href="#contact"]').innerText = 'Contact Us';
        document.querySelector('.sidebar.left ul li a[href="#about"]').innerText = 'About Us';
        document.querySelector('#biography h1').innerText = 'Arya\'s Biography';
        document.querySelector('#research h1').innerText = 'Research & Development (R&D)';
        document.querySelector('#portfolio h1').innerText = 'Arya\'s Portfolio';
        document.querySelector('#creator h1').innerText = 'Architect\'s Portfolio Creator';
        document.querySelector('#projects h1').innerText = 'We Accept Orders and Projects';
        document.querySelector('#contact h1').innerText = 'Contact Us';
        document.querySelector('#about h1').innerText = 'About Us';
        document.querySelector('#about-content').style.display = 'block';
    }
}

function showSection(sectionId) {
    const sections = document.querySelectorAll('main section');
    sections.forEach(section => {
        section.style.display = 'none';
    });

    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.style.display = 'block';
    }
}

function toggleLanguage() {
    const currentLang = new URLSearchParams(window.location.search).get('lang') || 'en';
    const newLang = currentLang === 'en' ? 'fa' : 'en';
    window.location.search = `?lang=${newLang}`;
}
