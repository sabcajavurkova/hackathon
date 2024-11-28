document.addEventListener("DOMContentLoaded", function() {
    // Získáme formulář a jeho inputy
    const loginForm = document.querySelector(".login");
    const usernameInput = loginForm.querySelector("input[name='username']");
    const passwordInput = loginForm.querySelector("input[name='password']");
    const submitButton = loginForm.querySelector("button[type='submit']");
    
    // Funkce pro kontrolu, jestli jsou všechna pole vyplněná
    function validateForm() {
        if (usernameInput.value.trim() === "" || passwordInput.value.trim() === "") {
            submitButton.disabled = true; // Zakázat tlačítko, pokud jsou pole prázdná
            submitButton.textContent = "Vyplňte všechna pole";
        } else {
            submitButton.disabled = false; // Povolit tlačítko, když jsou pole vyplněná
            submitButton.textContent = "Přihlásit se";
        }
    }

    // Spustíme validaci, když uživatel zadává hodnoty
    usernameInput.addEventListener("input", validateForm);
    passwordInput.addEventListener("input", validateForm);

    // Před odesláním formuláře můžeme udělat nějakou kontrolu (např. zkontrolovat formát uživatelského jména)
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Zabráníme odeslání formuláře

        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        // Zde by byla kontrola (např. formát jména nebo hesla), případně AJAX volání na server
        if (username && password) {
            // Můžeme provést odeslání formuláře, pokud všechno vypadá dobře
            loginForm.submit();
        }
    });

    // Inicializujeme kontrolu formuláře při načtení stránky
    validateForm();
});
