document.addEventListener("DOMContentLoaded", function() {
    // Create navbar
    const navbar = document.createElement('nav');

    // Create navbar items
    const navItems = ['Home', 'About', 'Services', 'Contact'];
    navItems.forEach(item => {
        const navLink = document.createElement('a');
        navLink.textContent = item;
        navLink.href = `#${item.toLowerCase()}`;
        navbar.appendChild(navLink);
    });

    // Append navbar to body
    document.body.appendChild(navbar);

    // Create homepage content
    const content = document.createElement('div');
    content.innerHTML = `
        <h1>Welcome to Cyber</h1>
        <p>Explore and have fun with the interactive navbar and vibrant designs!</p>
    `;

    // Add a playful animation to content
    content.style.animation = 'fadeIn 2s ease-out';

    // Append content to body
    document.body.appendChild(content);

    // Add a cool background color change on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            document.body.style.backgroundColor = '#ffe0b2'; // Light orange after scrolling
        } else {
            document.body.style.backgroundColor = '#f0f8ff'; // Original light blue
        }
    });
});
