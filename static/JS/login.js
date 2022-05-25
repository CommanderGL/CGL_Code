const sp = document.querySelector('#show_password');
const pi = document.querySelector('[type="password"]');

sp.addEventListener('click', () => {
	if (sp.checked) {
		pi.setAttribute('type', 'text');
	} else {
		pi.setAttribute('type', 'password');
	}
});