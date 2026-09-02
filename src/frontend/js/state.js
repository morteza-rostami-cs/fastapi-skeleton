const AppState = {
  get(key, defaultValue = null) {
    const value = localStorage.getItem(key);

    if (value === null) {
      return defaultValue;
    }

    return JSON.parse(value);
  },

  set(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  },

  remove(key) {
    localStorage.removeItem(key);
  },
};
// we can let apps/pages to subscribe to storage changes later
// window.addEventListener("storage", ...)
