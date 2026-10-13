'use strict';
document.documentElement.classList.add('js');
const status = document.querySelector('#interaction-status');
const figureDialog = document.querySelector('#figure-dialog');
let figureTrigger;
if (typeof figureDialog.showModal === 'function') {
  document.querySelectorAll('.zoom-image').forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    figureTrigger = link;
    const caption = link.dataset.caption;
    document.querySelector('#dialog-image').src = link.href;
    document.querySelector('#dialog-image').alt = caption;
    document.querySelector('#figure-caption').textContent = caption;
    document.querySelector('#dialog-source').href = link.href;
    figureDialog.showModal();
    document.querySelector('#close-figure').focus();
  }));
  document.querySelector('#close-figure').addEventListener('click', () => figureDialog.close());
  figureDialog.addEventListener('click', event => {
    if (event.target !== figureDialog) return;
    const rect = figureDialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) figureDialog.close();
  });
  figureDialog.addEventListener('close', () => figureTrigger?.focus());
}

if (['localhost','127.0.0.1'].includes(location.hostname) &&
    location.pathname.split('/')[1] === 'Personal') {
  document.querySelectorAll('[data-preview-path]').forEach(link => { link.href = link.dataset.previewPath; });
}

const menu = document.querySelector('[data-menu]');
const nav = document.querySelector('#nav-links');
menu?.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('open', open);
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  menu?.setAttribute('aria-expanded', 'false');
  nav.classList.remove('open');
}));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav?.classList.contains('open')) {
    nav.classList.remove('open');
    menu.setAttribute('aria-expanded', 'false');
    menu.focus();
  }
});

const siteSwitcher = document.querySelector('[data-site-switcher]');
document.addEventListener('click', event => {
  if (siteSwitcher?.open && !siteSwitcher.contains(event.target)) siteSwitcher.open = false;
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && siteSwitcher?.open) {
    siteSwitcher.open = false;
    siteSwitcher.querySelector('summary').focus();
  }
});
