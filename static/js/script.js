
    <script>
        const modeToggle = document.getElementById('mode-toggle');
        const body = document.body;

        modeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            const isDarkMode = body.classList.contains('dark-mode');
            modeToggle.textContent = isDarkMode ? 'Kunduzgi rejim' : 'Tungi rejim';
        });
    </script>
