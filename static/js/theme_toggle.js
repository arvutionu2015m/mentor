(function () {
  function getCookie(name) {
    const cookie = document.cookie.split('; ').find(row => row.startsWith(name + '='));
    return cookie ? cookie.split('=')[1] : null;
  }

  function setCookie(name, value) {
    document.cookie = `${name}=${value};path=/;max-age=31536000`;
  }

  function applyTheme(themeChoice) {
    let theme = themeChoice;

    if (theme === 'system') {
      const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      theme = prefersDark ? 'dark' : 'light';
    }

    const css = document.getElementById('theme-css');
    if (css) {
      css.href = `/static/css/admin_${theme}.css`;
    }

    const selector = document.getElementById('theme-select');
    if (selector) {
      selector.value = themeChoice;
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    let themeChoice = getCookie('admin_theme') || 'system';
    applyTheme(themeChoice);

    const selector = document.getElementById('theme-select');
    if (selector) {
      selector.addEventListener('change', function () {
        setCookie('admin_theme', this.value);
        applyTheme(this.value);
        location.reload(); // värskendame teema rakendamiseks
      });
    }
  });
})();
