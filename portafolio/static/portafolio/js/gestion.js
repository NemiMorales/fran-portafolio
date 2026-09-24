(() => {
  const dialog = document.querySelector('.creation-modal');
  const content = document.querySelector('#modal-content');
  const headers = { 'X-Requested-With': 'XMLHttpRequest' };
  let opener;
  let loading = false;
  let saving = false;
  const initPreview = (root) => {
    const input = root.querySelector('[name="imagen"]');
    const image = root.querySelector('.image-preview img');
    if (!input || !image) return;
    const update = () => {
      image.hidden = true;
      image.removeAttribute('src');
      try {
        const url = new URL(input.value);
        if (['https:', 'http:'].includes(url.protocol)) image.src = url.href;
      } catch { /* Keep the placeholder for an empty or invalid URL. */ }
    };
    image.onload = () => { image.hidden = false; };
    image.onerror = () => { image.hidden = true; };
    input.addEventListener('input', update);
    update();
  };
  initPreview(document);
  document.querySelectorAll('.creation-image img').forEach(image => {
    image.addEventListener('error', () => { image.hidden = true; });
    if (image.complete && !image.naturalWidth) image.hidden = true;
  });
  const rows = [...document.querySelectorAll('.creation')];
  const filters = document.querySelector('.filters');
  if (filters) {
    filters.hidden = false;
    filters.querySelectorAll('[data-filter]').forEach(button => {
      const filter = button.dataset.filter;
      button.querySelector('[data-count]').textContent = rows.filter(row => filter === 'all' || row.dataset.state === filter).length;
      button.addEventListener('click', () => {
        filters.querySelectorAll('button').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
        rows.forEach(row => { row.hidden = filter !== 'all' && row.dataset.state !== filter; });
        document.querySelector('#filter-empty').hidden = !rows.length || rows.some(row => !row.hidden);
      });
    });
  }
  if (!dialog || typeof dialog.showModal !== 'function') return;
  document.addEventListener('click', async event => {
    const close = event.target.closest('[data-close]');
    if (close && dialog.contains(close)) {
      event.preventDefault();
      if (saving) return;
      dialog.close();
      return;
    }
    const link = event.target.closest('[data-modal]');
    if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    if (loading) return;
    loading = true;
    opener = link;
    link.setAttribute('aria-busy', 'true');
    const error = document.querySelector('#page-error');
    error.hidden = true;
    try {
      const response = await fetch(link.href, { headers });
      if (response.redirected) { window.location.assign(response.url); return; }
      if (!response.ok) throw new Error('load');
      content.innerHTML = await response.text();
      initPreview(content);
      dialog.showModal();
      document.body.classList.add('modal-open');
      content.querySelector('[name="nombre"]').focus();
    } catch {
      error.textContent = 'No se pudo abrir el formulario. Intenta nuevamente.';
      error.hidden = false;
    } finally {
      loading = false;
      link.removeAttribute('aria-busy');
    }
  });
  dialog.addEventListener('close', () => {
    document.body.classList.remove('modal-open');
    opener?.focus();
  });
  dialog.addEventListener('click', event => {
    if (saving) return;
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
  dialog.addEventListener('submit', async event => {
    const form = event.target;
    if (!form.matches('.creation-form')) return;
    event.preventDefault();
    const button = form.querySelector('[type="submit"]');
    if (button.disabled) return;
    saving = true;
    button.disabled = true;
    button.textContent = 'Guardando…';
    const closeWhileSaving = event => { event.preventDefault(); };
    dialog.addEventListener('cancel', closeWhileSaving);
    try {
      const response = await fetch(form.action, { method: 'POST', headers, body: new FormData(form) });
      if (response.redirected) { window.location.assign(response.url); return; }
      if (response.status === 422) {
        content.innerHTML = await response.text();
        initPreview(content);
        content.querySelector('.form-error').setAttribute('tabindex', '-1');
        content.querySelector('.form-error').focus();
      } else if (response.ok) {
        const data = await response.json();
        window.location.assign(data.redirect);
      } else throw new Error('save');
    } catch {
      const error = form.querySelector('[data-submit-error]');
      error.textContent = 'No se pudo guardar. Revisa tu conexión e intenta nuevamente.';
      error.hidden = false;
    } finally {
      saving = false;
      button.disabled = false;
      button.textContent = form.action.includes('/editar/') ? 'Guardar cambios' : 'Guardar creación';
      dialog.removeEventListener('cancel', closeWhileSaving);
    }
  });
})();
