document.addEventListener("DOMContentLoaded", function() {
    // Create navbar
    const navbar = document.createElement('nav');

    // Create navbar items
    const navItems = ['Home', 'Contact'];
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
        <h1>Welcome, "name" !</h1>
        <p>Who is here with us today?</p>

    `;

    content.style.animation = 'fadeIn 2s ease-out';

    // Append content to body
    document.body.appendChild(content);
});
